print("enter three numbers")
x=int(input('first number'))
y=int(input('second number'))
z=int(input('third number'))
if (x>y and x>z):
    print('largest number is',x)
elif (y>z and y>x):
    print('largest number is',y)
elif (z>y and z>x):
    print('largest number is',z)
