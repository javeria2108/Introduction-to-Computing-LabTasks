name=str(input('enter name'))
if len(name)<3:
    print("name must be atleast three characters")
elif len(name)>50:
    print ("name can be maximum of 50 chrs")
else:
    print ("name looks good")
         
