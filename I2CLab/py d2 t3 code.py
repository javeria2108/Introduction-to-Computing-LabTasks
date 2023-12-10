x=int(input("enter your salary"))
y=int(input("enter your scale"))
if y>16:
    b=(x*40/100)
    z=(x+b)
    print("your salary wit bonus is",z)
elif y<16:
      c=(x*20/100)
      d=(x+c)
      print("your salary with bonus is",d)
