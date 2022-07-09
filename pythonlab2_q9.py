from ast import Index
t=(input("Enter tuple"))
a=tuple(int(x) for x in t.split())
item=input("Enter item to find index in tuple")
i=0
print(Index(item))  
