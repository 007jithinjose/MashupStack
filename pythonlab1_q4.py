num=int(input("Enter number to find its divisors"))
i=1
while(i<=num):
    if(num%i==0):
        print(i)  
    i=i+1     