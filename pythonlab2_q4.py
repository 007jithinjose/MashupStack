s=str(input("Enter String to check the repeated characters"))
for i in range(0,len(s)):
    count=0
    for j in range(0,len(s)):
        if(s[i]==s[j]):
            count+=1
    if(count>1):
        print(s[i],"occurs",count,"times")