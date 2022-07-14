lst=[1,2,3,4,5]
f=open("test.txt","w")
for i in lst:
    f.write("%s\n" % i)
f.close()
f=open("test.txt","r")
for i in f:
    print(f.readlines())

