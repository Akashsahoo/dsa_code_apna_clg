from collections import deque

def duplicate_parenthesis(string):
    stack = deque()
    for char in string:
        if char == ")":
            count = 0
            while len(stack) and stack[len(stack)-1]!="(":
                stack.pop()
                count += 1
            if count < 1:
                return True
            else:
                stack.pop()
        else:
            stack.append(char)
    return False


#is_duplicate_parenthesis = duplicate_parenthesis("((a+b)+((c+d)))")

is_duplicate_parenthesis = duplicate_parenthesis("((a+b)+(c+d))")
print(is_duplicate_parenthesis)
