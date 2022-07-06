s=str(input("Enter String to check if its a palindrome"))
rev =s[::-1]
if(rev==s):
    print(s,"is a Palindrome")
else:
    print(s,"is not a Palindrome")
        