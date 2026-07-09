from pydantic import BaseModel
from typing import Literal


class Delivery(BaseModel):

    # Players

    batsman: str

    bowler: str


    # Bowling Information

    bowling_type: Literal[
        "Pace",
        "Spin"
    ]


    bowling_style: Literal[
        "Fast",
        "Medium Pace",
        "Off Spin",
        "Leg Spin"
    ]


    # Delivery Details

    delivery_length: Literal[
        "Yorker",
        "Good Length",
        "Short Ball",
        "Bouncer",
        "Full Toss"
    ]


    delivery_line: Literal[
        "Off Stump",
        "Middle Stump",
        "Leg Stump",
        "Outside Off",
        "Outside Leg"
    ]


    # Batting Response

    shot_played: Literal[
        "Cover Drive",
        "Straight Drive",
        "Pull Shot",
        "Cut Shot",
        "Sweep",
        "Reverse Sweep",
        "Flick",
        "Defensive",
        "Leave"
    ]


    runs_scored: int


    # Extras

    extras: int


    # Ball Result

    is_dot_ball: bool

    is_boundary: bool


    # Wicket

    wicket: bool


    wicket_type: Literal[
        "None",
        "Bowled",
        "Caught",
        "LBW",
        "Run Out",
        "Stumped",
        "Hit Wicket"
    ]
