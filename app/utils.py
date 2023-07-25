from .models import RestaurantOpeningHours

from config import settings

class OpeningHoursFormatter:
    @staticmethod
    def format_opening_hours(opening_hours: RestaurantOpeningHours) -> str:
        """
        Форматирует часы работы ресторана.

        Args:
            opening_hours (RestaurantOpeningHours): Часы работы ресторана.

        Returns:
            str: Отформатированные часы работы ресторана.
        """
        formatted_hours = []
        for day in settings.DAYS:
            hours = getattr(opening_hours, day)
            if hours:
                day_hours = OpeningHoursFormatter.format_day_hours(day, hours, opening_hours)
                formatted_hours.append(f"{day.capitalize()}: {day_hours}")
            else:
                formatted_hours.append(f"{day.capitalize()}: Closed")

        return "\n".join(formatted_hours)

    @staticmethod
    def format_day_hours(day, hours, opening_hours: RestaurantOpeningHours) -> str:
        """
        Форматирует часы работы для одного дня.

        Args:
            hours (List[OpeningHours]): Часы работы для одного дня.

        Returns:
            str: Отформатированные часы работы для одного дня.
        """
        formatted_hours = []
        current_opening_time = None
        for hour in hours:
            if hour.type == "open":
                current_opening_time = hour.value
            elif hour.type == "close" and current_opening_time is not None:
                formatted_hours.append(f"{OpeningHoursFormatter.format_time_range(current_opening_time)} - {OpeningHoursFormatter.format_time_range(hour.value)}")
                current_opening_time = None

        if current_opening_time is not None: 
            hours = opening_hours.get_next_day(day)
            if hours[0].type == "close":
                formatted_hours.append(f"{OpeningHoursFormatter.format_time_range(current_opening_time)} - {OpeningHoursFormatter.format_time_range(hours[0].value)}")

        return ", ".join(formatted_hours)

    @staticmethod
    def format_time_range(value) -> str:
        """
        Форматирует временной диапазон.

        Args:
            value (int): Временное значение в формате UNIX.

        Returns:
            str: Отформатированный временной диапазон.
        """
        hours = int(value / 3600)
        minutes = int((value % 3600) / 60)
        if hours >= 12:
            am_pm = "PM"
            hours -= 12
        else:
            am_pm = "AM"
        return f"{hours}:{str(minutes).zfill(2)} {am_pm}"