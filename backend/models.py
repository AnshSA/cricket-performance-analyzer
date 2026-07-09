from pydantic import BaseModel
from typing import List, Literal


class Player(BaseModel):

    # Basic Information

    name: str
    age: int
    role: str


    # Match Information

    matches: int
    innings: int

    grounds_played: List[
        Literal[
            "Shree Cricket Mandir",
            "Unique Cricket Ground",
            "Mitrea Astro Turf"
        ]
    ]


    # Batting

    batting_position: Literal[
        "Opener",
        "No. 3",
        "Middle Order",
        "Lower Order",
        "Finisher"
    ]

    runs: int
    balls_faced: int

    fours: int
    sixes: int

    dot_balls_faced: int

    singles: int
    doubles: int
    triples: int


    # Pace vs Spin batting

    pace_balls_faced: int
    pace_runs: int

    spin_balls_faced: int
    spin_runs: int


    # Dismissal

    dismissal_type: Literal[
        "Not Out",
        "Bowled",
        "Caught",
        "LBW",
        "Run Out",
        "Stumped",
        "Hit Wicket"
    ]


    # Bowling

    bowling_style: Literal[
        "Fast Bowler",
        "Medium Pace",
        "Off Spinner",
        "Leg Spinner"
    ]


    balls_bowled: int

    pace_balls_bowled: int

    spin_balls_bowled: int


    runs_conceded: int

    wickets: int

    maidens: int


    # Bowling Extras

    wides: int

    no_balls: int

    dot_balls_bowled: int
