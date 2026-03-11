#to be used for in-class exercise
#Error Handling
class FormulaError(Exception):
    pass

def parse_input(user_input):
    input_list = user_input.split()
    try:
        n1, op, n2 = input_list
    except ValueError:
        raise FormulaError("ERROR: NOT ENOUGH INPUTTED VALUES")

    try:
        n1 = float(n1)
        n2 = float(n2)
    except ValueError:
        raise FormulaError(f"ERROR: {n1} OR {n2} VALUES WHERE NOT NUMERIC")
    return n1, op, n2

def calculate(n1, op, n2):
    if op == '+':
        return n1 + n2
    if op == '-':
        return n1 - n2
    if op == '*':
        return n1 * n2
    if op == '/':
        return n1 / n2
    else:
        raise FormulaError(f"ERROR: OPERAND {op} NOT RECOGNIZED")

while True:
    user_input = input('enter number, operator and another number: ')
    if user_input == 'quit':
        break
    n1, op, n2 = parse_input(user_input)
    result = calculate(n1, op, n2)
    print(result)

