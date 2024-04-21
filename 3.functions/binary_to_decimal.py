def binary_to_decimal(bin_num):
    pow = 0
    decimal = 0
    while bin_num!=0:
        decimal +=bin_num%10*2**pow 
        bin_num = bin_num / 10
        pow +=1
    print(decimal)
binary_to_decimal(111)
