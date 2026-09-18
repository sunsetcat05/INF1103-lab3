inventory = 0
Failed = 0

stock = get_valid_Input()

def get_valid_Input():
    while True:
        stock = input("Please enter the stock quantity:")
        if stock == "quit":
            return stock
        elif stock.isdigit():
            return int(stock)
        else:
            print("Invalid stock quantity. Please enter again.")

def process_quantity(stock):
    global inventory, Failed
    if stock == "quit":
        return
    elif isinstance(stock, int):
        inventory += stock
        print("Current Stock Quantity:", inventory)
    else:
        print("Invalid stock quantity. Please enter again.")
        Failed += 1
        print("Number of Failed/Rejected Entries:", Failed, "units")

def calculate_tax(amount):
    tax_rate = 0.1  # 10% tax rate
    tax = amount * tax_rate
    return tax

def generate_report():
    print("Total Units Processed:", inventory)
    print("Number of Failed/Rejected Entries:", Failed, "units")
    tax = calculate_tax(inventory)
    print("Total Tax on Inventory:", tax)
# while stock != "quit":   
#     if not stock.isdigit():
#         print("Invalid stock quantity. Please enter again.")
#         Failed += 1
#         print("Number of Failed/Rejected Entries:", Failed, "units")
#     else:
#         inventory += int(stock)
#         print("Current Stock Quantity:", inventory)
#     if inventory > 500:
#         print("Inventory is exceeded.")
#         break
#     if inventory == 500:
#         print("Maximum inventory reached. No more stock can be added.")
#         break
#     stock = input("Please enter the stock quantity:")

print("Total Units Processed:", inventory)
print ("Number of Failed/Rejected Entries:", Failed, "units")

    