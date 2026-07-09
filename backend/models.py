from pydantic import BaseModel

class Player(BaseModel):

    # Basic Information

    name: str
    age: int
    role: str

    # Batting

    matches: int
    innings: int
    runs: int
    balls_faced: int
    fours: int
    sixes: int
    highest_score: int

    # Against Pace

    pace_balls: int
    pace_runs: int
    pace_fours: int
    pace_sixes: int

    # Against Spin

    spin_balls: int
    spin_runs: int
    spin_fours: int
    spin_sixes: int

    # Bowling

    overs: float
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
