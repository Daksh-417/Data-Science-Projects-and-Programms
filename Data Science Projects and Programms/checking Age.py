age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible for voting and driving")
elif age >= 16:
    print("You are eligible for driving (with rules)")
else:
    print("You are not eligible for voting or driving")
