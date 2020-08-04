class library:
    def __init__(self,listOfBooks, libraryName):
        self.usrData = {}
        self.listOfBooks = listOfBooks
        self.libraryName = libraryName

        for books in self.listOfBooks:
            self.usrData[books] = None
    
    def displayBooks(self):
        for book in self.listOfBooks:
            print(book)

    def withdrawBook(self, nm1, book):
        if book in self.listOfBooks:
            if self.usrData[book] is None:
                self.usrData[book] = nm1
                print("done")
            elif self.usrData[book] == nm1:
                print("you already withdraw this book.")
            else:
                print(f"Book already withdraw by {self.usrData[book]}.")
        else:
            print("invalid book name!!!")

    def addBook(self, nBook):
        self.listOfBooks.append(nBook)
        self.usrData[nBook] = None
        print("done")

    def returnBook(self, nm2, book):
        if book in self.listOfBooks:
            if self.usrData[book] is not None:
                if self.usrData[book] == nm2:
                    self.usrData[book] = None
                    print("done")
                else:
                    print("this book is not belong to you")
            else:
                print(f"Sorry this book is not withdraw by anyone.")
        else:
            print("invalid book name!!!")
    
    def deleteBook(self, delBook):
        self.listOfBooks.remove(delBook)
        self.usrData.pop(delBook)
        print("done")

    def showUser(self):
        print("Books          Users\n")
        for bk in self.usrData:
            print(bk,"          ",self.usrData[bk])
        


def main():
    bookList = ["2666","All About Love","Desert Solitaire","Geek Love","Giovanni's Room","The Handmaid's Tale"]
    libNmae = "Sonu's"
    key = 5678

    lib1 = library(bookList,libNmae)

    print("="*50)
    print(f"                    welcome to {lib1.libraryName} Library")
    print("="*50)
    print("\nTo display all books type 'l'")
    print("To withdraw any book type 'w'")
    print("To add any book type 'a'")
    print("To return any book type 'r'")
    print("To delete any book type 'del'")
    print("To check Books data type 'data'")
    print("To quit type 'q'")
    
    loop = True
    while loop == True:
        inp = input("Option: ")

        print("-"*20)
        if inp == "l":
            lib1.displayBooks()
            
        elif inp == "w":
            nm1 = input("Enter your name: ")
            bk1 = input("Enter book name: ")
            lib1.withdrawBook(nm1, bk1)

        elif inp == "a":
            bk2 = input("Enter book name: ")
            lib1.addBook(bk2)

        elif inp == "r":
            nm2 = input("Enter your name: ")
            bk3 = input("Enter book name: ")
            lib1.returnBook(nm2, bk3)

        elif inp == "del":
            bk4 = input("Enter book name: ")
            ky = int(input("Enter secret key: "))
            if ky == key:
                lib1.deleteBook(bk4)
            else:
                print("You have no access to delete any book.")

        elif inp == 'q':
            print("Thanks for using.")
            loop = False

        elif inp == 'data':
            lib1.showUser()

        else:
            print("Invalid Input!!!")
        print("-"*20)

if __name__ == "__main__":
    main()
