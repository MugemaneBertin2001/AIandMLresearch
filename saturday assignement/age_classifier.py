def classify_age(age):
    if age <= 18:
        return "YOUNG"
    elif age <= 30:
        return "YOUTH"
    elif age <= 45:
        return "ADULT"
    else:
        return "OLD"