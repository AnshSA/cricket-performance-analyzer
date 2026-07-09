from pydantic import BaseModel
from typing import Literal


class Player(BaseModel):

    name: str

    ground_played: Literal[
        "Shree Cricket Mandir",
        "Unique Cricket Ground",
        "Mitrea Astro Turf"
    ]

    matches: int

    runs: int

    balls_faced: int

    # Batting against bowlers

    pace_balls_faced: int

    spin_balls_faced: int


    # Bowling

    balls_bowled: int

    pace_balls_bowled: int

    spin_balls_bowled: int


    wickets: int

    runs_conceded: int
