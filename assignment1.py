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

def count_weekend_days(start_date: str, end_date: str) -> int:
    """
    Counts the number of Saturdays and Sundays between start_date and end_date.
    """
    weekends = 0
    current_date = start_date
    
    while current_date <= end_date:
        year, month, day = map(int, current_date.split('-'))
        weekday = (year * 365 + sum(mon_max(m, year) for m in range(1, month)) + day) % 7
        
        if weekday in [6, 0]:  # Saturday (6) or Sunday (0)
            weekends += 1
        
        current_date = after(current_date)
    
    return weekends

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 assignment1.py YYYY-MM-DD YYYY-MM-DD")
        sys.exit(1)
    
    start_date, end_date = sys.argv[1], sys.argv[2]
    weekend_days = count_weekend_days(start_date, end_date)
    print("The period between {} and {} includes {} weekend days.".format(start_date, end_date, weekend_days))
