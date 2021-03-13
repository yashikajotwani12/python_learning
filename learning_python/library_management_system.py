class Library:
     def __init__(self, listofbooks):
         self.books=listofbooks



     def displayBooks(self):
         print("The Books Present in the libraries are:")
         for book in self.books:
             print("\t" + book)
    
     def borrowbooks(self, bookName):
        if bookName in self.books:
             print(f"You have borrowed this book {bookName}. Please Keep it safely. Return it in 30days")
             self.books.remove(bookName)
             return True
        else:
             print("Sorry this book has been already borrowed by somebody.Please wait the book is returned")
             return False
     def returnedbook(self, bookName):
         self.books.append(bookName)
         print("Thanks for returning the book!! . hope you enjoyed reading it")




class Student():
    def __init__(self):
        pass
    def requestbook(self):
        self.book=input("enter the book you want to borrow ")
        return self.book
    def returnbook(self):
        self.book=input("enter the book you want to return ")
        return self.book

       

if __name__=="__main__":

    centrallibrary=Library(["algorithms","django","flask","python","c++","c","cp","data Structures"])
    centrallibrary.displayBooks()
    student = Student()

    while(True):
        Welcomemsg=''' ===Welcome to Central Libtrary====
        Please Choose an option
        1. Listing all books
        2. request a book
        3. return a book
        4.exit the library
        '''
        print(Welcomemsg)
        a=int(input("enter a choice"))
        if(a==1):
            centrallibrary.displayBooks()
        elif ( a==2):
            centrallibrary.borrowbooks(student.requestbook())
        elif (a==3):
            centrallibrary.returnedbook(student.returnbook())
        elif a==4:
            print("Thanks for using the library !!")
            exit()
        else:
            print("Invalide Choice")
        
       
