from fastapi import APIRouter

router = APIRouter(
    prefix = '/api',
    tags = ['api'],
    responses = {404: {'description': 'Not found'}},
)
