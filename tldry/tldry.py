import numpy as np

from tldry.nlp import TextCleaner
from tldry.pdist_maker import PDistMaker


DEFAULT_LANGUAGE = 'english'


def get_distance(sent1, sent2):
    rate = 0
    for s1 in sent1:
        for s2 in sent2:
            rate += int(s1 == s2)
    # common = len(set(sent1) & set(sent2))

    norm = max(np.log(len(sent1) * len(sent2)), 1.)
    return rate / norm


class TLDRy:
    damping = 0.85

    def __init__(self, language=DEFAULT_LANGUAGE,
                 min_sent_len=2, min_df=2):
        self.text_cleaner = TextCleaner(
            language=language,
            min_sent_len=min_sent_len,
        )
        self.dist_matrix_maker = PDistMaker(
            min_df=min_df,
        )

    def summarize(self, text, topn=5, with_scores=False,
                  sort_by_position=True):
        clean_text = self.text_cleaner.fit_transform(text)
        raw_sentences = self.text_cleaner.raw_sentences

        if not raw_sentences:
            return []

        distance_matrix = self.dist_matrix_maker.fit_transform(clean_text)
        fitted_distance_matrix = self.preprocess_distance_matrix(
            distance_matrix)

        sentence_scores = self.textrank(fitted_distance_matrix)

        argsorted_ids = np.argsort(sentence_scores)[-topn:][::-1]
        if sort_by_position:
            argsorted_ids = sorted(argsorted_ids)

        topn_sentences = [raw_sentences[i] for i in argsorted_ids]

        if with_scores:
            scores = sentence_scores[argsorted_ids]
            return topn_sentences, scores

        return topn_sentences

    def preprocess_distance_matrix(self, distance_matrix):
        sums = distance_matrix.sum(axis=1)
        sums[sums == 0] = 1
        distance_matrix /= sums[:, None]

        return distance_matrix

    def textrank(self, distance_matrix):
        sentences_count = len(distance_matrix)

        basic_probability_matrix = ((1 - self.damping) *
                                    np.ones_like(distance_matrix) /
                                    sentences_count)
        matrix = self.damping * distance_matrix.T
        matrix += basic_probability_matrix

        eig_vector = np.ones((sentences_count, )) / sentences_count
        error_val = 1.0

        while error_val > 1e-4:
            next_eig = np.dot(matrix, eig_vector)
            error_val = np.linalg.norm(next_eig - eig_vector)
            eig_vector = next_eig

        return eig_vector
