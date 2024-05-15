def evalRPN(tokens) -> int:
    stack = []

    for element in tokens:
        if element not in ["+", "-", "*", "/"]:
            stack.append(int(element))
        else:
            v1 = stack.pop()
            v2 = stack.pop()
            if element == "+":
                newval = v1+v2
            elif element == '-':
                newval = v1-v2
            elif element == "*":
                newval = v1*v2
            else:
                newval = v1/v2
                if newval < 0:
                    newval = int(abs(newval)) * -1

            stack.append(newval)

    return stack.pop()
    

print(evalRPN(["2", "1", "+", "3", "*"]))