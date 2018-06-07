from collections import defaultdict

import numpy as np


class PDistMaker:

    def __init__(self, min_df=2):
        self.min_df = min_df

        self.vocabulary_ = {}

    def transform_tf(self, corpus):
        corpus_size = len(corpus)

        tf_matrix = np.zeros((corpus_size, len(self.vocabulary_)))
        for sent_id, kws in enumerate(corpus):
            for kw in kws:
                kw_id = self.vocabulary_.get(kw)
                if kw_id is not None:
                    tf_matrix[sent_id, kw_id] += 1

        return tf_matrix

    def fit_transform(self, corpus):
        self.fit(corpus)
        return self.transform(corpus)

    def transform(self, corpus):
        tf_matrix = self.transform_tf(corpus)
        sent_sizes = np.asarray([len(sent) for sent in corpus])[:, None]

        sizes_matrix = np.log(sent_sizes.dot(sent_sizes.T))
        sizes_matrix[sizes_matrix == 0] = 1

        distance_matrix = np.inner(tf_matrix, tf_matrix)

        return distance_matrix / sizes_matrix

    def fit(self, corpus):
        corpus_size = len(corpus)
        self.vocabulary_ = {}

        keywords_df = defaultdict(int)

        for kws in corpus:
            for kw in set(kws):
                keywords_df[kw] += 1

        kw2df = [(kw, df) for kw, df in keywords_df.items()
                 if df >= self.min_df]

        for kw_id, (kw, df) in enumerate(kw2df):
            self.vocabulary_[kw] = kw_id

        return self
