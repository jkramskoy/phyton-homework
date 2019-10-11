print("Hello.Please enter a number between 1 and 100")

while (True):
    number = int(input("Enter your number here"))
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 5 == 0:
        print("buzz")
    elif number % 3 == 0:
        print("fizz")





