import numpy as np

from tldry.nlp import TextCleaner
from tldry.pdist_maker import PDistMaker


DEFAULT_LANGUAGE = 'english'


class TLDRy:
    damping = 0.85

    def __init__(self, language=DEFAULT_LANGUAGE,
                 min_sent_len=2, min_df=2):
        self.language = language
        self.text_cleaner = TextCleaner(
            language=language,
            min_sent_len=min_sent_len,
        )
        self.dist_matrix_maker = PDistMaker(
            min_df=min_df,
        )

    def summarize(self, text, topn=5, with_scores=False,
                  sort_by_position=False):
        clean_text = self.text_cleaner.fit_transform(text)
        raw_sentences = self.text_cleaner.raw_sentences

        if not raw_sentences:
            return []

        distance_matrix = self.dist_matrix_maker.fit_transform(clean_text)

        sentence_scores = self.textrank(distance_matrix)

        argsorted_ids = np.argsort(sentence_scores)[-topn:][::-1]
        if sort_by_position:
            argsorted_ids = sorted(argsorted_ids)

        topn_sentences = [raw_sentences[i] for i in argsorted_ids]

        if with_scores:
            scores = sentence_scores[argsorted_ids]
            return topn_sentences, scores

        return topn_sentences

    def textrank(self, matrix):

        dangling_nodes = np.where(matrix.sum(axis=1) == 0)[0]

        p = np.repeat(1 / len(matrix), len(matrix))

        for node in dangling_nodes:
            matrix[node] = p

        matrix /= matrix.sum(axis=1)

        matrix = (
            self.damping * matrix +
            (1 - self.damping) * np.outer(np.ones(len(matrix)), p)
        )

        eigenvalues, eigenvectors = np.linalg.eigh(matrix.T)
        ind = eigenvalues.argmax()
        largest = np.array(eigenvectors[:, ind]).flatten().real
        norm = largest.sum()

        return largest / norm
