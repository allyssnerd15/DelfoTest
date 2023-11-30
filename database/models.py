from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Asset(Base):
    __tablename__ = 'asset'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    favorites = relationship('Measurements', backref='asset', lazy='subquery')


class Measurements(Base):
    __tablename__ = 'measurements'
    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(String)
    wind_speed = Column(String)
    power = Column(String)
    air_temperature = Column(String)
    asset_id = Column(Integer, ForeignKey('asset.id'))