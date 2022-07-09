s=str(input("Enter String to check its character frequency"))
for i in range(0,len(s)):
    count=0
    for j in range(0,len(s)):
        if(s[i]==s[j]):
            count+=1
    print(s[i],"occurs",count,"times")
            
