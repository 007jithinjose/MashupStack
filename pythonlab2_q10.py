t=(input("Enter tuple"))
a=tuple(int(x) for x in t.split())
b=list(a)
l=len(b)
c=b[::-1]
c=tuple(c)
print(c)

