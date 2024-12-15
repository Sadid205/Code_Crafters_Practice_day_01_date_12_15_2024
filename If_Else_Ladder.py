def ladder(number):
    if number > 0:
        print("positive")
    elif number < 0:
        print("negetive")
    else:
        print("zero")

num = None
try:
    num = int(input("Please Enter an Integer value: "))
    ladder(number=num)
except ValueError:
    print("This dose not and integer")
    num = int(input("Please Enter an Integer value: "))
    ladder(number=num)
