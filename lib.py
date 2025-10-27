# Library.

exit = ""

books = ["english", "math", "science", "history", "art"]

while exit != "e":
    print("Available books:")

    for book in books:
        print("-", book)
    choice = input("Enter the book you want to borrow (or 'e' to exit): ")
    
    if choice in books:
        print(f"You have borrowed the book: {choice}")
    
    if choice == "e":
        exit = "e"
        print("Exiting the library system. Goodbye!")    
