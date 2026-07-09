from pydantic import BaseModel


class Match(BaseModel):

    opponent: str

    ground: str

    format: str
    # T20, ODI, Test


    runs_scored: int

    balls_faced: int


    wickets_taken: int

    balls_bowled: int


    pace_balls_faced: int

    spin_balls_faced: int


    pace_balls_bowled: int

    spin_balls_bowled: int
