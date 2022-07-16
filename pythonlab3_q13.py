import shutil
source="test.txt"
destination="test1.txt"
dest = shutil.copyfile(source, destination)
print("Destination Path",dest)
f=open("test1.txt")
print(f.readlines())
