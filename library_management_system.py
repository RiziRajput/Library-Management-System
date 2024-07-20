def add_book(Books):
    name = str(input("Enter Book name->")).strip()
    if name:
        Books.append(name)
        print("Your Books:", Books)
    else:
        print("Book name cannot be empty.")
    return Books
     


def view_book(Books):
     
    if not Books:
        print("There is no book in the library")

    else:
        print("\nYour Books:")
        for i, task in enumerate(Books, start=1):
            print(f"{i}. {task}")
    # else:
    #     print("\nBooks that are available in your Library-->",Books)



def search_book(Books):
    n=str(input("enter the book which you want to search :"))
    if n in Books:
    
            print(f"yes, this book is availble.")
    else:
            print("Sorry, this book is not available")



def issue_book(Books):
    n=str(input("Enter the book which you want to Issue :"))
    if n in Books:
        Books.remove(n)
        print(f"Congratulations! The {n} Book is successfully issued now. " )
    else:
        print("This book is currently not availabel.")


   
def return_book(Books):
        n=str(input("enter the book which you want to Return :"))
        if n :
            Books.append(n)
            print(f"Congratulations! The {n} Book is successfully returned now. " )
        else:
            print("Book name could not be empty.")

    
def delete_book(Books):
    n=str(input("enter the book which you want to DELETE :"))
    if n in Books:
        Books.remove(n)
        print(f"Congratulations! The {n} Book is successfully Deleted now. " )
    else:
        print("This book is currently not availabel.")
    


def main():
    Books=[]
    while True:
        print("\n\t\t\t>>>>>>>>>>>>>  Library Management System  <<<<<<<<<<<<<")
        print("1. Add Books")
        print("2. Search Books")
        print("3. Issue Books")
        print("4. Return Books")
        print("5. Delete Books")
        print("6. View Books")
        print("7. Exit ")
        choice=int(input("Enter your Choice :"))
    
        if(choice==1):
            add_book(Books)
        elif(choice==2):
            search_book(Books)
        elif(choice==3):
            issue_book(Books) 
        elif(choice==4):
            return_book(Books) 
        elif(choice==5):
            delete_book(Books) 
        elif(choice==6):
            view_book(Books)
        elif(choice==7):
            print("Exiting the application, GoodBuy!")
            break
        else:
            print("invalid value, enter the number b/w 1 and 7")

if __name__ == "__main__":
    main()