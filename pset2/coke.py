amount_due = 50

while amount_due > 0 :
    coin= int(input("Enter the coins for coke "))
    if coin == 5 or coin == 10 or coin == 25:
        amount_due= amount_due - coin
    else :
        print("invalid coin")

    if amount_due <= 0 :
        print("change owd")
    else :
        print("Amount due is :",amount_due)
