n=0
with open('test.txt', 'r') as f:
    for i in f:
        n+=1
print("Number of lines in file=",n)        