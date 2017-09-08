import math
def roots(a,b,c,d):
    global r1,r2
    if(d==0):
      r1=(-b)/(2*a)
      r2=(-b)/(2*a)
      return print('the roots are equal and real \n r1={0} r2={1}'.format(r1,r2))
    elif(d>0):
      r1=(-b+math.sqrt(d))/2*a
      r2=(-b-math.sqrt(d))/2*a
      return print('the roots are real and distinct\n r1={0} r2={1}'.format(r1,r2))
    else:
      r1=-b/2*a
      r2=math.sqrt(-d)/2*a
      return print('the roots are complex\n r1={0}+i{1} r2={1}-i{2}'.format(r1,r2,r1,r2)) 
def read():
    return float(input('enter coefficients\n')) 
a=read(); 
b=read(); 
c=read(); 
d=(b**2)-(4*a*c) 
print('discriminant={0}'.format(d)) 
r=roots(a,b,c,d);
print(r)
