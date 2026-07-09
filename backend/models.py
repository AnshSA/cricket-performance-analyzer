from pydantic import BaseModel


class Player(BaseModel):
    name: str
    matches: int
    runs: int
    wickets: int
    strike_rate: float
    economy: float
