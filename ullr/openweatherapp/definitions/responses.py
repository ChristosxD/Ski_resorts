from pydantic import BaseModel
from typing import List
from datetime import time


class OWAAlertDef(BaseModel):
    sender_name: str
    event: str
    start: time
    end: time
    description: str
    tags: List[str]


class OWAWeatherDetailsDef(BaseModel):
    id: int
    main: str
    description: str
    icon: str


class OWATempDef(BaseModel):
    morn: float
    day: float
    eve: float
    night: float
    min: float
    max: float


class OWAFeelsLikeDef(BaseModel):
    morn: float
    day: float
    eve: float
    night: float


class OWAWeatherDef(BaseModel):
    dt: time
    sunrise: time
    sunset: time
    temp: OWATempDef
    feels_like: OWAFeelsLikeDef
    pressure: int
    humidity: int
    dew_point: float
    clouds: int
    uvi: float
    visibility: int
    wind_speed: int
    wind_gust: float
    wind_deg: float
    rain: float
    snow: float
    moonrise: time
    moonset: time
    weather: List[OWAWeatherDetailsDef]


class OWACurrentWeatherDef(BaseModel):
    dt: time
    sunrise: time
    sunset: time
    temp: float
    feels_like: float
    pressure: int
    humidity: int
    dew_point: float
    clouds: int
    uvi: float
    visibility: int
    wind_speed: int
    wind_gust: float
    wind_deg: float
    rain: float
    snow: float
    weather: List[OWAWeatherDetailsDef]


class OWAResponseDef(BaseModel):

    lat: float
    lon: float
    timezone: str
    timezone_offset: int
    current: OWACurrentWeatherDef
    hourly: List[OWAWeatherDef]
    daily: List[OWAWeatherDef]
    alerts: List[OWAAlertDef]
