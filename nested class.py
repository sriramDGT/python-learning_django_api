class Employee:
    def __init__(self,name,age,salary,technology):
        self.name=name
        self.age=age
        self.salary=salary
        self.technology=technology
        self.address=self.Address("106/2","South Street","Tenkasi","Tamilnadu","India")

    def show(self):
        print("Name :",self.name,",Age :",self.age,",Salary :",self.salary,",Technology :",self.technology)

    class Address():
        def __init__(self,doorno,street,location,state,country):
            self.doorno=doorno
            self.street=street
            self.location=location
            self.state=state
            self.country=country


        def showaddress(self):
            print("DoorNo :",self.doorno,",Street :",self.street,",Location :",self.location,",State :",self.state,",Country :",self.country)

emp1=Employee("Sriram",21,10000,"python")
emp1.show()
emp1.address.showaddress()
obj=Employee.Address("121","kovil Street","Coimbatore","Tamilnadu","India")
obj.showaddress()
emp1.address=obj