cart = []

while True:
    item = input("Enter item: ")

    if item == "done":
        break

    cart.append(item)
cart = tuple(cart)

print("Total items in cart =", len(cart))

print("Cart: ",cart)

print("CartType : ",type(cart))

print("Checkout")