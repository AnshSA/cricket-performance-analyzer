from pydantic import BaseModel
from typing import Literal


class Match(BaseModel):

    # Match Details

    opponent: str

    format: Literal[
        "T20",
        "ODI",
        "Test"
    ]


    ground: Literal[
        "Shree Cricket Mandir",
        "Unique Cricket Ground",
        "Mitrea Astro Turf"
    ]


    # Conditions

    pitch_type: Literal[
        "Batting Friendly",
        "Bowling Friendly",
        "Spin Friendly",
        "Seam Friendly",
        "Balanced"
    ]


    weather: Literal[
        "Sunny",
        "Cloudy",
        "Humid",
        "Rain"
    ]


    # Batting Match Data

    runs_scored: int

    balls_faced: int


    # Powerplay (Overs 1-6)

    powerplay_runs: int

    powerplay_balls: int


    # Middle Overs (7-15)

    middle_order_runs: int

    middle_order_balls: int


    # Death Overs (16-20)

    death_runs: int

    death_balls: int


    # Bowling Match Data

    balls_bowled: int

    runs_conceded: int

    wickets_taken: int
