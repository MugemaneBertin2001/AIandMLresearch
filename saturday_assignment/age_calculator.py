import datetime

def calculate_age(year_of_birth):
    current_year = datetime.datetime.now().year
    age = current_year - year_of_birth
    return age