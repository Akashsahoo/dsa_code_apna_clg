from collections import deque

def valid_parethesis(string):
    stack = deque()
    for char in string:
        if char == "(" or char == "{" or char == "[":
            stack.append(char)
        else:
            if not len(stack):
                return False
            if (char == "]" and stack[len(stack)-1] == "[") or (char == "}" and stack[len(stack)-1] == "{") or (char == ")" and stack[len(stack)-1] == "("):
              stack.pop()
            else:
                return False
    
    if not len(stack):
        return True


#is_valid = valid_parethesis("[()]{}{[()()]()}")
is_valid = valid_parethesis("[(])")
print(is_valid)

