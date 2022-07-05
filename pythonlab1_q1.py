from datetime import *
name=input("Enter Name")
age=int(input("Enter Age"))
print("Welcome ",name)
remage=int(100)-age
today=date.today()
age100=int(today.year)+remage
print("Year you will turn 100 is",age100)