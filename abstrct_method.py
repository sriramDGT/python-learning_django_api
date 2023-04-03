from abc import ABC,abstractmethod

class Library(ABC):
    @abstractmethod
    def add_books(self):
        pass

    @abstractmethod
    def view_books(self):
        pass

    @abstractmethod
    def issue_books(self):
        pass

    @abstractmethod
    def return_books(self):
        pass

    @abstractmethod
    def delete_books(self):
        pass

class college(Library):
    def __init__(self,books):
        self.books=books

    def add_books(self):
        if self.books==[]:
            count=int(input("\nEnter the number of books :"))
            print("\nEnter Books Name :")
            for i in range(count):
                bname=input()
                self.books.append(bname)
                

        else:
            print("Enter The Books Add Name :")
            self.books.append(input())
            print("Your Book is Added...!")

    def view_books(self):
        print("\nList The Books Name ;")
        for sno,name in enumerate(self.books,1):
            print("{}{}".format(sno,name))

    def issue_books(self):
        pass

    def return_books(self):
        pass

    def delete_books(self):
        pass

books=[]
obj=college(books)

while True:
    print("\n")
    print("1.Add Books ")
    print("2.View Books ")
    print("3.Issue Books ")
    print("4.Return Books ")
    print("5.Delete Books")
    print("6.Exit ")

    data=int(input("\nEnter the Operation :"))

    if(data==1):
        obj.add_books()

    elif(data==2):
        obj.view_books()

    elif(data==3):
        obj.issue_books()

    elif(data==4):
        obj.return_books()

    elif(data==5):
        obj.delete_books()

    else:
        quit()