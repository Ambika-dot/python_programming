"""
Q-2:A traveler on a visit to India is in need of some Indian Rupees(INR) but he has money belonging to another currency.He wants to know how much money he should provide in the currency he
has,to get the specified amount in INR.Write a python program to implement a currency calculator which accepts the amount needed in INR and the name of the currency which the traveler
has.The program should identify and display the amount the traveler should provide in the currency he has, to get the specified amount in INR.
Note: Use the forex information provided in the table below for the calculation.Consider that only the currency names mentioned in the table are valid.For any invalid currency name,
display -1.
Currency                       Equivalent of 1.00 INR
Euro                                  0.01417
British Pound                         0.0100
Austrian Dollar                       0.02140
Canadian Dollar                       0.02027

"""

def currencycal(AmountINR,curr):
    if curr=="Euro":
        print(AmountINR*0.01417)
    elif curr=="British Pound":
        print(AmountINR*0.0100)
    elif  curr=="Austrian Dollar":
        print(AmountINR*0.02140)
    elif curr=="Canadian Dollar":
        print(AmountINR*0.02027)
    else:
        print(-1)
currencycal(300,"Euro")
currencycal(300,"British Pound")
currencycal(300,"Austrian Dollar")
currencycal(300,"Canadian Dollar")

