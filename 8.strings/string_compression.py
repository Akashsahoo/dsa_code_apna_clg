def string_compression(string):
    i = 0
    output = ""
    n = len(string)
    while i<n:
        output += string[i]
        num = 1
        j=i
        while j<n-1 and string[j]==string[j+1]:
            num +=1
            j +=1
        if num > 1:
            output += str(num)
        i += num
    print(output)
# string = "aaabbcccdd"
string = "acd"
string_compression(string)


