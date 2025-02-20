from datetime import datetime


def checkDateFormat(date):
    try:
        parsed_date = datetime.fromisoformat(date)

        if parsed_date.strftime('%Y-%m-%d') == date:
            return True
        else:
            return "Invalid date format. Please use YYYY-MM-DD"

    except ValueError:
        return "Error: Invalid date format. Please use YYYY-MM-DD"
