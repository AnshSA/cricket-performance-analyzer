from pydantic import BaseModel
from typing import List


class Player(BaseModel):

    # Player Information

    name: str
    age: int
    role: str


    # Match Information

    matches: int
    innings: int
    grounds_played: List[str]


    # Batting Statistics

    runs: int
    balls_faced: int
    fours: int
    sixes: int
    highest_score: int


    # Batting Against Pace

    pace_balls_faced: int
    pace_runs: int
    pace_fours: int
    pace_sixes: int


    # Batting Against Spin

    spin_balls_faced: int
    spin_runs: int
    spin_fours: int
    spin_sixes: int


    # Bowling Statistics

    balls_bowled: int
    runs_conceded: int
    wickets: int
    maidens: int


    # Bowling Type

    pace_balls_bowled: int
    spin_balls_bowled: int


    # Bowling Extras

    wides: int
    no_balls: int
    dot_balls: int


    # Fielding

    catches: int
    run_outs: int
    stumpings: int
