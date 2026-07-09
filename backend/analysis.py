def batting_average(runs, innings):

    if innings == 0:
        return 0

    return round(runs / innings,2)


def strike_rate(runs, balls):

    if balls == 0:
        return 0

    return round((runs/balls)*100,2)


def pace_strike_rate(runs, balls):

    if balls == 0:
        return 0

    return round((runs/balls)*100,2)


def spin_strike_rate(runs, balls):

    if balls == 0:
        return 0

    return round((runs/balls)*100,2)


def bowling_average(runs, wickets):

    if wickets == 0:
        return 0

    return round(runs/wickets,2)


def economy(runs, overs):

    if overs == 0:
        return 0

    return round(runs/overs,2)


def dot_ball_percentage(dot_balls, balls):

    if balls == 0:
        return 0

    return round((dot_balls/balls)*100,2)
