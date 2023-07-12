age = int(input("enter your age: "))
height = float(input("enter your height in centimeters: "))

if age >= 18 and height >= 180:
    print("Welcome! You meet the necessary age and height requirements.")
else:
    print("Sorry, you do not meet the necessary age and/or height requirements.")
