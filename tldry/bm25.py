from collections import defaultdict

import numpy as np


class BM25DistanceScorer:
    k1 = 1.5
    b = 0.75

    def __init__(self, min_df=2, n_gram=3):
        self.min_df = min_df
        self.n_gram = n_gram

        self.vocabulary_ = {}
        self.idf_ = None

    def transform_tf(self, corpus):
        corpus_size = len(corpus)

        tf_matrix = np.zeros((corpus_size, len(self._vocabulary)))
        for sent_id, kws in enumerate(corpus):
            counter = 0
            while counter < len(kws):
                best_keyword_id = None
                best_size = 0
                for n in range(self.n_gram, 0, -1):
                    kw = tuple(kws[counter: counter+n])
                    keyword_id = self._vocabulary.get(kw)
                    if keyword_id is None:
                        continue
                    else:
                        best_keyword_id = keyword_id
                        best_size = n
                        break

                if best_keyword_id is not None:
                    tf_matrix[sent_id, best_keyword_id] += 1
                    counter += best_size
                else:
                    counter += 1

        return tf_matrix

    def fit_transform(self, corpus):
        self.fit(corpus)
        return self.transform(corpus)

    def transform(self, corpus):
        tf_matrix = self.transform_tf(corpus)
        sent_sizes = np.sum(tf_matrix, axis=1)
        sent_sizes[sent_sizes == 0] = 1

        bm25_matrix = np.copy(tf_matrix)

        sent_sizes /= np.mean(sent_sizes)

        bm25_matrix = (self._idf * bm25_matrix * (self.k1 + 1)
                       / (bm25_matrix + self.k1 * (1 - self.b + self.b * sent_sizes[:, None])))

        distance_matrix = np.inner(tf_matrix, bm25_matrix)

        return distance_matrix

    def fit(self, corpus):
        corpus_size = len(corpus)
        self._vocabulary = {}

        keywords_df = defaultdict(int)

        for kws in corpus:
            for kw in set(self.extract_keywords(kws)):
                keywords_df[kw] += 1

        keywords_idf = [(kw, np.log((corpus_size - df + 0.5)/(df + 0.5)))
                        for kw, df in keywords_df.items()
                        if df >= self.min_df]

        self._idf = np.zeros(len(keywords_idf))
        for kw_id, (kw, idf) in enumerate(keywords_idf):
            self._vocabulary[kw] = kw_id
            self._idf[kw_id] = idf

        self._idf[self._idf < 0] = np.mean(self._idf) * 0.25

        return self

    def extract_keywords(self, sentence_tokens):
        keywords = []
        for n in range(1, self.n_gram + 1):
            for t in range(len(sentence_tokens) - n + 1):
                kw = tuple(sentence_tokens[t: t+n])
                keywords.append(kw)
        return keywords
