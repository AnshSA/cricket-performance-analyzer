def batting_average(runs, dismissals):

    if dismissals == 0:
        return runs

    return round(runs / dismissals, 2)



def strike_rate(runs, balls):

    if balls == 0:
        return 0

    return round((runs / balls) * 100, 2)



def economy_rate(runs_conceded, balls_bowled):

    if balls_bowled == 0:
        return 0

    overs = balls_bowled / 6

    return round(runs_conceded / overs, 2)



def bowling_average(runs_conceded, wickets):

    if wickets == 0:
        return 0

    return round(runs_conceded / wickets, 2)



def dot_ball_percentage(dot_balls, total_balls):

    if total_balls == 0:
        return 0

    return round((dot_balls / total_balls) * 100, 2)



def pace_performance(runs, balls):

    if balls == 0:
        return 0

    return {
        "runs": runs,
        "balls": balls,
        "strike_rate": round((runs / balls) * 100, 2)
    }



def spin_performance(runs, balls):

    if balls == 0:
        return 0

    return {
        "runs": runs,
        "balls": balls,
        "strike_rate": round((runs / balls) * 100, 2)
    }



def ground_performance(matches, runs):

    if matches == 0:
        return 0

    return round(runs / matches, 2)



def phase_performance(runs, balls):

    if balls == 0:
        return 0

    return {
        "runs": runs,
        "balls": balls,
        "strike_rate": round((runs / balls) * 100, 2)
    }



def player_summary(player):

    return {

        "player": player.name,

        "batting": {

            "runs": player.runs,

            "strike_rate":
                strike_rate(
                    player.runs,
                    player.balls_faced
                ),

            "pace_analysis":
                pace_performance(
                    player.pace_runs,
                    player.pace_balls_faced
                ),

            "spin_analysis":
                spin_performance(
                    player.spin_runs,
                    player.spin_balls_faced
                )
        },


        "bowling": {

            "economy":
                economy_rate(
                    player.runs_conceded,
                    player.balls_bowled
                ),

            "wickets":
                player.wickets
        }
    }
