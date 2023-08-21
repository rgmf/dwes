from ..tuples import (
    forth_vowel, all_vowels, too_true, has_false, Location, locations, altitude
)


def test_tuple():
    assert forth_vowel == "o"
    assert all_vowels == ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    assert len([v for v in too_true if v]) == 100
    assert not has_false
    assert len([loc for loc in locations if isinstance(loc, Location)]) == 4
    assert altitude == locations[2].altitude
