from nba_api.stats.static import teams
from nba_api.stats.endpoints import LeagueGameFinder
from nba_api.stats.endpoints import BoxScoreTraditionalV3


# Brooklyn Nets
def SideOne():
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


# Cleveland Cavs 
def SideTwo():
    gamefinder = LeagueGameFinder(team_id_nullable=1610612739)
    games = gamefinder.get_data_frames()[0]

    latest_game_id = games.iloc[0]["GAME_ID"]

    boxscore = BoxScoreTraditionalV3(game_id=latest_game_id)
    player_stats = boxscore.player_stats.get_data_frame()

    cavs_stats = player_stats[player_stats["teamId"] == 1610612739]
    cavs_stats["player"] = (  # Changed from "Player" to "player"
        cavs_stats["firstName"] + " " + cavs_stats["familyName"]
    )

    print(
        cavs_stats[
            ["player", "points", "reboundsTotal", "assists"]  # Fixed "rebountTotal" typo
        ]
    )


def HeadToHead():
    print("--------------HEADTOHEAD------------")
    print("teamOne:")
    SideOne()
    print("\nteamTwo:")
    SideTwo()


HeadToHead()  
