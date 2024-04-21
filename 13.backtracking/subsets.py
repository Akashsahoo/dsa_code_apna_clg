def subsets(string,ans,index):
    if index == len(string):
        print(ans)
        return
    
    # yes
    subsets(string,ans+string[index],index+1)
    #no
    subsets(string,ans,index+1)
    
subsets("abc","",0)

