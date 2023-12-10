a=int(input('what operation do you want to perform? press 1 for addition,2 for subtraction, 3 for multiply and 4 for div'))
if a==1:
    def Addition(i,j):
        z=i+j
        return z
    x=int(input('1st no.'))
    y=int(input('2nd no.'))
    j=Addition(x,y)
    print ('sum is',j)
if a==2:
    def subtraction (i,j):
        z=i-j
        return z
    x=int(input('1st no.'))
    y=int(input('2nd no.'))
    j=subtraction(x,y)
    print ('difference is',j)
if a==3:
    def multiplication(i,j):
        z=i*j
        return z
    x=int(input('1st no.'))
    y=int(input('2nd no.'))
    j=multiplication(x,y)
    print ('product is',j)
if a==4:
    def division (i,j):
        z=i/j
        return z
    x=int(input('1st no.'))
    y=int(input('2nd no.'))
    j=division(x,y)
    print ('quotient is',j)
    
    
    
