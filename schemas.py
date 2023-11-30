
from pydantic import BaseModel


class IgnoredType:
    pass


class AssetsCreateInput(BaseModel):
    id: str
    name: str

    
class StandardOutput(BaseModel):
    message: str


class ErrorOutput(BaseModel):
    detail: str


class ListMeasurementsOutput(BaseModel):
    id: int
    timestamp: float
    wind_speed: float
    power: float
    air_temperature: float
    asset_id: int
    
    class Config:
        orm_mode = True


class AssetsListOutput(BaseModel):
    id: int
    name: str
   
    
class AssetsListIdOutput(BaseModel):
    id: int
    name: str
    favorites: list[ListMeasurementsOutput]
    
    class Config:
        orm_mode = True