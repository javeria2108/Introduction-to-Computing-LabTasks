n=int(input("enter number of terms,n"))
if n<=0:
        print ('n should be greater than 0')
else:
        i=2
        j=-5
        for x in range (1,n+1):
                if x%2!=0:
                        print (i,end='')
                        i+=2
                elif x%2==0:
                        print(j,end='')
                        if x<n:
                                print('+',end='')
                        j-=5
        
      
