dic = {}
def remove_duplicates(string,dic,output="",index=0):
    if index==len(string):
        print(output)
        print(dic)
        return
    if string[index] not in dic.keys():
        dic[string[index]] = 1
        output +=string[index]
    else:
        dic[string[index]] += 1
    remove_duplicates(string,dic,output,index+1)

remove_duplicates("appnnacollege",dic)