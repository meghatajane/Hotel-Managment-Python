menu ={
    'Pizza':100,
    'Pasta': 99,
    'Cold coffe':40,
    'sandwize':70,
}

#Great
print("Welcome to our Hotel")
print("Pizza: Rs100\n Pasta: Rs99\n Cold-coffe: Rs40\n sandwize: Rs70")

order_total = 0 

#condition

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:  #membership item
    order_total += menu[item_1] #update order
    print(f"Your item{item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not available yet!")

another_order = input("Do you want to add another item? (yes/No)")
if another_order =="yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has beem added to order")

    else:
        print(f"Ordered item {item_2} is not available")


print(f"The total amount of item is to pay {order_total}")