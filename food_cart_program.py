from collections import Counter

menu={"pizza": 300, 
      "cold drink": 100,
      "chips": 50,
      "momo": 200,
      "pasta": 250,
      "water": 30}

cart=[]

total=0

print("-------MENU-------")

for key , values in menu.items():
    print(f"{key}: {values}")

print("-----------")

while True:
    cart_item=input("enter the item you want to purchase and type q to quit: ").lower()
    if cart_item == "q":
        break
    elif cart_item in menu.keys():
        cart.append(cart_item)
    else:
        print("Invalid entry try again")


for i in cart:
    total+=menu.get(i)

print()
if len(cart)==0:
    print("cart is empty")
else:
    print("FINAL RECEIPT: ")
    cart_item_print=Counter(cart)
    print(cart_item_print)

print()
print(f"total is : {total}")

