t=(input("Enter list to find its sum"))
a=list(int(x) for x in t.split())
sum=0
for x in a:
    sum+=x
print("Sum= ",sum)    
