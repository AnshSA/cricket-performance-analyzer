from pydantic import BaseModel


class Delivery(BaseModel):

    batsman: str

    bowler: str

    bowling_type: str
    # pace or spin

    runs_scored: int

    balls_faced: int

    wicket: bool

    extras: int

    is_boundary: bool

    is_dot_ball: bool
