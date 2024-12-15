def Buy(amount):
    if amount >=10000:
        print("Gucci Bag")
        if amount > 20000:
            print("Gucci Belt")
    elif amount >=5000:
        print("Levis Bag")
    else:
        print("Something")


taka = None
try:
    taka = int(input("Please enter an integer amount: "))
    Buy(amount=taka)
except ValueError:
    print("Please enter a valid amount.")
    taka = int(input("Please enter an integer amount: "))
    Buy(amount=taka)
