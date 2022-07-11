class_list = dict()
n=int(input("Enter no of elements in dictionary"))
for i in range(0,n):
    key = int(input("Enter key"))
    value = int(input("Enter value"))
    class_list[key] = [value]
print(class_list.keys())
print(class_list.values())
print(class_list.items())

