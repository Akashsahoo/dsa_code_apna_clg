def friend_pairing(n):
    if n==1 or n==2:
        return n
    totalways = friend_pairing(n-1) + (n-1)*friend_pairing(n-2)
    return totalways
print(friend_pairing(3))