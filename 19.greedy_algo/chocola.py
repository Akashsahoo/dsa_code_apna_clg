def chocola(ver_cost,hor_cost):
    n  = len(ver_cost)
    m = len(hor_cost)
    
    ver_cost = sorted(ver_cost,reverse=True)
    hor_cost = sorted(hor_cost,reverse=True)

    h_index = 0
    v_index = 0
    hp = 1
    vp = 1
    cost = 0
    while h_index < m and v_index < n :
        if (ver_cost[v_index] <= hor_cost[h_index]):
            cost += (hor_cost[h_index]) * vp
            hp += 1
            h_index +=1
        else:
            cost += (ver_cost[v_index])*hp
            vp +=1
            v_index += 1
    
    while h_index <m:
        cost += hor_cost[h_index]*vp
        hp +=1
        h_index += 1
    
    while v_index <n:
        cost += ver_cost[v_index]*hp
        vp +=1
        v_index +=1
    
    print(f"min cost {cost}")


ver_cost = [2,1,3,1,4]
hor_cost = [4,1,2]

chocola(ver_cost,hor_cost)

    