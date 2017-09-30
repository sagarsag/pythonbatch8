n=int(input())
d={}
for i in range(n):
  text=(input().split('='))
  d[text[0]]=text[1]
print(d)
