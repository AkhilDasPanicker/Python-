import math
print "Coefficient of x^2 "
a=input()
print "Enter coefficient of x "
b=input()
print "Enter a constant "
c=input()

d=(b*b)-(4*a*c)

r=math.sqrt(d)
e=(-b+r)/(2*a)

f=(-b-r)/(2*a)

if(d>0):
        print "Equation has Real Roots and Roots are ",e," and ",f
elif(d==0):
        print "Equation has Equal Roots and Roots are ",e," and ",f
else:
        print "Equation has Imaginary Roots and Roots are ",e," and ",f



