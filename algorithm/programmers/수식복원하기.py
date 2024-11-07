def evaluate_expression(expression: str) -> tuple:
    elements = {}
    num = ''
    idx = 0
    max_num: int = 2;

    for char in expression:
        if char.isdecimal():
            num += char
            if int(char) > max_num:
                max_num = int(char);
        else:
            if num:
                elements[idx] = int(num)
                idx += 1
                num = ''
            if char in '+-':
                elements[idx] = char
                idx += 1
    
    if num:
        elements[idx] = int(num)
    
    return (elements, max_num);

def evaluate_expressions(expression: list[str]):
    len_expression = len(expression);
    evaluated_expression: list = [];
    evaluated_expression.append(5);
    max_notation: int = 2;
    for i in range(len_expression):
        (exp, max_num) = evaluate_expression(expression[i]);

        if max_notation < max_num:
            max_notation = max_num;

        evaluated_expression.append(exp);

    return (evaluated_expression, max_notation + 1);

def solution(expressions):
    answer = [];
    # ["12 + 3 = 5", "13 - 6 = 9"]
    inputed_expressions: list[str] = expressions;
    (evaluated_expressions, max_notation) = evaluate_expressions(inputed_expressions);
    print("max_notation: ", max_notation);

    for i in evaluated_expressions:
        print(i);
    return answer

test1 = ["14 + 3 = 17", "13 - 6 = X", "51 - 5 = 44"];

solution(test1);
