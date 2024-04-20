import age_calculator
import age_classifier
import user_input

def main():
    while True:
        year_of_birth = user_input.request_year_of_birth()
        if year_of_birth is None:
            break
        age = age_calculator.calculate_age(year_of_birth)
        age_category = age_classifier.classify_age(age)
        print(f"You are {age} years old, and you fall into the '{age_category}' category.")

if __name__ == "__main__":
    main()