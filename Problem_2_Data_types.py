def Sum_Sub_Multi_D(number1,number2):
    print(f"{number1} + {number2} = {number1+number2}")
    print(f"{number1} - {number2} = {number1-number2}")
    print(f"{number1} * {number2} = {number1*number2}")
    print(f"{number1} / {number2} = {number1/number2:.2f}")


num1 = int(input("Please type here a number: "))
num2 = int(input("Please type here another number: "))

Sum_Sub_Multi_D(number1=num1,number2=num2)