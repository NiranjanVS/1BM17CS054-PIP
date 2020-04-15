def even(li):
    evel=[]
    for a in li:
        if(a%2==0):
            evel.append(a)
    for i in evel:
        print(i,end=" ")
    print()    

n=int(input("Enter the number of elements : "))
li=[]
for i in range(n):
    a=int(input())
    li.append(a)
even(li)
