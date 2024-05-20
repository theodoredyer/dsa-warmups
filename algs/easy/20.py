class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        open_pars = ["(", "[", "{"]

        for char in s:
            if char in open_pars:
                stack.append(char)
            else:
                if stack:
                    leftside = stack.pop()
                    if (leftside == "(" and char != ")") or (leftside == "[" and char != "]") or (leftside == "{" and char != "}"):
                        return False
                else:
                    return False
        return stack == []