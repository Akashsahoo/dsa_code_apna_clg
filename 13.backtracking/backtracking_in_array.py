def changearr(li,index,val):
    if index==len(li):
        print(li)
        return
    
    li[index]=val
    changearr(li,index+1,val+1)
    # backtracking step
    li[index] -=2
li =[-1]*5
changearr(li,0,0)
print(li)