x=int(input("enter the total bill"))
y=int(input("enter cash given by customer"))
z=y-x
if z<0:
    print("Warning: AMOUNT PAID IS LESS THAN TOTAL BILL")
else:
    print("Amount to be returned",z)
    notes1=z//5000
    remainder= z%5000
    notes2=remainder//1000
    remainder2= remainder%1000
    notes3= remainder2//500
    remainder3=remainder2%500
    notes4= remainder3//100
    remainder4=remainder3%100
    notes5= remainder4//50
    remainder5=remainder4%50
    notes6= remainder5//20
    remainder6=remainder5%20
    notes7=remainder6//10
    remainder7=remainder6%10
    coins8=remainder7//5
    remainder8=remainder7%5
    coins1=remainder8//2
    remainder9=remainder8%2
    coins2=remainder9//1
    if z>5000:
        print('5000:',notes1)
    if z>1000:
            print("1000:",notes2)
    if z>500:
                print('500:',notes3)
    if z>100:
                    print('100',notes4)
    if z>50:
                        print('50:',notes5)
    if z>20:
                            print('20:',notes6)
    if z>10:
                              print('10:',notes7)
    if z>5:
                                    print('5:',coins8)
    if z>2:
                                         print('2:',coins1)
    if z>1:
                                            print('1:',coins2)
                                        
                        
        
