while True:
    print("\nSelect an option")
    print("1 add a book")
    print("2 view all books")
    print("3 search a book")
    print("4 update a book")
    print("5 delete a book")
    print("6 exit")
    
    ch=int(input("select an option  : \n"))
    if (ch==1):
        print("selected add book")
    elif(ch==2):
         print("selected view all books")
    elif(ch==3):
        print("selected search books")
    elif(ch==4):
        print("selected update the books")
    elif(ch==5):
        print("selected delete books")
    elif(ch==6):
        break