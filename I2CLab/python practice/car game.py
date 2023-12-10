x=str(input("> type help for list of commands"))
if x=='help':
    print ('''start-to start the car
stop- to stop the car
quit-to exit''')
    y=str(input())
    if y=='start':
        print ('the car has started....ready to go')
        d=int(input ('how much kilometers you want your car to travel ?'))
        distance=1
        while distance<=d:
            print ('*')
            distance = distance+1
    elif y=='stop':
        print ('the car has stopped')
    elif y== 'quit':
        print ('process finished with exit code 0')
    else:
        print ("I don't understand")
else:
    print(' I dont understand')    
