class Employees:
    def add_employee(self):
        self.emp=[]
        count=int(input("\nEnter The number of Employees :"))
        print("\nEnter the Employee Name :")
        for i in range(count):
            ename=input()
            self.emp.append(ename)

    def view_employee(self):
        print("\nList Employees")
        for sno ,name in enumerate(self.emp,1):
            print("{}{}".format(sno,name))


    def delete_employee(self):
        data=input("\nWhich EmployeeYou Want to delete :")
        if data in self.emp:
            self.emp.remove(data)
            print("invaid Emolyee Name..")
        else:
            print("Invalid Employee Name..")
obj=Employees()

while True:
        print("\n")
        print("1.Add Employee")
        print("2.View Employee")
        print("3.Delete Employee")
        print("4.Exit")

        data=int(input("\nEnter the operation :"))

        if data==1:
            obj.add_employee()

        elif data==2:
            obj.view_employee()

        elif data==3:
            obj.delete_employee()

        else:
            quit    