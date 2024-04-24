import datetime

def request_year_of_birth():
    current_year = datetime.datetime.now().year
    while True:
        year_input = input("Enter your year of birth (type 'q' to quit): ")
        if year_input.lower() == 'q':
            return None
        try:
            year_of_birth = int(year_input)
            if year_of_birth > current_year:
                print(f"Please enter a year of birth not more than {current_year}.")
            else:
                return year_of_birth
        except ValueError:
            print("Please enter a valid year of birth (e.g., 1990).")