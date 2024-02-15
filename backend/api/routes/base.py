from fastapi import APIRouter


main_router = APIRouter()

@main_router.get('/')
def get_home_page():
    return {"Hello": "World"}