def Addition(i,j):
        z=i+j
        return z
def subtraction (i,j):
        z=i-j
        return z
def multiplication(i,j):
        z=i*j
        return z
def division (i,j):
    z=i/j
    return z
print ('enter 1 for + , 2 for -, 3 for *, 4 for /')
x=int(input('1st no.'))
y=int(input ('2nd no.'))
i=int(input('enter choice'))
if i==1:
    k=Addition(x,y)
    print ('sum is',k)
if i==2:
    k=subtraction (x,y)
    print ('subtraction s',k)
if i==3:
    k=multiplication(x,y)
    print ('product is',k)
if i==4:
    k=division (x,y)
    print('div is',k)
    
