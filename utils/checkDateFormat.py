from datetime import datetime


def checkDateFormat(date):
    try:
        parsed_date = datetime.fromisoformat(date)

        if parsed_date.strftime('%Y-%m-%d') == date:
            return True
        else:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD")

    except ValueError as e:
        return f"Error: {e}"  # Return the error message for invalid format
