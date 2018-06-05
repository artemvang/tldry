import pytest

from tldry import TLDRy


@pytest.fixture
def english_tldr():
    return TLDRy(language='english')


@pytest.fixture
def russian_tldr():
    return TLDRy(language='russian')


@pytest.fixture
def russian_text():
    with open('tests/text_data/russian_review.txt') as f:
        text = f.read()

    return text


@pytest.fixture
def english_text():
    with open('tests/text_data/english_review.txt') as f:
        text = f.read()

    return text
