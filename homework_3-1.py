from datetime import datetime, timedelta

def get_days_from_today(date) -> int:

    # converting date type from string to datetime using strptime method
    # checking if data was typed in correct format:
    
    try:
        converted_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        print("Wrong date type. Should be written in a YYYY-MM-DD format. Please, try again")
        return None  
    
    # Return None to indicate that an error occurred

    # finding current day:
    
    today = datetime.today().date()

    # counting difference between current day (today) and converted typed in date (converted_date)
    # converting them from datetime objects into integer using toordinal method
    # that way we count the difference between the ordinal numbers of the dates:

    difference = converted_date.toordinal() - today.toordinal()

    return difference

''' 
# example usage:
date = input("Please, write a date: ")
print(f"The difference between the current day and your date is {get_days_from_today(date)}")
'''