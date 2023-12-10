def is_even(a):
    if a%2==0:
        return ('true')
    else:
        return ('false')
a=int(input('enter no.'))
is_even(a)
if is_even(a)=='true':
    print ('even no.')
else:
    print ('odd no.')
    
