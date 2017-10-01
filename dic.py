def read():
  return int(input())
def compute(text,n,d):
  for i in range(n):
    d[text[0]]=text[1]
  return d
n=read()
d={}
for i in range(n):
  text=list(input().split('='))
  d=compute(text,n,d)
print(d)
