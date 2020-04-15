def search(li,a):
    print(li)
    if a in li:
        return True
    else:
        return False

li=[]
a=0
print("Enter the elemts of the list (Enter -1 to exit)")
while(a!=-1):
    a=int(input())
    li.append(a)
b=int(input("enter the element to be searched: "))
print(search(li,b))