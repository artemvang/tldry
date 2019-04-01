from collections import defaultdict

import numpy as np
from scipy.stats import boxcox


class PDistMaker:

    def __init__(self, min_df=2):
        self.min_df = min_df

        self.vocabulary_ = {}

    def transform_tf(self, corpus):
        corpus_size = len(corpus)

        tf_matrix = np.zeros((corpus_size, len(self.vocabulary_)))
        for sent_id, kws in enumerate(corpus):
            for kw in kws:
                kw_id_df = self.vocabulary_.get(kw)
                if kw_id_df is not None:
                    kw_id, df = kw_id_df
                    tf_matrix[sent_id, kw_id] += df

        return tf_matrix

    def fit_transform(self, corpus):
        self.fit(corpus)
        return self.transform(corpus)

    def transform(self, corpus):
        tf_matrix = self.transform_tf(corpus)

        tf_matrix[np.sum(tf_matrix, axis=1) == 0] = 1e-8
        tf_matrix /= np.linalg.norm(tf_matrix, axis=1, keepdims=True)

        distance_matrix = (tf_matrix.dot(tf_matrix.T) + 1) / 2

        return distance_matrix

    def fit(self, corpus):
        self.vocabulary_ = {}

        keywords_df = defaultdict(int)

        for kws in corpus:
            for kw in set(kws):
                keywords_df[kw] += 1

        kw2df = [(kw, df) for kw, df in keywords_df.items()
                 if df >= self.min_df]

        for kw_id, (kw, df) in enumerate(kw2df):
            self.vocabulary_[kw] = [kw_id, len(corpus) / df]

        vals = [s for _, s in self.vocabulary_.values()]
        _, lamb = boxcox(vals)

        for key, val in zip(self.vocabulary_, boxcox(vals, lamb)):
            self.vocabulary_[key][1] = val

        return self
