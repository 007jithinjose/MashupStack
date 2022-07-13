f = open("test.txt")
n=int(input("Enter no of lines to display from file")) 
for i in range(n):
    print(f.readline())
f.close()