from random import random, randrange


import  random 
print("Generating a number between 1 and 9")
rnum=random.randrange(1,9,1)
guess=int(input("Guess the number generated and enter it"))
if(rnum==guess):
    print(rnum,"is same you guessed it exactly right")
elif(rnum<guess):
    print(rnum,"you guessed it too high") 
elif(rnum>guess):
    print(rnum,"you guessed it too low")
else:
    print("ok")    