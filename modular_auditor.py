inventory = 0
Failed = 0



def get_valid_Input():
        global Failed
        stock = input("Please enter the stock quantity:")
        if stock == "quit":
            return stock
        if not stock.isdigit():
            print("Invalid stock quantity. Please enter again.")
            Failed += 1

def process_quantity(current_total, new_value):
    global inventory, Failed
    if new_value == "quit":
        return
    elif isinstance(new_value, int):
        inventory += new_value      
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

# print("Total Units Processed:", inventory)
# print ("Number of Failed/Rejected Entries:", Failed, "units")

while True:
    stock_quantity = get_valid_Input()
    if stock_quantity != "quit":
        process_quantity(inventory, stock_quantity)
        calculate_tax(inventory)
    else:
        generate_report()
        break
