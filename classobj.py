#class and object

class Addition:
    def add(self):
        a=int(input("Enter the Number :"))
        b=int(input("Enter the Number :"))
        c=a+b
        print("Addition",c)

class Subtraction:
    def sub(self):
        a=int(input("Enter the Number :"))
        b=int(input("Enter the Number :"))
        c=a-b
        print("Subtraction",c)

obj1=Addition()
obj1.add()

obj2=Subtraction()
obj2.sub()

class sri:
    a=10
    def hi(self):
        print("This is OOPs concept")
    
obj=sri()
obj.hi()
print("The Value Of A is :",obj.a)

class OOPs:
    def myfun1(self,name,age):
        self.name=name
        self.age=age

    def myfun2(self):
        print("Name :",self.name)
        print("Age :",self.age)

obj=OOPs()
obj.myfun1("Sriram",21)
obj.myfun2()

class siva:
    def visagan(self,name):
        self.name=name
        
    def seetha(self):
        print("Name :",self.name)

obj=siva()
obj.visagan("Swsthika")
obj.seetha()

class Myclass:
    def BioData(self,Name,Age,Address):
        self.Name=Name
        self.Age=Age
        self.Address=Address
        print("BioDate Of Me")

    def BioData1(self):
        print("Name :",self.Name)
        print("Age :",self.Age)
        print("Address :",self.Address)

obj=Myclass()
obj.BioData("Sriram",25,"Tenkasi")
obj.BioData1()

class function:
    def Mycls(self,name,age,address):
        print("NAME :",name)
        print("AGE :",age)
        print("ADDRESS :",address)

k=function()
k.Mycls("sivaram",21,"Tenkasi")

#Constructor

class Myclass():
    def __init__(self):
        print("Welcome to python")

obj=Myclass()

class Myclass():
    def __init__(self,name):
        print("Welcome :",name)

obj=Myclass("Sriram")

class Myclass():
    def __init__(self,name):
        self.name=name

    def Data(self):
        print("Welcome :",self.name)

obj=Myclass("Sri")
obj.Data()

#overloading

class Myclass:
    def fun(self,a):
        print(a)

    def fun(self,a,b):
        print(a+b)

    def fun(self,a,b,c):
        print(a+b+c)

obj=Myclass()
obj.fun(10,20,30)

class Myclass:
    def fun(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            return a+b+c

        elif a!=None and b!=None:
            return a+b

        else:
            return a
        
obj=Myclass()
print("Result :",obj.fun(50,20,30))

class Myclass:
    def fun(self,*args):
        sum=0
        for i in args:
            sum+=i
            print("Sum value :",sum)
obj=Myclass()
obj.fun(10)

class Mylass :
    def fun(self,*args):
        sum=0
        for i in args:
            sum+=i
            print("Sum :",sum)

obj=Myclass()
obj.fun(10,20,30,40)

#overriding

class ram:
    def project(self):
        print("Online Shopping Management System")

class sam(ram):
    def project(self):
        print("online Voting System")

obj=sam()
obj.project()

class ram:
    def project(self):
        print("Online Shopping Management System")
class sam(ram):
    def project(self):
        super().project()
        print("Online Voting System")

class kumar(sam):
    def project(self):
        super().project()
        print("Car rental System")

obj=kumar()
obj.project()

print("-----------------------------")

class siva:
    def visagan(self):
        print("Personal Expence Tracker")

class sri(siva):
    def visagan(self):
        super().visagan()
        print("Students Gravence System")

obj=sri()
obj.visagan()

#operational Overloading

class myclass:
    def __init__(self,a):
        self.a=a
    def __add__(self,others):
        return self.a+others.a
    
obj1=myclass(20)
obj2=myclass(30)
print("sum of value is :",obj1 +obj2)

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        #print("Name :",self.name)
        #print("Salaray :",self.salary)

    def __mul__(self,others):
        print("Name :",self.name)
        return self.salary * others.days

class Payroll:
    def __init__(self,days):
        self.days=days

obj1=Employee("Sriram",1000)
obj2=Payroll(24)
print("Net Salary :",obj1 * obj2)


#Single Inheritance 

class sri():
    def fun1(self):
        print("My name is sriram")

class siva(sri):
    def fun2(self):
        print("My name is sivaram")

obj=siva()
obj.fun2()
obj.fun1()


class Addition():
    def add(self):
        a=int(input("Enter the Number :"))
        b=int(input("Enter the Number :"))
        c=a+b
        print("Addition :",c)

class Subtraction(Addition):
    def sub(self):
        a=int(input("Enter the Number :"))
        b=int(input("Enter the Number :"))
        c=a-b
        print("Subtraction :",c)

obj=Subtraction()
obj.add()
obj.sub()

#Multiple Inheritance

class Addition:
    def add(self):
        a=int(input("Enter The Number :"))
        b=int(input("Enter The Number :"))
        c=a+b
        print("Addition :",c)

class Subtraction:
    def sub(self):
        a=int(input("Enter The Number :"))
        b=int(input("Enter The Number :"))
        c=a-b
        print("Subtraction :",c)

class myfun(Addition,Subtraction):
    def base(self):
        self.add()
        self.sub()

obj=myfun()
obj.base()

#Multi Level Inheritance

class Addition:
    def add(self):
        a=int(input("Enter the number :"))
        b=int(input('Enter the Number :'))
        c=a+b
        print("Addition :",c)

class Subtraction(Addition):
    def sub(self):
        a=int(input("Enter The Number :"))
        b=int(input("Enter The Number :"))
        c=a-b
        print("Subtraction :",c)

class Callfun(Subtraction):
    def call(self):
        self.add()
        self.sub()

obj=Callfun()
obj.call()

class get:
    def gitin(self):
        self.a=int(input("Enter The Number :"))
        self.b=int(input("Enter The Number :"))

class Addition(get):
    def add(self):
        self.gitin()
        c=self.a + self.b
        print("Addition :",c)

class Subtraction(get):
    def sub(self):
        self.gitin()
        c=self.a - self.b
        print("Subtraction :",c)

obj=Addition()
obj.add()

obj1=Subtraction()
obj1.sub()

#Hybird Inheritance

class get:
    def getin(self):
        self.a=int(input("Enter the number :"))
        self.b=int(input("Enter the number :"))

class Addition(get):
    def add(self):
        self.getin()
        c=self.a + self.b
        print("Addition :",c)

class Subtraction(get):
    def sub(self):
        self.getin()
        c=self.a - self.b
        print("Subtraction :",c)

class kaja(Addition,Subtraction):
    def kajal(self):
        self.add()
        self.sub()

obj1=kaja()
obj1.kajal()

#Encapsulation

class BANK():

    def __init__(self):
        self.__value=10
    def ram(self):
        print("Name :Ram")
        print("A/C :12345")
        print("Amount : 10000")
        print("Address :Tenkasi")

    def sam(self):
        print("Name : Sam")
        print("A/C :12346")
        print("Address :Chennai")
        print("Amount :10000")

obj1=BANK()
obj1.sam()
print("____________________________")

obj1.ram()

class division:
    def div(self):
        a=int(input("Enter The Number :"))
        b=int(input("Enter The Number :"))
        c=a/b
        print("Div :",c)

class multiplication:
    def mult(self):
        a=int(input("Enter The Number :"))
        b=int(input("Enter The Number :"))
        c=a*b
        print("mult :",c)

obj=division()
obj.div()

obj=multiplication()
obj.mult()
