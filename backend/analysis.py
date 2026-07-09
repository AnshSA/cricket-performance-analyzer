def batting_average(runs, innings):
    if innings == 0:
        return 0
    return round(runs / innings, 2)


def strike_rate(runs, balls):
    if balls == 0:
        return 0
    return round((runs / balls) * 100, 2)


def bowling_average(runs_given, wickets):
    if wickets == 0:
        return 0
    return round(runs_given / wickets, 2)


def economy_rate(runs_given, overs):
    if overs == 0:
        return 0
    return round(runs_given / overs, 2)
