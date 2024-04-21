from collections import deque

def reverse_string(stack,string):
    print(f"input string -> {string}")
    index = 0
    while index!=len(string):
        stack.append(string[index])
        index += 1
    
    string = ""
    while len(stack):
        top = stack.pop()
        string +=top
    print(f"output string -> {string}")

stack = deque()
reverse_string(stack,"priya")