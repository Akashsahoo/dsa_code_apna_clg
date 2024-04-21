def indian_coin_exchange(target):
    indian_currency = [1,2,5,10,20,50,100,500]
    indian_currency = sorted(indian_currency,reverse=True)
    total_currency = 0
    currency = []
    index = 0
    while total_currency < target:
        if total_currency+indian_currency[index]<=target:
            currency.append(indian_currency[index])
            total_currency +=indian_currency[index]
        else:
            index +=1
    
    print(currency)

indian_coin_exchange(590)


