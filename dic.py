def read():
  return int(input())
def compute():
  for i in range(n):
    text=(input().split('='))
    d[text[0]]=text[1]
  return d
n=read()
d={}
d=compute()
print(d)
