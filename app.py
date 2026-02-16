from nba_api.stats.static import teams
from nba_api.stats.endpoints import LeagueGameFinder
from nba_api.stats.endpoints import BoxScoreTraditionalV3


def one():
    gamefinder = LeagueGameFinder(team_id_nullable=1610612751)
    games = gamefinder.get_data_frames()[0]
    latest_game_id = games.iloc[0]["GAME_ID"]
    print(latest_game_id)
    print(games.head()) 
  

def two():
    nba_teams = teams.get_teams()

    nets = [t for t in nba_teams if t["full_name"] == "Brooklyn Nets"][0]
    print(nets)

def three():
    gamefinder = LeagueGameFinder(team_id_nullable=1610612751)
    games = gamefinder.get_data_frames()[0]

    latest_game_id = games.iloc[0]["GAME_ID"]
    print(latest_game_id)

    boxscore = BoxScoreTraditionalV3(game_id=latest_game_id)
    player_stats = boxscore.player_stats.get_data_frame()

    nets_stats = player_stats[player_stats["teamId"] == 1610612751]

    nets_stats["player"] = (
        nets_stats["firstName"] + " " + nets_stats["familyName"]
    )

    print(
        nets_stats[
            ["player", "points", "reboundsTotal", "assists"]
        ]
    )


three()