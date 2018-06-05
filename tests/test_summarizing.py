

def test_russian_text(russian_tldr, russian_text):
    summary = russian_tldr.summarize(russian_text)

    assert summary == [
        (
            'В 1964-м культуролог, искусствовед (и просто лучший человек '
            'на Земле) Сьюзен Зонтаг написала важное эссе «Заметки о кэмпе», '
            'в котором тезисно наметила важные черты этого понятия.'
         ),
        (
            'Каждый кадр настолько вылизан, выставлен с четкими цветовыми '
            'акцентами, что красота становится абсолютом, '
            'перманентным состоянием.'
         ),
        (
            'Кэмп избавляет боевик про месть от морали, от самой '
            'возможности вынесения оценочных суждений.'
        ),
        (
            'Зонтаг пишет, что кэмп отказывается как от гармонии традиционной '
            'серьезности, так и от риска полной идентификации с крайними '
            'состояниями чувств.'
        ),
        (
            'Без пяти минут античная трагедия едва сходится с маньеристским '
            'боевиком, в котором полтора часа красивые (и не очень) люди по '
            'инерции мстят друг другу, освещенные неоновыми лампами и '
            'красными светильниками.'
        )]

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
            'This is a visual cue which evokes imagery of the fist fight with '
            'Chang later on in the film, in which Julian in knocked to the '
            'ground with Chang standing behind him, with his fists '
            'raised in the same position as the statue.'
         ),
        (
            'Its the films clashing of east and west which is interesting as '
            'we feel like we are watching a western fused with elements of '
            'samurai films, though the film takes more of its cues from '
            'Sergio Leonne rather than Akira Kurosawa.'
        ),
        (
            'Which makes sense in the context of the scene since '
            'Ryan Goslings character, Julian, is fighting Chang (God).'
        ),
        (
            'Julian has visions through out the film, where the scene will '
            'seamlessly go into what he is imagining or experiencing, with '
            'visual cues to let us know it is a vision (for example his '
            'shirt changes to a different colour in his vision, and then back '
            'to its original colour to let us know we are back in reality).'
        )]
