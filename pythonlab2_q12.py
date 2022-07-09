t=(input("Enter list of characters to convert into string"))
a=list(str(x) for x in t.split())
string=""
for x in a:
    string+=x
print(string)    