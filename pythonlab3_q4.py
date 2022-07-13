fname="test.txt"
n=int(input("Enter no of lines from last of file to print"))
with open(fname) as file:
        for line in (file.readlines() [-n:]):
            print(line, end ='')    