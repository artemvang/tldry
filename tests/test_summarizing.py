

def test_russian_text(russian_tldr, russian_text):
    summary = russian_tldr.summarize(russian_text)

    assert summary == [
        'Но само это обозначение могло появиться только в постмодернистскую эпоху.',
        'К нему можно причислить «Лебединое Озеро» Чайковского, почтовые открытки, некоторые оперы Вагнера, Голливуд 50-х.',
        'Один из самых переоцененных и недооцененных режиссеров современности, о котором говорят все, но мало кто всерьёз.',
        'Не для пущего смысла, а исключительно из эстетических соображений.',
        'Смех без смеха.',

    ]


def test_english_text(english_tldr, english_text):
    summary = english_tldr.summarize(english_text)

    assert summary == [
        'The films story is told primarily though visuals and music, with very sparse Dialogue, so the music at times acts as the voice of the situation, helping us paint a much larger more epic picture of what’s going on.'
        'The sense of surreal mysticism that the neon drenched streets of Bangkok at night creates is almost dream like, and covers the screen in a hellish red and orange glow with slight variations with other bright colours, a thematic artistic choice that makes the Bangkok setting look like hell has corrupted the earth.'
        'The cast is lead by Ryan Gosling, who despite top billing, is actually very underplayed and the film is essentially about his redemption at the hands of Chang, the Thai police Lieutenant played by relative newcomer Vithaya Pansringarm.'
        'He also appears to show a level of all knowing abilities, as he senses the incoming danger of a gun fight before it even occurs, and at one point demonstrates his talent for vanishing completely after turning a corner while he is being followed.'
        'He home is surrounded by nature, which gives off the idea of heaven, or paradise, and that Chang (God) is residing in a place of peace and purity, while the inhabitants of the corrupt seedy Bangkok are condemned to rainy, smoggy, moody looking areas with the hellish red and orange lights bearing down.'
    ]
