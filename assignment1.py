import sys

def leap_year(year: int) -> bool:
    """
    Determines if a given year is a leap year.
    Returns True if it is a leap year, otherwise False.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def mon_max(month: int, year: int) -> int:
    """
    Returns the maximum number of days for a given month in a given year.
    Handles leap years for February.
    """
    feb_max = 29 if leap_year(year) else 28
    days_in_month = {1: 31, 2: feb_max, 3: 31, 4: 30, 5: 31, 6: 30, 
                     7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    return days_in_month[month]

def after(date: str) -> str:
    """
    Returns the next day's date in YYYY-MM-DD format.
    """
    year, month, day = map(int, date.split('-'))
    days_in_month = mon_max(month, year)
    day += 1
    
    if day > days_in_month:
        day = 1
        month += 1
    
    if month > 12:
        month = 1
        year += 1
    
    return "{}-{:02}-{:02}".format(year, month, day)

def day_of_week(date: str) -> int:
    """
    Returns the day of the week for a given date.
    0 = Sunday, 1 = Monday, ..., 6 = Saturday
    """
    year, month, day = map(int, date.split('-'))
    offset = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if month < 3:
        year -= 1
    return (year + year // 4 - year // 100 + year // 400 + offset[month - 1] + day) % 7

def day_count(start_date: str, end_date: str) -> int:
    """
    Counts the number of Saturdays and Sundays between start_date and end_date.
    """
    weekends = 0
    current_date = start_date
    
    while current_date <= end_date:
        if day_of_week(current_date) in [0, 6]:  # Sunday (0) or Saturday (6)
            weekends += 1
        current_date = after(current_date)
    
    return weekends

def valid_date(date: str) -> bool:
    """
    Checks if the given date is valid (YYYY-MM-DD format and actual date exists).
    """
    parts = date.split('-')
    if len(parts) != 3:
        return False
    year_str, month_str, day_str = parts
    if len(year_str) != 4 or len(month_str) != 2 or len(day_str) != 2:
        return False
    try:
        year = int(year_str)
        month = int(month_str)
        day = int(day_str)
    except ValueError:
        return False
    if month < 1 or month > 12:
        return False
    if day < 1 or day > mon_max(month, year):
        return False
    return True

def is_earlier(start_date: str, end_date: str) -> bool:
    """
    Checks if the start_date is earlier than or equal to the end_date.
    """
    return start_date <= end_date

def usage():
    """
    Prints a usage message and exits the program.
    """
    print("Usage: python3 assignment1.py YYYY-MM-DD YYYY-MM-DD")
    print("Both dates must be valid and in YYYY-MM-DD format.")
    sys.exit(1)

if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) != 3:
        usage()
    
    start_date, end_date = sys.argv[1], sys.argv[2]
    
    # Validate the dates
    if not valid_date(start_date) or not valid_date(end_date):
        usage()
    
    # Ensure the start date is earlier than the end date
    if not is_earlier(start_date, end_date):
        start_date, end_date = end_date, start_date  # Swap dates if necessary
    
    # Calculate and print the number of weekend days
    weekend_days = day_count(start_date, end_date)
    print("The period between {} and {} includes {} weekend days.".format(start_date, end_date, weekend_days))
