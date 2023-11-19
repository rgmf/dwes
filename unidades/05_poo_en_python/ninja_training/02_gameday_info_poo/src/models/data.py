from random import randint


GAMEDAYS: list[dict[str, any]] = [
    {
        "gameday": 1,
        "played": True,
        "games": [
            {"team1": "Atlético de Madrid", "team2": "Osasuna"},
            {"team1": "Villarreal", "team2": "Valencia"},
            {"team1": "Athlétic de Bilbao", "team2": "FC Barcelona"},
            {"team1": "Real Madrid", "team2": "Sevilla FC"},
            {"team1": "Real Sociedad", "team2": "Celta de Vigo"}
        ]
    },
    {
        "gameday": 2,
        "played": True,
        "games": [
            {"team1": "Osasuna", "team2": "Villarreal"},
            {"team1": "Valencia", "team2": "Athlétic de Bilbao"},
            {"team1": "FC Barcelona", "team2": "Real Madrid"},
            {"team1": "Sevilla FC", "team2": "Real Sociedad"},
            {"team1": "Celta de Vigo", "team2": "Atlético de Madrid"}
        ]
    },
    {
        "gameday": 3,
        "played": True,
        "games": [
            {"team1": "Atlético de Madrid", "team2": "Villarreal"},
            {"team1": "Osasuna", "team2": "Valencia"},
            {"team1": "Athlétic de Bilbao", "team2": "Sevilla FC"},
            {"team1": "Real Madrid", "team2": "Celta de Vigo"},
            {"team1": "FC Barcelona", "team2": "Real Sociedad"}
        ]
    },
    {
        "gameday": 4,
        "played": True,
        "games": [
            {"team1": "Villarreal", "team2": "FC Barcelona"},
            {"team1": "Valencia", "team2": "Sevilla FC"},
            {"team1": "Athlétic de Bilbao", "team2": "Celta de Vigo"},
            {"team1": "Real Madrid", "team2": "Real Sociedad"},
            {"team1": "Osasuna", "team2": "Atlético de Madrid"}
        ]
    },
    {
        "gameday": 5,
        "played": False,
        "games": [
            {"team1": "Atlético de Madrid", "team2": "Valencia"},
            {"team1": "Villarreal", "team2": "Sevilla FC"},
            {"team1": "Osasuna", "team2": "Celta de Vigo"},
            {"team1": "FC Barcelona", "team2": "Real Sociedad"},
            {"team1": "Athlétic de Bilbao", "team2": "Real Madrid"}
        ]
    },
    {
        "gameday": 6,
        "played": False,
        "games": [
            {"team1": "Valencia", "team2": "Real Madrid"},
            {"team1": "Sevilla FC", "team2": "Celta de Vigo"},
            {"team1": "Villarreal", "team2": "Real Sociedad"},
            {"team1": "FC Barcelona", "team2": "Atlético de Madrid"},
            {"team1": "Osasuna", "team2": "Athlétic de Bilbao"}
        ]
    },
    {
        "gameday": 7,
        "played": False,
        "games": [
            {"team1": "Atlético de Madrid", "team2": "Valencia"},
            {"team1": "Villarreal", "team2": "Real Madrid"},
            {"team1": "Osasuna", "team2": "Celta de Vigo"},
            {"team1": "FC Barcelona", "team2": "Sevilla FC"},
            {"team1": "Athlétic de Bilbao", "team2": "Real Sociedad"}
        ]
    },
    {
        "gameday": 8,
        "played": False,
        "games": [
            {"team1": "Valencia", "team2": "Sevilla FC"},
            {"team1": "Real Madrid", "team2": "Celta de Vigo"},
            {"team1": "Villarreal", "team2": "Atlético de Madrid"},
            {"team1": "FC Barcelona", "team2": "Real Sociedad"},
            {"team1": "Osasuna", "team2": "Athlétic de Bilbao"}
        ]
    },
    {
        "gameday": 9,
        "played": False,
        "games": [
            {"team1": "Atlético de Madrid", "team2": "Real Sociedad"},
            {"team1": "Villarreal", "team2": "Celta de Vigo"},
            {"team1": "Osasuna", "team2": "Real Madrid"},
            {"team1": "FC Barcelona", "team2": "Athlétic de Bilbao"},
            {"team1": "Valencia", "team2": "Sevilla FC"}
        ]
    },
    {
        "gameday": 10,
        "played": False,
        "games": [
            {"team1": "Osasuna", "team2": "Atletico de Madrid"},
            {"team1": "Valencia", "team2": "Villarreal"},
            {"team1": "FC Barcelona", "team2": "Athletic de Bilbao"},
            {"team1": "Sevilla FC", "team2": "Real Madrid"},
            {"team1": "Celta de Vigo", "team2": "Real Sociedad"}
        ]
    },
    {
        "gameday": 11,
        "played": False,
        "games": [
            {"team1": "Villarreal", "team2": "Atletico de Madrid"},
            {"team1": "Athletic de Bilbao", "team2": "Osasuna"},
            {"team1": "Real Madrid", "team2": "FC Barcelona"},
            {"team1": "Real Sociedad", "team2": "Sevilla FC"},
            {"team1": "Atletico de Madrid", "team2": "Celta de Vigo"}
        ]
    },
    {
        "gameday": 12,
        "played": False,
        "games": [
            {"team1": "Villarreal", "team2": "Atletico de Madrid"},
            {"team1": "Valencia", "team2": "Osasuna"},
            {"team1": "Sevilla FC", "team2": "Athletic de Bilbao"},
            {"team1": "Celta de Vigo", "team2": "Real Madrid"},
            {"team1": "Real Sociedad", "team2": "FC Barcelona"}
        ]
    },
    {
        "gameday": 13,
        "played": False,
        "games": [
            {"team1": "FC Barcelona", "team2": "Villarreal"},
            {"team1": "Sevilla FC", "team2": "Valencia"},
            {"team1": "Celta de Vigo", "team2": "Athletic de Bilbao"},
            {"team1": "Real Sociedad", "team2": "Real Madrid"},
            {"team1": "Atletico de Madrid", "team2": "Osasuna"}
        ]
    },
    {
        "gameday": 14,
        "played": False,
        "games": [
            {"team1": "Valencia", "team2": "Atletico de Madrid"},
            {"team1": "Sevilla FC", "team2": "Villarreal"},
            {"team1": "Celta de Vigo", "team2": "Osasuna"},
            {"team1": "Real Sociedad", "team2": "FC Barcelona"},
            {"team1": "Real Madrid", "team2": "Athletic de Bilbao"}
        ]
    },
    {
        "gameday": 15,
        "played": False,
        "games": [
            {"team1": "Real Madrid", "team2": "Valencia"},
            {"team1": "Celta de Vigo", "team2": "Sevilla FC"},
            {"team1": "Real Sociedad", "team2": "Villarreal"},
            {"team1": "Atletico de Madrid", "team2": "FC Barcelona"},
            {"team1": "Athletic de Bilbao", "team2": "Osasuna"}
        ]
    },
    {
        "gameday": 16,
        "played": False,
        "games": [
            {"team1": "Valencia", "team2": "Atletico de Madrid"},
            {"team1": "Real Madrid", "team2": "Villarreal"},
            {"team1": "Celta de Vigo", "team2": "Osasuna"},
            {"team1": "FC Barcelona", "team2": "Sevilla FC"},
            {"team1": "Athletic de Bilbao", "team2": "Real Sociedad"}
        ]
    },
    {
        "gameday": 17,
        "played": False,
        "games": [
            {"team1": "Sevilla FC", "team2": "Valencia"},
            {"team1": "Celta de Vigo", "team2": "Real Madrid"},
            {"team1": "Atletico de Madrid", "team2": "Villarreal"},
            {"team1": "FC Barcelona", "team2": "Real Sociedad"},
            {"team1": "Osasuna", "team2": "Athletic de Bilbao"}
        ]
    },
    {
        "gameday": 18,
        "played": False,
        "games": [
            {"team1": "Real Sociedad", "team2": "Atletico de Madrid"},
            {"team1": "Celta de Vigo", "team2": "Villarreal"},
            {"team1": "Real Madrid", "team2": "Osasuna"},
            {"team1": "Athletic de Bilbao", "team2": "FC Barcelona"},
            {"team1": "Sevilla FC", "team2": "Valencia"}
        ]
    }
]


SCOREBOARDS = [
    {
        "gameday": i + 1,
        "scoreboard": [
            (randint(0, 3), randint(0, 3)),
            (randint(0, 3), randint(0, 3)),
            (randint(0, 3), randint(0, 3)),
            (randint(0, 3), randint(0, 3)),
            (randint(0, 3), randint(0, 3))
        ]
    }
    for i in range(len(GAMEDAYS))
]
