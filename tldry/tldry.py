import numpy as np

from tldry.nlp import TextCleaner
from tldry.bm25 import BM25DistanceScorer


DEFAULT_LANGUAGE = 'russian'


class TLDRy:
    delta = 0.85

    def __init__(self, language=DEFAULT_LANGUAGE,
                 min_token_len=4, min_sent_len=2,
                 min_df=2, n_gram=3):
        self.text_cleaner = TextCleaner(
            min_token_len=min_token_len,
            min_sent_len=min_sent_len,
            language=language
        )
        self.bm25_dist_scorer = BM25DistanceScorer(
            min_df=min_df,
            n_gram=n_gram
        )

    def summarize(self, text, topn=5, with_scores=False):
        clean_text = self.text_cleaner.fit_transform(text)
        raw_sentences = self.text_cleaner.raw_sentences

        if not raw_sentences:
            return []

        distance_matrix = self.bm25_dist_scorer.fit_transform(clean_text)
        fitted_distance_matrix = self.preprocess_distance_matrix(distance_matrix)

        sentence_scores = self.textrank(fitted_distance_matrix)

        argsorted_ids = np.argsort(sentence_scores)[-topn:][::-1]
        topn_sentences = [raw_sentences[i] for i in argsorted_ids]

        if with_scores:
            scores = sentence_scores[argsorted_ids]
            return topn_sentences, scores

        return topn_sentences

    def preprocess_distance_matrix(self, distance_matrix):
        stds = np.std(distance_matrix, axis=1)
        stds[stds == 0] = 1
        distance_matrix /= stds[:, None]
        means = np.mean(distance_matrix, axis=1)

        distance_matrix[distance_matrix <= means[:, None]] = 0
        distance_matrix[distance_matrix > means[:, None]] = 1

        sums = distance_matrix.sum(axis=1)
        sums[sums == 0] = 1
        distance_matrix /= sums[:, None]

        return distance_matrix

    def textrank(self, distance_matrix):
        sentences_count = len(distance_matrix)

        basic_probability_matrix = ((1 - self.delta) *
                                    np.ones_like(distance_matrix.T) /
                                    sentences_count)
        matrix = self.delta * distance_matrix.T
        matrix += basic_probability_matrix

        eig_vector = np.ones((sentences_count, )) / sentences_count
        error_val = 1.0

        while error_val > 1e-3:
            next_eig = np.dot(matrix, eig_vector)
            error_val = np.linalg.norm(next_eig - eig_vector)
            eig_vector = next_eig

        return eig_vector
