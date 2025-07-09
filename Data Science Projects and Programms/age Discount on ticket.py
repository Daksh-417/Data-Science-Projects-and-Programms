def agelogic(age = int(input("Enter your age: "))):
    if age < 5:
        print("Free Ticket")
    elif age <= 12:
        discount = fare*(25/100)
        print("Ticket Fare:", fare - discount)
    elif age >= 60:
        discount = fare*(15/100)
        print("Ticket Fare:", fare - discount)
    else:
        print("Ticket Fare:", fare)
fare = 100
agelogic()