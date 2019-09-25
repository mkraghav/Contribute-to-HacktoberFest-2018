from collections import Counter
n,arr=int(input()),list(map(int,input().split()))
m,brr=int(input()),list(map(int,input().split()))
a,b=Counter(arr),Counter(brr)
print(*(sorted((b-a).keys())))
