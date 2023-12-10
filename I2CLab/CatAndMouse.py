def CatAndMouse(a,b,c):
    if abs(a-c)>abs(b-c):
        return -1
    elif abs(a-c)<abs(b-c):
        return 1
    else:
        return 0
def mainFunction(x,y,z):
    p=CatAndMouse(x,y,z)
    if d==-1:
        return("Cat B")
    elif d==1:
        return ("Cat A")
    elif d==0:
        return ("Mouse C")
    
cata=int(input('position of Cat A ='))
catb=int(input('position of Cat B='))
mc=int(input('position of Mouse='))
d=CatAndMouse (cata,catb,mc)
e=mainFunction(cata,catb,mc)
print (d,e)
