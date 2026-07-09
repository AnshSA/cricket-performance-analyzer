from fastapi import APIRouter

from .database import players, matches, deliveries

router = APIRouter()


@router.get("/players")
def get_players():
    return {
        "players": players
    }


@router.get("/matches")
def get_matches():
    return {
        "matches": matches
    }


@router.get("/deliveries")
def get_deliveries():
    return {
        "deliveries": deliveries
    }
