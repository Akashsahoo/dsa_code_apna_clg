def permutations(string,ans):
    if len(string)==0:
        print(ans)
        return
    for index in range(len(string)):
        permutations(string[0:index]+string[index+1:],ans+string[index])




permutations("abc","")