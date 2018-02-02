#palindrome

def palin(n):
    s=0
    n_1=n
    while(n>0):
        temp=n%10
        n=n//10
        s=s*10+temp
        
    if(n_1==s):
        print("Number is Palindrome")
    else:
        print("Number is Not Palindrome")

n=int(input("Enter any value For Palindrome: "))
palin(n)

#calculator
def cal(operation,num1,num2):
    if(operation=="+"):
        print("Sum of Two number "+ str(num1+num2))
    elif(operation=="-"):
        print("Substraction of Two number "+ str(num1-num2))
    elif(operation=="*"):
        print("Multiply of Two number "+ str(num1*num2))
    elif(operation=="/"):
        print("Division of Two number "+ str(num1/num2))
    else:
       print("Wrong operation")
op=input("Enter operation +,-,*,/ :")
a=int(input("Enter Number one: "))
b=int(input("Enter Number Two: "))
cal(op,a,b)




#10 number   
def number(n):
    for i in range(n):
        print(i)
        
n=int(input("Enter n value:"))
number(n)

