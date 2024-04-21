def palendrom(string):
    ptr1 = 0
    ptr2 = len(string)-1
    while ptr1 <ptr2:
        if string[ptr1]== string[ptr2]:
            ptr1 += 1
            ptr2 -= 1
        else:
            print("not pallendrom")
            return
    print("pallendrom")


palendrom("akash")

