def fib(n):
    if(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        return fib(n-2)+fib(n-1)

a=int(input("Enter the number : "))
for i in range(1,a+1):
    print(fib(i))
	  
