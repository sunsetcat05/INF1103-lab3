inventory = 0
Failed = 0

stock = input("Please enter the stock quantity:")

while stock != "quit":   
    if not stock.isdigit():
        print("Invalid stock quantity. Please enter again.")
        Failed += 1
        print("Number of Failed/Rejected Entries:", Failed, "units")
    else:
        inventory += int(stock)
        print("Current Stock Quantity:", inventory)
    if inventory > 500:
        print("Inventory is exceeded.")
        break
    if inventory == 500:
        print("Maximum inventory reached. No more stock can be added.")
        break
    stock = input("Please enter the stock quantity:")

print("Total Units Processed:", inventory)
print ("Number of Failed/Rejected Entries:", Failed, "units")

    