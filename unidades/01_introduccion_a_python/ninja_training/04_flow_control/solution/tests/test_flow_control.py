from ..flow_control import (
    random_nums, addition_large_nums, addition, avg_grades, info_best_student,
    rick_and_morty_names, female_characteres, simple_ram
)


def test_flow_control():
    assert len(random_nums) == 10
    assert addition_large_nums == sum(sorted(random_nums)[:2])
    assert addition == sum(random_nums)
    assert avg_grades == (6.75 + 7.25 + 8.5 + 3.75) / 4
    assert info_best_student == "Mary ha obtenido la nota más alta: 8.5."
    assert rick_and_morty_names == [
        "Rick Sanchez", "Morty Smith", "Summer Smith",
        "Beth Smith", "Abadango Cluster Princess"
    ]
    assert female_characteres == [
        "Summer Smith", "Beth Smith", "Abadango Cluster Princess"
    ]
    assert simple_ram == [
        {
            "name": "Rick Sanchez",
            "species": "Human",
            "gender": "Male"
        },
        {
            "name": "Morty Smith",
            "species": "Human",
            "gender": "Male"
        },
        {
            "name": "Summer Smith",
            "species": "Human",
            "gender": "Female"
        },
        {
            "name": "Beth Smith",
            "species": "Human",
            "gender": "Female"
        },
        {
            "name": "Abadango Cluster Princess",
            "species": "Alien",
            "gender": "Female",
        }
    ]
