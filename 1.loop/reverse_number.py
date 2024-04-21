n = 10899
revese_no = 0
while n!=0:
    revese_no = revese_no * 10 + n%10
    n = n // 10
print(revese_no)