data = input().split() 
order = input()
products = {}
for el in range(0, len(data), 2):
    k = data[el]
    v = int(data[el + 1])
    if k not in products:
        products[k] = 0
    products[k] += v
if order in products:
    print(f"We have {products[order]} of {order} left")
else:
    print(f"Sorry, we don't have {order}")
