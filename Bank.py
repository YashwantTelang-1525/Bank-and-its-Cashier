amount = int(input())
r1 = 1
r2 = 2
rsum = r1+r2
ratio = amount/rsum
rem_value = amount - 2*ratio

ans = rem_value + ratio
print(round(ans))