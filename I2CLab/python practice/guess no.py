i=9
guess = 0
while guess<3:
    inputt = int(input("guess the number"))
    guess = guess+1
    if inputt!=i:
        print ("wrong guess")
    elif inputt==i:
        print ("you won")
        break
    
    
