'''#nested if

mark=int(input("Enter the Mark :"))
if mark >=35:
    print(mark,"Pass")
    if mark>=90:
        print(mark,"Pass With First Class")
    else:
        print(mark,"Not First Class")

else:
    print("Fail")

def table(n,t):
    if n!=0:
        table(n-1,t)
        print(n,"*",t,"=",n*t)

n=int(input("Enter The Limit :"))
t=int(input("Enter The Table :"))

table(n,t)

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
    
n=int(input("Enter The Number :"))
res=fact(n)
print("The Factorial is:",res)'''

def sum(n):
    if n==0:
        return 1
    else:
        return n+sum(n-1)
    
n=int(input("Enter the number :"))
res=sum(n)
print("sum of value:",res)