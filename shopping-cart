food = []
prices = []
total = 0

while True:
    quantity_of_food_item=int(input("enter the quantity of food item: "))
    if quantity_of_food_item==0:
        print("input end")
        break 
    food_to_input=input("enter the food: ")
    price_of_food=float(input("enter the price of food: "))
    
    for i in range (0,quantity_of_food_item):
        food.append(food_to_input)
        prices.append(price_of_food)

print("YOUR CART: ")
i=0
for i in range (len(food)) : 
    print(f"{food[i]} : {prices[i]}")
    total+=prices[i]

print(total)
