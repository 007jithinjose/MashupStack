str="aeiou"
n=len(str)
arr = [] 
for i in range(0,n):    
    for j in range(i,n):  
        arr.append(str[i:(j+1)]);  
print("All possible subsets for given string are: ");  
for i in arr:  
    print(i);  