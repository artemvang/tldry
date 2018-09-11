

def test_russian_text(russian_tldr, russian_text):
    summary = russian_tldr.summarize(russian_text)

    assert summary == [
        (
            'Это не четкий термин, но некий тип чувствительности, крикливой '
            'эстетичности, порой предельно серьезной, иногда ироничной, а '
            'зачастую и вовсе отвергающей явную иронию.'),
        (
            'Без пяти минут античная трагедия едва сходится с маньеристским '
            'боевиком, в котором полтора часа красивые (и не очень) люди по '
            'инерции мстят друг другу, освещенные неоновыми лампами и '
            'красными светильниками.'),
        (
            'Предельная серьезность интонации избавляет фильм от морали.'
        ),
        (
            'Каждый кадр настолько вылизан, выставлен с четкими цветовыми '
            'акцентами, что красота становится абсолютом, '
            'перманентным состоянием.'),
        (
            'Кэмп избавляет боевик про месть от морали, от самой возможности '
            'вынесения оценочных суждений.'
        ),
    ]


def test_english_text(english_tldr, english_text):
    summary = english_tldr.summarize(english_text)

    assert summary == [
        (
            'The film blends genre\'s in fairly interesting ways, as this '
            'film is essentially a western masquerading as a '
            'eastern neo noir crime film.'
        ),
        (
            'The director also said this about the film, "From the beginning, '
            'I had the idea of a thriller produced as a western, all in the '
            'Far East, and with a modern cowboy hero." Many people would '
            'assume that the "cowboy hero" would be Julian, but it becomes '
            'apparent over the course of the film that he was most '
            'likely subtlety referring to Chang.'
        ),
        (
            'Its the films clashing of east and west which is interesting as '
            'we feel like we are watching a western fused with elements of '
            'samurai films, though the film takes more of its cues from '
            'Sergio Leonne rather than Akira Kurosawa.'
        ),
        (
            'This is a visual cue which evokes imagery of the fist fight '
            'with Chang later on in the film, in which Julian in knocked '
            'to the ground with Chang standing behind him, with his fists '
            'raised in the same position as the statue.'
        ),
        (
            'He fights Chang about of frustration, realising Chang is '
            'possibly God and he is angry at God because he feels he has '
            'been created to be the way he is rather than accepting that his '
            'mother is the source of his problems and is the one who '
            'manipulated him and his brother into getting into '
            'crime in the first place.'
        ),
    ]
