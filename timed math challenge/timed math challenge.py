import random

operators = ["+", "-", "*"]
min_operand = 3
max_operand = 12

def generate_problem():
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    operator = random.choice(operators)

    expr = str(left) + "" + operator + "" + str(right)
    answer = eval(expr)
    return expr, answer

    expr, answer = generate_problem()
    print(expr, answer)
