list2= ("this is the first string", "this Is the second string")
spaces=0
for string1 in list2:
    for character1 in string1:
        if character1=="I":
            spaces+=1
print (spaces)        
