def sol(n,output,last_item):
    if n==0:
        print(output)
        return

    
    sol(n-1,output+"0",last_item="0")
    if last_item=="0":
        sol(n-1,output+"1",last_item="1")
    

    # if last_item=="0":
    #     sol(n-1,output+"0",last_item="0")
    #     sol(n-1,output+"1",last_item="1")
    
    # if last_item=="1":
    #     sol(n-1,output+"0",last_item="0")


sol(4,"","0")

    
    
