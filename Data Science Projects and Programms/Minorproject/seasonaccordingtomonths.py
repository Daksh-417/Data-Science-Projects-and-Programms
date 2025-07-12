def get_season(month):
    month = month.lower()

    if month in ['december', 'january', 'february']:
        return 'Winter'
    elif month in ['march', 'april', 'may']:
        return 'Spring'
    elif month in ['june', 'july', 'august']:
        return 'Summer'
    elif month in ['september', 'october', 'november']:
        return 'Autumn'
    else:
        return 'Invalid month'
print("\t\t\tWelcome to season checker of your months:")
month_input = input("Enter the name of a month: ")
season = get_season(month_input)
print(f"The season for {month_input.capitalize()} is: {season}")
