def fib(n):
    if(n==1 or n==0):
        return 0
    elif(n==2):
        return 1
    else:
        return fib(n-1)+fib(n-2)


n=int(input("Enter the nuber : "))
li=[]
for i in range(1,n+1):
    a=fib(i)
    li.append(a)
for k in li:
    print(k,end=" ")
print()    