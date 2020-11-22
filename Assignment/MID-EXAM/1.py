a = int(input("Budget: \t"))
b = int(input("Domestic Collection: \t"))
c= int(input("International Collection: \t"))
profit = (b+c)-a
if profit<0:
    print("No Profit")
else:
    print(f"Profit: {profit}")
if profit >= 3000000:
    print("Super Hit!!!") 
elif profit >= 2000000 and profit<= 3000000:
    print("Success!!")
elif profit >500000 and profit<=2000000:
    print("Average movie")
elif profit<=500000 and profit>=0:
    print("Flop movie! Waste of money. Waste of time.")
elif profit<0:
    print("Super flop movie!!")
