a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
x=input("Entetr the operator : ")
if(x=='+'):
    print(a,x,b,"=",a+b)
elif(x=='-'):
    print(a,x,b,"=",a-b)
elif(x=='*'):
    print(a,x,b,"=",a*b)
elif(x=='/'):
    if(b==0):
        print("division by zero")
    else:
        print(a,x,b,"=",a/b)
elif(x=='%'):
    if(b==0):
        print("division by zero")
    else:
        print(a,x,b,"=",(a*100/b))
else:
    print("you have entered a improper variable")
