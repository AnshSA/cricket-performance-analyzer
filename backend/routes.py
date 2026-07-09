
from .database import players
from .models import Player


router = APIRouter()



@router.post("/players")
def add_player(player: Player):

    players.append(player)

    return {

        "message": "Player performance saved",

        "player": player

    }



@router.get("/players")
def get_players():

    return players
