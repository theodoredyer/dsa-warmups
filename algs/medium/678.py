def validPartentheisString( s):

    left_open = 0
    remaining_wildcards = 0

    for c in s:
        if c == "(":
            left_open += 1
        elif c == "*":
            remaining_wildcards += 1
        else:
            left_open -=1

        if left_open == -1:
            if remaining_wildcards == 0:
                return False
            else:
                left_open += 1


    return left_open == 0 or left_open <= remaining_wildcards

print(validPartentheisString("()"))
print(validPartentheisString("(*)"))
print(validPartentheisString("((*)"))
print(validPartentheisString("(*))"))
print(validPartentheisString("(((*)"))