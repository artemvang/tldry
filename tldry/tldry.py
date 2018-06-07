import itertools

import numpy as np

from tldry.nlp import TextCleaner


"""
Text summarizer algorithm based on this work https://arxiv.org/abs/1210.3312

"""


DEFAULT_LANGUAGE = 'english'


class TLDRy:

    def __init__(self, language=DEFAULT_LANGUAGE,
                 min_sent_len=1, min_df=2):
        self.text_cleaner = TextCleaner(
            language=language,
            min_sent_len=min_sent_len,
            min_df=min_df,
        )

    def summarize(self, text, topn=5, with_scores=False):
        clean_sentences = self.text_cleaner.transform(text)
        raw_sentences = self.text_cleaner.raw_sentences

        if not raw_sentences:
            return []

        sentences_matrix = self.build_sentences_matrix(clean_sentences)
        mean_sent = sentences_matrix.mean(axis=0)[:, None]
        mean_char = sentences_matrix.mean(axis=1)

        sentence_scores = (sentences_matrix @ mean_sent).flatten() * mean_char

        argsorted_ids = np.argsort(sentence_scores)[-topn:][::-1]
        topn_sentences = [raw_sentences[i] for i in argsorted_ids]

        if with_scores:
            scores = sentence_scores[argsorted_ids]
            return topn_sentences, scores

        return topn_sentences


    def build_sentences_matrix(self, clean_sentences):
        possible_chars = set(itertools.chain.from_iterable(clean_sentences))
        char2id = {char: i for i, char in enumerate(possible_chars)}

        matrix = np.zeros((len(clean_sentences), len(char2id)))

        for sent_i, sent in enumerate(clean_sentences):
            for char in sent:
                matrix[sent_i, char2id[char]] += 1

        matrix /= np.linalg.norm(matrix, axis=1, keepdims=True)
        return matrix
