from fastapi import FastAPI

from .models import RestaurantOpeningHours
from .utils import OpeningHoursFormatter

app = FastAPI()

@app.post("/opening-hours")
def opening_hours_endpoint(opening_hours: RestaurantOpeningHours) -> str:
    """
    Конечная точка для форматирования часов работы ресторана.

    Args:
        opening_hours (RestaurantOpeningHours): Часы работы ресторана.

    Returns:
        str: Отформатированные часы работы ресторана.
    """

    return OpeningHoursFormatter().format_opening_hours(opening_hours)
