import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',password='',database='librarydb')

mycursor=mydb.cursor()
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
        cat=input("Enter the category of the book")
        name=input("Enter the title of the book")
        author=input("Enter author name")
        pb=input("Enter the the publication")
        charge=input("Enter the book charge per day")
        sql='INSERT INTO `books`(`category`, `title`, `author`, `publication`, `price`) VALUES (%s,%s,%s,%s,%s)'
        data=(cat,name,author,pb,charge)
        mycursor.execute(sql,data)
        mydb.commit()        
        print("inserted success")
    elif(ch==2):
        sql='SELECT * FROM `books`'
        mycursor.execute(sql)
        result=mycursor.fetchall()
        for i in result:
            print(i)
        print("selected view all books")
    elif(ch==3):
        name=input("Enter the book title for searching the book")
        sql="SELECT * FROM `books` WHERE `title`='"+name+"'"
        mycursor.execute(sql)
        result=mycursor.fetchall()
        print(result)
    elif(ch==4):
        print("selected update the books")
    elif(ch==5):
        print("selected delete books")
    elif(ch==6):
        break