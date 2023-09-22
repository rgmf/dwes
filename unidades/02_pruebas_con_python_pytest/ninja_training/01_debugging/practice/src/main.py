import json
import base64

from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder


nba_teams = teams.get_teams()

lal = [team for team in nba_teams if team["abbreviation"] == "LAL"][0]

lal_id = lal["id"]
gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=lal_id)
games = json.loads(gamefinder.get_json())["resultSets"][0]["rowSet"]

with open("data.bin", "wb") as fd:
    for game in games:
        game_name, lal_result = game[6], game[7]
        # print(f"Game: {game_name:<20}Los Angeles Lakers: {lal_result}")
        fd.write(base64.b64encode(game_name.encode('utf-8')))
        fd.write(b"\n")
        fd.write(base64.b64encode(lal_result.encode('utf-8')))
        fd.write(b"\n")
