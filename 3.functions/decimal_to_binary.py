def decimal_to_binary(decimal_num):
    pow = 0
    bin_num = 0
    while decimal_num!=0:
        bin_num +=  decimal_num%2*10**pow 
        decimal_num = decimal_num // 2
        pow +=1
    print(bin_num)
decimal_to_binary(7)