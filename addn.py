def sum(a):
    sum=0
    for i in a :
        sum=sum+i
    return sum 
a=input('enter the elements\n') 
n=[int(x) for x in a.split()] 
s=sum(n);
print('sum={0}'.format(s))
