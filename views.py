from typing import List
from fastapi import APIRouter, HTTPException

from schemas import AssetsCreateInput, StandardOutput, ErrorOutput, AssetsListOutput, AssetsListIdOutput
from service import AssetService, MeasurementsService

assets_router = APIRouter(prefix='/assets')
measurementservice_router = APIRouter(prefix='/measurementservice')

@assets_router.post('/create', response_model=StandardOutput, responses={400:{'model': ErrorOutput}})
async def assets_create(id, name):
    try:
        await AssetService.create_asset(id=id, name=name)
        return StandardOutput({
            'message': 'Created'
        })
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@assets_router.get('/list-assets', response_model=AssetsListOutput, responses={400: {'model': ErrorOutput}})
async def list_get_assets():
    try:
        return await AssetService.list_asset()
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@assets_router.get('/list-assets-id/{id}', response_model=List[AssetsListIdOutput], responses={400:{'model': ErrorOutput}})
async def list_assets_id(id: int):
    try:
        return await AssetService.get_by_id(id=id)
    except Exception as error:
        raise HTTPException(400, detail=str(error))
    

@measurementservice_router.post('/create', response_model=StandardOutput, responses={400:{'model': ErrorOutput}})
async def measurementservice_create(assets_input: AssetsCreateInput):
    try:
        await MeasurementsService.create_asset(id=assets_input.id, name=assets_input.name)
        return StandardOutput({
            'message': 'Created'
        })
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@measurementservice_router.get('/list-assets', response_model=AssetsListOutput, responses={400: {'model': ErrorOutput}})
async def list_get_measurementservice():
    try:
        return await MeasurementsService.list_asset()
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@measurementservice_router.get('/list-assets-id/{id}', response_model=List[AssetsListIdOutput], responses={400:{'model': ErrorOutput}})
async def list_measurementservice_id(id: int):
    try:
        return await MeasurementsService.get_by_id(id=id)
    except Exception as error:
        raise HTTPException(400, detail=str(error))

        