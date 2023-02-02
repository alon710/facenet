import requests
from fastapi import APIRouter

router = APIRouter(
    prefix="/faces",
    tags=["faces"],
)


@router.get("/does_contain_faces")
def does_contain_faces(image_url: str) -> requests.Response:
    pass


@router.get("/is_same_person")
def is_same_person(first_image_url: str, second_image_url: str) -> requests.Response:
    pass
