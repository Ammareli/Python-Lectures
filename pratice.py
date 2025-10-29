# MY SHOP.

# name = "Ammar"

# print(f"my name is{name}")


"""
WELCOME TO MY SHOP!

AVALABLE PRODUCTS:
1. APPLE - $2
2. BANANA - $1
3. ORANGE - $3
4. GRAPES - $4

PLEASE SELECT A PRODUCT BY TYPING ITS NAME:
HOW MANY WOULD YOU LIKE TO BUY?
CLIENT NAME:

MY SHOP RECEIPT:
________________________________
CLINET NAME: {client_name}
PRODUCT: {product_name}
QUANTITY: {quantity}
TOTAL PRICE: ${total_price}
THANK YOU FOR SHOPPING WITH US!

"""

products = ["APPLE", "BANANA", "ORANGE", "GRAPES"]
prices = [2, 1, 3, 4]

print("WELCOME TO MY SHOP!\n")
print("_________________________________________\n")
print("AVALABLE PRODUCTS:")

price_index = 0
for product in products:
    print(f"- {product} - {prices[price_index]}pkr")
    price_index += 1
while True:
    print("\nPLEASE SELECT A PRODUCT BY TYPING ITS NAME:")
    product_name = input().upper() # ammar -> AMMAR
    print("HOW MANY WOULD YOU LIKE TO BUY?")
    quantity = int(input())
    print("CLIENT NAME:")
    client_name = input()


    if product_name in products:
        product_index = products.index(product_name)  # Get the index of the selected product
        product_price = prices[product_index] # Get the price using the index
        total_price = product_price * quantity

        print("\nMY SHOP RECEIPT:")
        print("________________________________")
        print(f"CLINET NAME: {client_name}")
        print(f"PRODUCT: {product_name}")
        print(f"QUANTITY: {quantity}")
        print(f"TOTAL PRICE: {total_price}pkr")
        print("THANK YOU FOR SHOPPING WITH US!")
    else:
        print("Sorry, the product you selected is not available in our shop.")

    exit_choice = input("\nType 'e' to exit or any other key to continue shopping: ")
    if exit_choice.lower() == 'e':
        break


