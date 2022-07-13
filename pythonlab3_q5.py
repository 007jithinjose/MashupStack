f = open("test.txt") 
lst=[]
for i in f:
    lst.append(i)
print(lst)    
f.close()