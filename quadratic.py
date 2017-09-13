global r1,r2,d
import cmath
def roots(a,b,c,d):
      r1=(-b+cmath.sqrt(d))/2*a
      r2=r1.conjugate()
      return r1,r2 
def read():
    return float(input()) 
print('enter coefficients of quadratic equatin  from higer order')
a=read(); 
b=read(); 
c=read(); 
d=(b**2)-(4*a*c) 
print('discriminant={0}'.format(d)) 
r=roots(a,b,c,d);
if(d==0):
 print('roots are real and equal')
elif(d>0):
 print('roots are real and distinct')
else:
 print('roots are complex')
print(r)
