

def test_russian_text(russian_tldr, russian_text):
    summary = russian_tldr.summarize(russian_text)

    assert summary == [
        (
            'Фабульно это без пяти минут трагедия с четким моральным '
            'посылом — каждый получает кару за свои грехи.'
        ),
        (
            'Даже вышеупомянутый полицейский, поющий в караоке и берущий на '
            'себя функцию Бога, находится все время в одном состоянии, '
            'поэтому в его образе нет никакой иронии.'
        ),
        (
            'Каждый кадр настолько вылизан, выставлен с четкими цветовыми '
            'акцентами, что красота становится абсолютом, перманентным состоянием.'
        ),
        (
            'Без пяти минут античная трагедия едва сходится с маньеристским '
            'боевиком, в котором полтора часа красивые (и не очень) люди по '
            'инерции мстят друг другу, освещенные неоновыми '
            'лампами и красными светильниками.'
        ),
        (
            'Кэмп избавляет боевик про месть от морали, от самой '
            'возможности вынесения оценочных суждений.'
        ),
    ]


def test_english_text(english_tldr, english_text):
    summary = english_tldr.summarize(english_text)

    assert summary == [
        (
            'The director also said this about the film, "From the beginning, '
            'I had the idea of a thriller produced as a western, all in '
            'the Far East, and with a modern cowboy hero." Many people would '
            'assume that the "cowboy hero" would be Julian, but it becomes '
            'apparent over the course of the film that he was most '
            'likely subtlety referring to Chang.'
        ),
        (
            'The sense of surreal mysticism that the neon drenched streets of '
            'Bangkok at night creates is almost dream like, and covers the '
            'screen in a hellish red and orange glow with slight variations '
            'with other bright colours, a thematic artistic choice that makes '
            'the Bangkok setting look like hell has corrupted the earth.'
        ),
        (
            'It features tropes associated with westerns (silent characters, '
            'justice being brought to the lawless, ect) and has a slow, '
            'mesmerizing pace that borders on the surreal and fantastical.'
        ),
        (
            'This is a visual cue which evokes imagery of the fist fight with '
            'Chang later on in the film, in which Julian in knocked to the '
            'ground with Chang standing behind him, with his fists raised '
            'in the same position as the statue.'
        ),
        (
            'Because the film is basically a larger than life clash between '
            'good and evil, its appropriate that the film has music of '
            'high energy and operatic sounds.'
        ),
    ]
