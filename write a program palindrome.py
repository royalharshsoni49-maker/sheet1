a=int(input("enter a number:"))
b=a
rev=0
while a!=0:
    dig=a%10
    rev=rev*10+dig
    a//=10
if b==rev:
    print("palindrome")
else:
    print("not palindrome")
