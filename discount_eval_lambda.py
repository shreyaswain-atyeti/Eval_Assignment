import json
def apply_discount(products, expression):
    return eval(expression, {}, {"products": products})
products = [
    {"name": "apple", "price": 30},
    {"name": "banana", "price": 20},
    {"name": "cherry", "price": 50}
]
expression = "list(map(lambda x: {'name': x['name'], 'price': round(x['price'] * 0.9, 2)}, products))"
output = apply_discount(products, expression)
print(json.dumps(output, indent=4))  