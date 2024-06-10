products = {}

while True:
    entry = input()
    if entry == "START":
        break
    product, quantity = entry.split(": ")
    quantity = int(quantity)
    if product in products:
        products[product] += quantity
    else:
        products[product] = quantity
total_products = len(products)
total_quantity = sum(products.values())
for product, quantity in products.items():
    print(f"{product}: {quantity}")
print(f"Total products: {total_products}")
print(f"Total quantity: {total_quantity}")
