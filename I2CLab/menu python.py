print("do you want to eat something")
a=str(input())
while (a=='y'):
       print ("welcome to Raja's restaurant")
       print ("choose 1-4")
       print("1.biryani")
       print("2.sphaghetti")
       print("3.karahi")
       print("4.chicken shashlik")
       x=int(input("enter choice: "))
       if (x==1):
              print ("how many plates of biryani?")
              y=int(input())
              z=y*100
              print("Biryani price is",z)
       elif (x==2):
                     print ("how many plates of sphaghetti?")
                     y=int(input())
                     z=y*100
                     print("sphaghetti price is",z)
       elif (x==3):
                            print ("how many plates of karahi?")
                            y=int(input())
                            z=y*100
                            print("karahi price is",z)
       elif (x==4):
                                   print ("how many plates of chicken shashlik?")
                                   y=int(input())
                                   z=y*100
                                   print("chicken shashlik price is",z)
                                   
if (a=='n'):
     print("loop finished")
