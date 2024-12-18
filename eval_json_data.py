import json
def evaluate_inventory_expression(json_string, expression):
    inventory = json.loads(json_string)
    return eval(expression, {}, inventory)

json_string = '{"item1": 50, "item2": 30, "item3": 100}'
expression = "item1 if item1 > 40 else item2"
output = evaluate_inventory_expression(json_string, expression)
print(output) 
