def Odd_Even(number):
    value = number%2
    if value == 0:
        print("even")
    else:
        print("odd")

num = None
num = int(input("Please type an integer value (without 0): "))
if num==0:
    num = int(input("Please enter number without 0: "))
    Odd_Even(number=num)
else:
    Odd_Even(number=num)