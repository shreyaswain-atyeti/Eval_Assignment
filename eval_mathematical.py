def evaluate_expression(expression, variables):
    return eval(expression, {}, variables)

expression = "a + b * c"
variables = {"a": 4, "b": 2, "c": 3}
output = evaluate_expression(expression, variables)
print(output) 
