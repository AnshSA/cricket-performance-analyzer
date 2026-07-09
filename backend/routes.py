from fastapi import APIRouter
from .grounds import get_grounds

router = APIRouter()


@router.get("/grounds")
def grounds_list():

    return {
        "grounds": get_grounds()
    }
