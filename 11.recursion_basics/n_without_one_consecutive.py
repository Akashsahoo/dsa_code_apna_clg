def sol(n,output,index,last_item):
    if index==n:
        print(output)
        return

    
    sol(n,output+"0",index+1,last_item="0")
    if last_item=="0":
        sol(n,output+"1",index+1,last_item="1")
    

    # if last_item=="0":
    #     sol(n,output+"0",index+1,last_item="0")
    #     sol(n,output+"1",index+1,last_item="1")
    
    # if last_item=="1":
    #     sol(n,output+"0",index+1,last_item="0")


sol(3,"",0,"0")

    
    
