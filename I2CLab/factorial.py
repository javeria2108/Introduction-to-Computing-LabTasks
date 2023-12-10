x=int(input('enter a positive number'))
if x<0:
    print("factorial doesn't exist")
else:
    factorial=1
    for i in range (1,x+1):
        factorial=factorial*i
    print('The factorial of',x,'is',factorial)
