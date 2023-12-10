import time
for j in range (1,10):
    for i in range(1,21):
        if i%2==0:
            continue
        time.sleep(5)
        print (i,' is odd')
             
