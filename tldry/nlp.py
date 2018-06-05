import pkgutil
import importlib
import os.path as op

from Stemmer import Stemmer
import regex as re

import tldry.stopwords as stopwords


stopwords_dirname = op.dirname(stopwords.__file__)
AVAILABLE_LANGUAGES = frozenset(
    name for _, name, _ in pkgutil.iter_modules([stopwords_dirname]))


class TextCleaner:
    paragraph_re = re.compile(r'[.!?]*\n+')
    word_regex = re.compile(r'[^\W_]+')
    sent_regex = re.compile(r'(?<=[.!?]+)\s+')

    def __init__(self, language, min_token_len, min_sent_len):
        if language not in AVAILABLE_LANGUAGES:
            err = (f"Language '{language}' is not available, "
                   f"choose from [{', '.join(AVAILABLE_LANGUAGES)}]")
            raise ValueError(err)

        self.min_token_len = min_token_len
        self.min_sent_len = min_sent_len

        self.stem = Stemmer(language).stemWord

        stopwords = importlib.import_module(
            f'tldry.stopwords.{language}').stopwords
        self.stopwords = frozenset(self.stem(s) for s in stopwords)

        self.raw_sentences = []

    def fit_transform(self, text):
        raw_sentences_ = self.sent_tokenize(text)
        clean_sentences_ = [self.clean_sentence(self.word_tokenize(sent))
                           for sent in raw_sentences_]

        raw_sentences = []
        clean_sentences = []
        for c, r in zip(clean_sentences_, raw_sentences_):
            if len(c) < self.min_sent_len:
                continue
            clean_sentences.append(c)
            raw_sentences.append(r)

        self.raw_sentences = raw_sentences

        return clean_sentences

    def sent_tokenize(self, text):
        text = self.paragraph_re.sub('. ', text)
        return self.sent_regex.split(text)

    def word_tokenize(self, sentence):
        return self.word_regex.findall(sentence)

    def clean_sentence(self, sentence):
        new_sentence = []
        for tok in sentence:
            tok = self.stem(tok.lower())
            if self.is_valid_token(tok):
                new_sentence.append(tok)

        return new_sentence

    def is_valid_token(self, token):
        return token not in self.stopwords and len(token) >= self.min_token_len
