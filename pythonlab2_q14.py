t=(input("Enter Elements in Set"))
a=list(int(x) for x in t.split())
a=set(a)
print("Set elements:",a)
item=int(input("enter item to remove from set"))
for i in a:
    if(i==item):
        a.discard(item)
        break
print("Set elements",a)    
