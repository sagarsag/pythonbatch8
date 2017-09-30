def read():
  return int(input())
def compute(text):
  for i in range(n):
    #text=(readstring().split('='))
    d[text[0]]=text[1]
  return d
n=read()
d={}
t=[]
for i in range(n):
  text=list(input().split('='))
  d=compute(text)
print(d)
