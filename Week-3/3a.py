def div(n):
    li=[]
    for i in range(1,n//2):
        if(n%i==0):
            li.append(i)
    li.append(n)
    print(li)

a=int(input("enter the number : "))
div(a)
