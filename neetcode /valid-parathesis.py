
def isValid(s: str) -> bool:
    # the paranthesis stack :
    stack = []

    # the matching dict :
    match = {
        ")":"(",
        "}":"{",
        "]":"["
    }

    for i in range(len(s)):
        # if opening we always push
        if s[i] in "({[":
            stack.append(s[i])
        # if not, if zero in stack - append else compare
        else:
            if len(stack) == 0:
                return False
            elif stack[-1] == match[s[i]]:
                stack.pop()
            else:
                return False

    return (len(stack) == 0)

print(isValid("((((]]]]]]]]]])))"))