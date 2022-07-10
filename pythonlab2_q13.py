t=(input("Enter list to generate its sublists"))
a=list(int(x) for x in t.split())
lists = [[]]
for i in range(len(a) + 1):
    for j in range(i):
        lists.append(a[j: i])
print(lists)        