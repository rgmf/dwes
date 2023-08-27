from ..pig_latin import pig_latin


def test_empty_sentence():
    assert pig_latin("") == ""


def test_sentence_with_one_character_word_vowel():
    assert pig_latin("a") == "away"


def test_sentence_with_one_character_word_consonant():
    assert pig_latin("b") == "bay"


def test_sentence_with_a_word_begin_vowel():
    assert pig_latin("eat") == "eatway"
    assert pig_latin("ate") == "ateway"
    assert pig_latin("user") == "userway"


def test_sentence_with_a_word_begin_consonant():
    assert pig_latin("tea") == "eatay"
    assert pig_latin("split") == "itsplay"
    assert pig_latin("write") == "itewray"


def test_sentence_with_upper_case_word():
    assert pig_latin("Eat") == "Eatway"
    assert pig_latin("Tea") == "Eatay"


def test_sentence():
    assert pig_latin("an easy sentence") == "anway easyway entencesay"
    assert pig_latin("I am DWES student") == "Iway amway Esdway udentstay"
    assert pig_latin("All Word Are Capitalized") == "Allway Ordway Areway Apitalizedcay"
