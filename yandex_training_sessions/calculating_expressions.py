OPERATIONS = {
    '+': 0,
    '-': 0,
    '*': 1,
    '/': 1,
}


def calc(string):
    result = []
    steck = []
    idx = 0

    while idx < len(string):
        if string[idx].isdigit():
            result.append(string[idx])
        elif string[idx] == '(':
            steck.append(string[idx])
        elif string[idx] == ')':
            while steck[-1] != '(':
                result.append(steck.pop())
            steck.pop()
        else:
            while steck and steck[-1] != '(' and OPERATIONS[string[idx]] <= OPERATIONS[steck[-1]]:
                result.append(steck.pop())
            steck.append(string[idx])
        idx += 1

    while steck:
        result.append(steck.pop())

    return result


string = '6+3*(1+4*5)*2'
print(calc(string))
