from database.connection import async_session
from sqlalchemy.ext.asyncio.session import async_session
from sqlalchemy.future import select
from database.models import Asset, Measurements

class AssetService:
    async def create_asset(id, name):
        async with async_session() as session:
            session.add(Asset(id, name))
            await session.commit()
    
    async def list_asset():
        async with async_session() as session:
            result = await session.execute(select(Asset))
            return result.scalars().all()
        
    
    async def get_by_id(id):
        async with async_session() as session:
            result = await session.execute(select(Asset).where(Asset.id==id))
            return result.scalar().first()
            
            
            
class MeasurementsService:
    async def create_measurements(id, **dados ):
        async with async_session() as session:
            session.add(Measurements(id, **dados))
            await session.commit()
    
    async def list_measurements():
        async with async_session() as session:
            result = await session.execute(select(Measurements))
            return result.scalars().all()
        
    
    async def get_measurements_id(asset_id):
        async with async_session() as session:
            result = await session.execute(select(Measurements).where(Measurements.asset_id==asset_id))
            return result.scalar()