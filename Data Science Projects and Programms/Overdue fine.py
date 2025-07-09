def payfine(days = int(input("Enter number of overdue days: "))):
    if days <= 5:
        fine = days * 2
    elif days <= 10:
        fine = (5 * 2) + (days - 5) * 5
    else:
        fine = (5 * 2) + (5 * 5) + (days - 10) * 10
    return fine
print("Total Fine:", payfine(), "Rs")
