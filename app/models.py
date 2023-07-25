from typing import List
from pydantic import BaseModel, Field

from config import settings

class OpeningHours(BaseModel):
    type: str = Field(..., description="Тип (open/close) часов работы")
    value: int = Field(..., description="Значение времени в формате UNIX")


class RestaurantOpeningHours(BaseModel):
    monday: List[OpeningHours] = []
    tuesday: List[OpeningHours] = []
    wednesday: List[OpeningHours] = []
    thursday: List[OpeningHours] = []
    friday: List[OpeningHours] = []
    saturday: List[OpeningHours] = []
    sunday: List[OpeningHours] = []

    def get_next_day(self, current_day: str) -> List[OpeningHours]:
        current_index = settings.DAYS.index(current_day.lower())
        next_index = (current_index + 1) % len(settings.DAYS)
        next_day = settings.DAYS[next_index]
        return getattr(self, next_day)
