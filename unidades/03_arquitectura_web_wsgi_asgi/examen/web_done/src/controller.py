from urllib.parse import parse_qs

from src.templates import render_template
from src.models.data import GAMEDAYS, SCOREBOARDS
from src.models.random_bet import random_bet, is_valid_bet, is_a_correct_pick


def home() -> str:
    return render_template(
        "src/views/index.html",
        {
            "nav": render_template("src/views/parts/nav.html")
        }
    )


def error404() -> str:
    return render_template(
        "src/views/404.html",
        {
            "nav": render_template("src/views/parts/nav.html")
        }
    )


def about() -> str:
    return render_template(
        "src/views/about.html",
        {
            "nav": render_template("src/views/parts/nav.html")
        }
    )


def teams_list(teams: list[str]) -> str:
    context: dict[str, str] = {
        "nav": render_template("src/views/parts/nav.html"),
        "teams": ""
    }

    for team_name in teams:
        context["teams"] += render_template(
            "src/views/parts/team_li_with_link.html",
            {"team": team_name}
        )

    return render_template("src/views/teams.html", context)


def team_games(team: str) -> str:
    return f"Sin hacer: se buscan los partidos del equipo {team}"


def teams(environ: dict) -> str:
    query_strings: dict[str, list[str]] = parse_qs(environ["QUERY_STRING"])
    teams: list[str] = []

    for game in GAMEDAYS[0]["games"]:
        teams.append(game["team1"])
        teams.append(game["team2"])

    if "name" in query_strings and query_strings["name"][0] in teams:
        return team_games(query_strings["name"][0])
    else:
        return teams_list(teams)


def gamedays_list() -> str:
    gamedays: list[int] = [gameday["gameday"] for gameday in GAMEDAYS]
    html_list: str = "<ul>"

    for gd in gamedays:
        link_html: str = render_template(
            "src/views/parts/gameday_link.html",
            {"gameday_number": str(gd)}
        )
        html_list += f"<li>{link_html}</li>"

    html_list += "</ul>"

    context: dict[str, str] = {
        "nav": render_template("src/views/parts/nav.html"),
        "gamedays_list": html_list
    }
    return render_template("src/views/gamedays.html", context)


def gamedays_info(gameday_number: int) -> str:
    gameday: list[dict[str, str]] = GAMEDAYS[gameday_number - 1]["games"]
    context: dict[str, str] = {"nav": render_template("src/views/parts/nav.html")}

    for i, game in enumerate(gameday):
        key: str = f"game{i + 1}"
        context[key] = (
            "<td>" + game["team1"] + "</td>" +
            "<td>" + game["team2"] + "</td>"
        )

    context["gameday_number"] = GAMEDAYS[gameday_number - 1]["gameday"]

    return render_template("src/views/gameday_info.html", context)


def gamedays(environ: dict) -> str:
    query_strings: dict[str, list[str]] = parse_qs(environ["QUERY_STRING"])

    if "n" in query_strings and query_strings["n"][0].isdecimal():
        return gamedays_info(int(query_strings["n"][0]))
    else:
        return gamedays_list()


def random_bet_list(environ: dict) -> str:
    gamedays_not_played: list[dict[str, any]] = [
        gameday for gameday in GAMEDAYS if not gameday["played"]
    ]
    if not gamedays_not_played:
        return render_template(
            "src/views/no_gamedays_left.html",
            {
                "nav": render_template("src/views/parts/nav.html"),
            }
        )

    last_gameday: list[dict[str, str]] = gamedays_not_played[0]
    bets: list[str] = []
    context: dict[str, str] = {
        "nav": render_template("src/views/parts/nav.html")
    }

    for i, game in enumerate(last_gameday["games"]):
        bet: str = random_bet()
        bets.append(bet)
        key: str = f"game{i + 1}"
        context[key] = (
            "<td>" + game["team1"] + "</td>" +
            "<td>" + game["team2"] + "</td>" +
            "<td>" + bet + "</td>"
        )

    context["gameday_number"] = GAMEDAYS[-1]["gameday"]

    context["query_param"] = (
        f"gameday={last_gameday['gameday']}&{'&'.join(['bets=' + bet for bet in bets])}"
    )

    return render_template("src/views/randombetlist.html", context)


def random_bet_list_checking(environ: dict) -> str:
    qs: dict[str, list[str]] = parse_qs(environ["QUERY_STRING"])

    if "gameday" not in qs or not qs["gameday"][0].isdecimal():
        return error404()

    gameday: int = int(qs["gameday"][0])
    if not 1 <= gameday <= len(SCOREBOARDS):
        return error404()

    if "bets" not in qs:
        return error404()

    scoreboards: list[tuple[int, int]] = SCOREBOARDS[gameday - 1]
    bets: list[str] = [bet for bet in qs["bets"] if is_valid_bet(bet)]
    if len(scoreboards["scoreboard"]) != len(bets):
        return error404()

    picks_games: list[bool] = [
        is_a_correct_pick(bet, scoreboards["scoreboard"][i])
        for i, bet in enumerate(bets)
    ]

    context: dict[str, str] = {
        "nav": render_template("src/views/parts/nav.html"),
        "gameday_number": GAMEDAYS[gameday - 1]["gameday"]
    }
    for i, game in enumerate(GAMEDAYS[gameday - 1]["games"]):
        bet: str = bets[i]
        key: str = f"game{i + 1}"
        context[key] = (
            f"<td>{game['team1']}</td>" +
            f"<td>{game['team2']}</td>" +
            f"<td>{bet}</td>" +

            f"<td>{scoreboards['scoreboard'][i][0]} - " +
            f"{scoreboards['scoreboard'][i][1]}</td>" +

            f"<td>{'SÍ' if picks_games[i] else 'NO'}</td>"
        )

    return render_template("src/views/randombetlist_checking.html", context)
