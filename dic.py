def read():
  return int(input())
def compute(text):
  for i in range(n):
    t=text.split('=')
    d[t[0]]=t[1]
  return d
n=read()
d={}
for i in range(n):
  text=input()
  d=compute(text)
print(d)
