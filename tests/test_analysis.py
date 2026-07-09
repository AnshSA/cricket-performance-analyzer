from backend.analysis import (
    batting_average,
    strike_rate,
    bowling_average,
    economy_rate
)


def test_batting_average():
    assert batting_average(240, 6) == 40


def test_strike_rate():
    assert strike_rate(50, 25) == 200


def test_bowling_average():
    assert bowling_average(150, 5) == 30


def test_economy_rate():
    assert economy_rate(36, 6) == 6
