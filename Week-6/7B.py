n = int(input("Enter the size : "))
m = n
while(n):
    n=n-1
    for i in range(m):
        print(" --",end="")
    print("")
    for i in range(m):
        print("|  ",end="")
    print("|")
for i in range(m):
    print(" --",end="")
print('')
