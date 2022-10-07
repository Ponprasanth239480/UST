def Palindromecheck(s):
    return string1 == string1[::-1]
 
 
string1 = str(input("enter the string : "))
ans = Palindromecheck(string1)
 
if ans:
    print("Yes, the given string is palindrome")
else:
    print("No, the given string is not palindrome")
