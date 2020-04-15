fil = open("PrimeNumbers.txt","r")
line = fil.read()
prime = line.split(" ")
prime.pop() 
print(len(prime))
fil.close()

fil = open("HappyNumbers.txt","r")
line = fil.read()
happy = line.split(" ")
happy.pop()
print(len(happy))
fil.close()

count = 0
for i in prime:
    if i in happy:
        print(i,end=" ")