def max_length_chain_of_pairs(pairs):
    pairs = sorted(pairs,key=lambda x:x[1])

    max_chain_length = 0
    chain = []
    chain.append(pairs[0])
    max_chain_length = 1
    end_chain = pairs[0][1]

    for i in range(1,len(pairs)):
        if end_chain<pairs[i][0]:
            chain.append(pairs[i])
            max_chain_length += 1
            end_chain = pairs[i][1]
    
    print(max_chain_length)
    print(chain)



pairs = [[5,24],[39,60],[5,28],[27,40],[50,90]]
max_length_chain_of_pairs(pairs)