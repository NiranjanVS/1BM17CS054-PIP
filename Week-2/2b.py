def rev1(str1):
    lis=str1.split(" ")
    lis.reverse()
    a=" "
    s2=a.join(lis)
    print(s2)

def rev2(str1):
    lis=str1.split(" ")
    lis2=" "
    for i in lis:
        lis2+=i[::-1]
        lis2+=" "
    print(lis2)

str1=input("Enter the string : ")
rev1(str1)
rev2(str1)