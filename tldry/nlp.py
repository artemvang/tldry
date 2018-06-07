import pkgutil
import importlib
import os.path as op
from collections import defaultdict

from Stemmer import Stemmer
import regex as re

import tldry.stopwords as stopwords


stopwords_dirname = op.dirname(stopwords.__file__)
AVAILABLE_LANGUAGES = frozenset(
    name for _, name, _ in pkgutil.iter_modules([stopwords_dirname]))


class TextCleaner:
    word_regex = re.compile(r'[^\W\d_]+')
    sent_regex = re.compile(r'(?<=(?:[\p{lower}\d]|[^\w])\s*[.!?\n]+)\s*(?=(?:[\p{upper}\d]|[^\w]))')

    def __init__(self, language, min_sent_len, min_df):
        if language not in AVAILABLE_LANGUAGES:
            err = (f"Language '{language}' is not available, "
                   f"choose from [{', '.join(AVAILABLE_LANGUAGES)}]")
            raise ValueError(err)

        self.min_sent_len = min_sent_len
        self.min_df = min_df

        self.stem = Stemmer(language).stemWord

        stopwords = importlib.import_module(f'tldry.stopwords.{language}')
        self.stopwords = frozenset(stopwords.stopwords)

        self.raw_sentences = []

    def transform(self, text):
        raw_sentences_ = self.sent_tokenize(text)
        clean_sentences_ = [self.clean_sentence(self.word_tokenize(sent))
                            for sent in raw_sentences_]
        filtered_clean_sentences_ = self.filter_by_min_df(clean_sentences_)

        raw_sentences = []
        clean_sentences = []
        for c, r in zip(filtered_clean_sentences_, raw_sentences_):
            if len(c) < self.min_sent_len:
                continue
            clean_sentences.append(c)
            raw_sentences.append(r)

        self.raw_sentences = raw_sentences

        ultra_stem_clean_sentences = self.ultra_stem_sentences(clean_sentences)

        return ultra_stem_clean_sentences

    def ultra_stem_sentences(self, clean_sentences):
        return [[t[0] for t in sent] for sent in clean_sentences]

    def filter_by_min_df(self, clean_sentences):
        df = defaultdict(int)
        for sent in clean_sentences:
            for tok in set(sent):
                df[tok] += 1

        return [[tok for tok in sent if df[tok] >= self.min_df]
                for sent in clean_sentences]

    def sent_tokenize(self, text):
        return self.sent_regex.split(text)

    def word_tokenize(self, sentence):
        return self.word_regex.findall(sentence)

    def clean_sentence(self, sentence):
        new_sentence = []
        for tok in sentence:
            tok = tok.lower()
            if tok in self.stopwords:
                continue
            new_sentence.append(self.stem(tok))

        return new_sentence
