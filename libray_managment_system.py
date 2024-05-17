from datetime import date


# importing the modules
import MYSQL.library_mangment_system
from datetime import date

# clean UDF to clear the window
def clean():
  for _ in range(1):
     print

# main_menu to let the user explore the different features of the Library management system project in Python and explore the options as per its scenario
def main_menu():
    while True:
          clean()
          print(' Welcome to the Feature Window of the Library Menu: ')
          print('\n1.  Add Books ')
          print('\n2.  Add Member ')
          print('\n3.  Update Book ')
          print('\n4.  Update Member ')
          print('\n5.  Issue Book')
          print('\n6.  Return Book ')
          print('\n7.  Search Menu ')
          print('\n8.  Report Menu ')
          print('\n9.  Special Menu ')
          print('\n0.  Take me Back to the Application')
          print('\n\n')
          choice = int(raw_input('Please select your choice: '))
# once the input from the user is taken, below are the different features to access from.
          if choice == 1:
              add_book()
          if choice == 2:
              add_member()
          if choice == 3:
              modify_book()
          if choice == 4:
              modify_member()
          if choice == 5:
              issue_book()
          if choice == 6:
              return_book()
          if choice == 7:
              search_menu()
          if choice == 8:
              report_menu()
          if choice == 9:
              special_menu()
          if choice == 0:
              break


if __name__ == "__main__":
    main_menu()


## Below code snippet is for Adding members
# Use the user-defined function in Python to create an add member function with the respective details
def addition_member():
    connection = mysql.connector.connect(
       host='localhost', database='library', user='root', password='')
    cursor = connection.cursor()
# database details addition

    name = raw_input('Please mention the Name of the Member :')
    email = raw_input('Please mention the Email of the Member :' )
    phone = raw_input('Please mention the Phone of the Member :' )
    address = raw_input('Please mention the Address of the Member :' )
    clas = raw_input('Please mention the Section of the Member :')
 
    sql_insert = 'insert into library_member(name,class,address,phone,email) values ( "' + \
      name + '","' + clas+'","'+address+'","'+phone + \
        '","'+email+'");'
    cursor.execute(sql_insert)
    connection.close()
#print statement gives the user the code that the new book details have been added in the librray_book successfully.
    print('\n\nYou New member record has been successfully added.')
    continuation = raw_input('\n\n Press 2 to continue ')
  


## Below code snippet is for Update Book
# using the user-defined function in Python to update the book with the respective details
def update_book():
    connection = mysql.connector.connect(
       host='localhost', database='library', user='root', password='')
  cursor = connection.cursor()
# database details addition
    clean()
    print('Welcome to the Book Update Information Window')
    print('-'*120)
    print('\n1. Update the Book Title')
    print('\n2. Update the Book Author')
    print('\n3. Update the Book Publisher')
    print('\n4. Update the Book Pages')
    print('\n5. Update the Book Price')
    print('\n6. Update the Book Edition')
    print('\n\n')
    choice = int(raw_input('Please select your choice: '))
    field =''
    if choice == 1:
        field =' title'
    if choice == 2:
        field = 'author'
    if choice ==3:
        field ='publisher'
    if choice == 4:
        field = 'pages'
    if choice == 5:
        field = 'price'
    book_id =raw_input('Please verify the Book ID :')
    value = raw_input('Please specify the new value :')
    if field =='pages' or field == 'price':
        sql_update = 'update library_book set ' + field + ' = '+value+' where id = '+book_id+';'
    else:
        sql_update = 'update library_book set ' + field + ' = "'+value+'" where id = '+book_id+';'
    print(sql_update)
    cursor.execute(sql_update)
# print statement gives the user the code that the new book details have been added in the librray_book successfully.
    print('\n\nYour Book record has been successfully updated.')
    connection.close()
    continuation = raw_input('\n\n Press 2 to continue')



## Below code snippet is for Update Member
# using the user-defined function in Python to update members with the respective details
def update_member():
    connection = mysql.connector.connect(
       host='localhost', database='library', user='root', password='')
    cursor = connection.cursor()
# database details addition
    clean()
    print('Welcome to the Member Update Information Window')
    print('-'*120)
    print('\n1. Update Name')
    print('\n2. Update Email')
    print('\n3. Update Phone')
    print('\n4. Update Address')
    print('\n5. Update Section')
    print('\n\n')
    choice = int(raw_input('Please select your choice: '))
    field =''
    if choice == 1:
        field ='name'
    if choice == 2:
        field = 'email'
    if choice ==3:
        field ='phone'
    if choice == 4:
        field = 'address'
    if choice == 5:
        field = 'section'
    member_id =raw_input('Please verify the member ID :')
    value = raw_input('Please specify the new value :')
    sql_update = 'update library_member set '+ field +' = "'+value+'" where id = '+member_id+';'
    print(sql_update)
    cursor.execute(sql_update)
    connection.close()
# print statement gives the user the code that the new book details have been added in the librray_book successfully.
    print('\n\nYou Member record has been successfully updated.')
    continuation = raw_input('\n\n Press 2 to continue')




## Below code snippet is for Issue Book
# using the user-defined function in Python to Issue a Book to the member with the respective details
def issue_thebook():
    connection = mysql.connector.connect(
       host='localhost', database='library', user='root', password='')
    cursor = connection.cursor()
# database details addition
    clean()
    print('\n You are viewing the BOOK ISSUE Window ')
    print('-'*120)
    book_id = raw_input('Please specify the Book  ID  for issuing: ')
    member_id  = raw_input('Please specify the Member  ID  for issuing:')
    output_book = status_book(book_id)
    output_member = status_member_issue(member_id)
    #print(output_member)
    today_date = date.today()
    if len(output_member) == 0:
        if result == 'available':
            sql_insert = 'insert into library_trans(b_id, m_id, date_of_issue) values('+book_id+','+member_id+',"'+str(today_date)+'");'
            sql_book_update = 'update library_book set status="issue" where id ='+book_id + ';'
            cursor.execute(sql_insert)
            cursor.execute(sql_book_update)
            print('\n\n\n The Book has been successfully ISSUED')
        else:
            print('\n\nThe Book is not available for ISSUING... The Current status says:',output_member)
     else:
         if len(output_member)<1:
             sql_insert = 'insert into library_trans(b_id, m_id, date_of_issue) values(' + \
             book_id+','+member_id+',"'+str(today)+'");'
             sql_book_update = 'update library_book set status="issue" where id ='+book_id + ';'
             cursor.execute(sql_insert)
             cursor.execute(sql_book_update)
             print('\n\n\n The Book has been successfully ISSUED')
         else:
             print('\n\nOne of the member has this book already issued to them')

# print statement gives the user the code that the new book details have been added in the librray_book successfully.
    print('\n\nYour Book record has been successfully updated.')
    connection.close()
    continuation = raw_input('\n\n Press 2 to continue')
 


## Below code snippet is for Return Book
# using the user-defined function in Python to Return the Book to the library with the respective details
fine_perday =10.0 


def return_thebook():
    connection = mysql.connector.connect(
       host='localhost', database='library', user='root', password='')
    cursor = connection.cursor()
# database details addition
    global fine_perday
    clean()
    print('\n Welcome to the BOOK RETURN Window ')
    print('-'*120)
    book_id = raw_input('Please specify the Book  ID  for issuing: ')
    member_id  = raw_input('Please specify the Member  ID  for issuing:')
    output_book = status_book(book_id)
    output_member = status_member_issue(member_id)
    #print(output_member)
    today_date = date.today()
    result = issuestatus_book(book_id,member_id)
    if output==None:
        print('Oh No! This Book is not Issued...Please try again with checking Book Id and Member ID...')
    else:
        sql_status='update book set status ="available" where id ='+book_id +';'
        date_of_return = (today - result[3]).days
        fine = din * fine_perday    #  fine per data
        sql_status_1 = 'update transaction set dor ="'+str(today)+'" , fine='+str(fine)+' where b_id='+book_id +' and m_id='+member_id+' and date_of_return is NULL;' 
       
        cursor.execute(sql_status)
        cursor.execute(sql_status_1)
        print('\n\nThis Book has been successfully RETURNED')
    connection.close()
    continuation = raw_input('\n\n Press 2 to continue')
    
# below are the two functions status_book(book_id) and status_member_issue(member_id) which we have used in the above UDF. 


# to check the status of the book that is issued to one member like if it's back to the library or not.
def status_member_issue(mem_id):
    connection = mysql.connector.connect(
       host='localhost', database='library', user='root', password='')
    cursor = connection.cursor()
    sql_select ='select * from library_trans where m_id ='+member_id +' and date_of_return is NULL;'
    print(sql_select)
    cursor.execute(sql_select)
    results = curfetch allhall()
    return results

# to check the status of the book that is issued to one member and the date of return is not at all mentioned.

def issuestatus_book(book_id,member_id):
    connection = mysql.connector.connect(
       host='localhost', database='library', user='root', password='')
    cursor = connection.cursor()
    sql_select = 'select * from library_trans where b_id ='+book_id + ' and m_id ='+ member_id +' and date_of_return is NULL;'
    cursor.execute(sql_select)
    result = cursor.fetchone()
    return result



# to check the status of the book 
def status_book(book_id):
    connection = mysql.connector.connect(
       host='localhost', database='library', user='root', password='')
    cursor = connection.cursor()
    sql_select = 'select * from library_book where id ='+book_id + ';'
    cursor.execute(sql_select)
    result = cursor.fetchone()
    return result[5]



## Below code snippet is for Search Menu
# Use the user-defined function in Python to go to the Search Menu of the LMS system to search for any book or related details  
def menu_search():
    while True:
        clean()
        print(' Welcome to the Search Menu!! You can search from various options listed below)
        print("\n1.  Search for Title of the Book")
        print('\n2.  Search for Author of the Book')
        print('\n3.  Search for Publisher of the Book')
        print('\n4.  Take me back to Main Menu')
        print('\n\n')
        choice = int(raw_input('Please specify by your choice: '))
        field =''
        if choice == 1:
            field='title'
        if choice == 2:
            field = 'author'
        if choice == 3:
            field = 'publisher'
        if choice == 4:
            break
        search_book(field)
        
# to search a book in the table that we returned in the above UDF, below is its code snippet

def book_search(field):
    connection = mysql.connector.connect(
       host='localhost', database='library', user='root', password='')
    cursor = connection.cursor()
    clean()
    print('\n Welcome to the Search Window for Books!')
    print('-'*120)
    message ='Enter '+ field +' Value :'
    title = raw_input(message)
    sql_select ='select * from library_book where '+ field + ' like "%'+ title+'%"'
    cursor.execute(sql_select)
    records = cursor.fetchall()
    clear()
    print('The output after performing the search on the table in the database  for :',field,' :' ,title)
    print('-'*120)
    for result in results:
      print(result)
    connection.close()
    continuation = raw_input('\n\n Press 2 to continue')


## Below code snippet is for Report Menu 
# using the user-defined function in Python to go to the Report Menu of the LMS system to generate reports for any book or member-related details  
def report_menu():
    while True:
        clean()
        print(' Welcome to the Report Generation menu!!! Please select from the below-given list to generate the report: ')
        print("\n1. To generate report of all the books")
        print('\n2. To generate report of all the members')
        print('\n3. To generate report of all the issued books')
        print('\n4. To generate a report of all the available books')
        print('\n5. To generate report of all the weed out books')
        print('\n6. To generate a report of all the lost books')
        print('\n7. To generate a report of all the stolen books')
        print('\n8. To generate report of all the fine collections of books')
        print('\n9. Take me back to Main Menu')
        print('\n\n')
        choice = int(raw_input('Please specify your choice ...: '))
        if choice == 1:
            issuedbooks_report()
        if choice == 2:
            availablebooks_report()
        if choice == 3:
            lostbooks_report()
        if choice == 4:
            memberlist_report()
        if choice == 5:
            finecollection_report()
        if choice == 6:
            stolenbooks_report()
        if choice == 7:
            booklist_report()
        if choice == 8:
            weedoutbooks_report()
        if choice == 9:
            break
    
#### for all the options that are being returned we created their res[ective small user-defined functions in Python as shown below.

### To generate a report of all the books: `booklist_report()`

def booklist_report():
    connection = mysql.connector.connect(
        host='localhost', database='library', user='root', password='')
    cursor = connection.cursor()
    clean()
    print('\n To generate report of all the books ')
    print('-'*120)
    sql_select ='select * from library_book'
    cursor.execute(sql_select)
    results = cursor.fetchall()
    for result in results:
       print(result)
    connection.close()
    continuation = raw_input('\n\n Press 2 to continue')
    
    
### To generate a report of all the members: `memberlist_report()`

def memberlist_report():
    connection = mysql.connector.connect(
        host='localhost', database='library', user='root', password='')
    cursor = connection.cursor()
    clean()
    print('\n REPORT - Members List ')
    print('-'*120)
    sql = 'select * from library_member'
    cursor.execute(sql_select)
    results = cursor.fetchall()
    for result in results:
       print(result)
    connection.close()
    continuation = raw_input('\n\n Press 2 to continue')
    
    
### To generate a report of all the issued books: `issuedbooks_report()`

def issuedbooks_report():
    connection = mysql.connector.connect(
        host='localhost', database='library', user='root', password='')
    cursor = connection.cursor()
    clean()
    print('\n To generate report of all the issued books')
    print('-'*120)
    sql_select = 'select * from library_book where status = "issue";'
    cursor.execute(sql)
    results = cursor.fetchall()
    for result in results:
       print(result)
    connection.close()
    continuation = raw_input('\n\n Press 2 to continue')
    
    
### To generate e report of all the available books: `availablebooks_report()`

def availablebooks_report():
    connection = mysql.connector.connect(
        host='localhost', database='library', user='root', password='')
    cursor = connection.cursor()
    clean()
    print('\n To generate report of all the available books ')
    print('-'*120)
    sql_select = 'select * from library_book where status = "available";'
    cursor.execute(sql_select)
    results = cursor.fetchall()
    for result in results:
       print(result)
    connection.close()
    continuation = raw_input('\n\n Press 2 to continue')
    
    
### To generate a report of all the weed-out books: `weedoutbooks_report()`


def weedoutbooks_report():
    connection = mysql.connector.connect(
        host='localhost', database='library', user='root', password='')
    cursor = connection.cursor()

    clean()
    print('\n To generate report of all the weed out books')
    print('-'*120)
    sql_select = 'select * from library_book where status = "weed-out";'
    cursor.execute(sql_select)
    results = cursor.fetchall()
    for result in results:
       print(result)
    connection.close()
    continuation = raw_input('\n\n Press 2 to continue')
    
    
### To generate e report of all the lost books: `lostbooks_report()`

def lostbooks_report():
    connection = mysql.connector.connect(
        host='localhost', database='library', user='root', password='')
    cursor = connection.cursor()
    clean()
    print('\n REPORT - BOOK TITLES - lost')
    print('-'*120)
    sql = 'select * from library_book where status = "lost";'
    cursor.execute(sql_select)
    results = cursor.fetchall()
    for result in results:
       print(result)
    connection.close()
    continuation = raw_input('\n\n Press 2 to continue')
    
    
### To generate report of all the stolen books: `stolenbooks_report()`

def stolenbooks_report():
    connection = mysql.connector.connect(
        host='localhost', database='library', user='root', password='')
    cursor = connection.cursor()
    clean()
    print('\n To generate report of all the stolen books')
    print('-'*120)
    sql_select = 'select * from library_book where status = "stolen";'
    cursor.execute(sql_select)
    results = cursor.fetchall()
    for result in results:
       print(result)
    connection.close()
    continuation = raw_input('\n\n Press 2 to continue')
    
    
### To generate a report of all the fines collected for books: `finecollection_report()`
 



def finecollection_report():
    connection = mysql.connector.connect(
        host='localhost', database='library', user='root', password='')
    cursor = connection.cursor()
    sql ='select sum(fine) from library_trans where date_of_return ="'+str(date.today())+'";'
    cursor.execute(sql_select)
    result = cursor.fetchone() 
# return tuple form of values
    clean()
    print('The book falling under fine collection')
    print('-'*120)
    print('The total fine collected today :',result[0])
    print('\n\n\n')
    connection.close()
    continuation = raw_input('\n\n Press 2 to continue')



## Below code snippet is for Return Book
# Use the user-defined function in Python to access the Special Book to the library with the respective details
def special_menu():

    while True:
        clean()
        print(' Welcome to the Special Menu!!! Please select from the below-given list  for accessing special command for the LMS system:  ')
        print("\n1. Special menu for accessing if a book is weed out ')
        print('\n2. Special menu for accessing if the book is  lost' )
        print('\n3. Special menu for accessing if the book is stolen' )
        print('\n4. Special menu for accessing if the book is return book" )
        print('\n\n')
        choice = int(raw_input('Please specify your choice: '))
        status=''
        if choice == 1:
            status ='weed-out'
        if choice == 2:
            status = 'lost'
        if choice == 3:
            status = 'stolen'
        if choice == 4:
            break
        book_id = raw_input('Please enter the book id :')
        change_book_status(status,book_id)
      
# user-defined function for checking the change book status 

def bookstatus_changes(status,book_id):
    connection = mysql.connector.connect(
       host='localhost', database='library', user='root', password='')
    cursor = connection.cursor()
    sql_update = 'update book set status = "'+status +'" where id ='+book_id + ' and status ="available"'
    cursor.execute(sql_update)
    print('Now the booking status has been changed ',status)
    print('\n\n\n')
    connection.close()
    continuation = raw_input('\n\n Press 2 to continue')




## FINAL SOURCE CODE for Library management system project in Python


############Step 1: To set up the database along with data records inserted in the Table

######### CODE BASE FOR SQL Database and Tables###########

SET time_zone = "+00:00";

Database: `library`
######Creating the schema for first tables: library_book
--

CREATE TABLE `library_book` (
  `id` int(15) NOT NULL,
  `title` char(80) DEFAULT NULL,
  `author` char(60) DEFAULT NULL,
  `pages` int(8) DEFAULT NULL,
  `price` float(8,2) DEFAULT NULL,
  `status` char(15) DEFAULT NULL,
  `publisher` char(80) DEFAULT NULL,
  `edition` char(20) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

########### INSERT some record to the table library_book

INSERT INTO `library_book` (`id`, `title`, `author`, `pages`, `price`, `status`, `publisher`, `edition`) VALUES
(1, 'java', 'jensen', 120, 350.00, 'available', 'TKpublisher', '3'),
(2, 'Python', 'ohio', 120, 380.00, 'available', 'TKpublisher', '1');
(3, 'C', 'nitoa', 120, 540.00, 'available', 'TKpublisher', '2');
(4, 'golang', 'eunmi', 120, 730.00, 'available', 'TKpublisher', '8');
-- --------------------------------------------------------

######Creating the schema for first tables: library_member

CREATE TABLE `library_member` (
  `id` int(15) NOT NULL,
  `name` char(60) DEFAULT NULL,
  `class` char(20) DEFAULT NULL,
  `address` char(200) DEFAULT NULL,
  `phone` char(30) DEFAULT NULL,
  `email` char(70) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

########### INSERT some record to the table library_member


INSERT INTO `member` (`id`, `name`, `class`, `address`, `phone`, `email`) VALUES
(1, 'Niya', '12th standard', 'victoria garden', '123456789', 'niya@gmail.com');
(2, 'Zara', '7th standard', 'angel park', '987654321', 'zara@gmail.com');
(3, 'Rohan', '5th standard', 'shadow park', '456321789', 'rohan@gmail.com');
(4, 'Ritwik', '11th standard', 'garden street', '654789321', 'ritwik@gmail.com');
------------------------------------------------------------

######Creating the schema for first tables: library_transaction

CREATE TABLE `library_trans` (
  `tid` int(15) NOT NULL,
  `b_id` int(20) DEFAULT NULL,
  `m_id` int(30) DEFAULT NULL,
  `date_of_invite` date DEFAULT NULL,
  `date_of_return` date DEFAULT NULL,
  `fine` float(25,2) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--------------######Below are some indexes for tables ##########-----------

############# Indexes for table `library_book`
--
ALTER TABLE `library_book`
  ADD PRIMARY KEY (`id`);

--
############# Indexes for table `library_member`
--
ALTER TABLE `library_member`
  ADD PRIMARY KEY (`id`);

--
############# Indexes for table `library_trans`
--
ALTER TABLE `library_trans`
  ADD PRIMARY KEY (`tid`);


############Step 2: To start adding the above learnt code snippet for the Library management system project in Python


# importing the modules
import mysql.connector
from datetime import date

# clean UDF to clear the window
def clean():
  for _ in range(1):
     print

# main_menu to let the user explore the different features of the Library management system project in Python and explore the options as per its scenario
def main_menu():
    while True:
          clean()
          print(' Welcome to the Feature Window of the Library Menu:')
          print("\n1.  Add Books")
          print('\n2.  Add Member')
          print('\n3.  Modify Book Information')
          print('\n4.  Modify Student Information')
          print('\n5.  Issue Book')
          print('\n6.  Return Book')
          print('\n7.  Search Menu')
          print('\n8.  Report Menu')
          print('\n9.  Special Menu')
          print('\n0.  Take me Back to the Application')
          print('\n\n')
          choice = int(raw_input('Please select your choice: '))
# once the input from the user is taken, below are the different features to access from.
          if choice == 1:
              add_book()
          if choice == 2:
              add_member()
          if choice == 3:
              modify_book()
          if choice == 4:
              modify_member()
          if choice == 5:
              issue_book()
          if choice == 6:
              return_book()
          if choice == 7:
              search_menu()
          if choice == 8:
              report_menu()
          if choice == 9:
              special_menu()
          if choice == 0:
              break


if __name__ == "__main__":
    main_menu()

## Below code snippet is for Add books
# Use the user-defined function in Python to create an add book function with the respective details
def addition_book():
    connection = mysql.connector.connect(
       host='localhost', database='library', user='root', password='')
    cursor = connection.cursor()
# database details addition
    title = raw_input('Please mention the Title of the Book :')
    author = raw_input('Please mention the Author of the Book : ')
    publisher = raw_input('Please mention the Publisher of the Book : ')
    pages = raw_input('Please mention the Pages in the Book : ')
    price = raw_input('Please mention the Price of the Book : ')
    edition = raw_input('Please mention the Edition of the Book : ')
    copies  = int(raw_input('Please mention the Copies of the Book : '))
    sql_insert = 'insert into library_book(title,author,price,pages,publisher,edition,status) values ( "' + \
       title + '","' + author+'",'+price+','+pages+',"'+publisher+'","'+edition+'","available");'
   #sql2 = 'insert into transaction(dot,qty,type) values ("'+str(today)+'",'+qty+',"purchase");'
  #print(sql)
# using for loop in Python to make the addition of books in a loop
    for _ in range(0,copies):
        cursor.execute(sql_insert)
    connection.close()
# print statement gives the user the code that the new book details have been added in the librray_book successfully.
    print('\n\nYou New Book record has been successfully added.')
    continuation = raw_input('\n\n Press 2 to continue')

## Below code snippet is for Add members
# using the user-defined function in Python to create an add member function with the respective details
def addition_member():
    connection = mysql.connector.connect(
       host='localhost', database='library', user='root', password='')
    cursor = connection.cursor()
# database details addition

    name = raw_input('Please mention the Name of the Member :')
    email = raw_input('Please mention the Email of the Member :' )
    phone = raw_input('Please mention the Phone of the Member :' )
    address = raw_input('Please mention the Address of the Member :' )
    clas = raw_input('Please mention the Section of the Member :')
 
    sql_insert = 'insert into library_member(name,class,address,phone,email) values ( "' + \
      name + '","' + clas+'","'+address+'","'+phone + \
        '","'+email+'");'
    cursor.execute(sql_insert)
    connection.close()
#print statement gives the user the code that the new book details have been added in the librray_book successfully.
    print('\n\nYou New member record has been successfully added.')
    continuation = raw_input('\n\n Press 2 to continue')
    
## Below code snippet is for Update Book
# using the user-defined function in Python to update the book with the respective details
def update_book():
    connection = mysql.connector.connect(
       host='localhost', database='library', user='root', password='')
  cursor = connection.cursor()
# database details addition
    clean()
    print('Welcome to the Book Update Information Window')
    print('-'*120)
    print('\n1. Update the Book Title')
    print('\n2. Update the Book Author')
    print('\n3. Update the Book Publisher')
    print('\n4. Update the Book Pages')
    print('\n5. Update the Book Price')
    print('\n6. Update the Book Edition')
    print('\n\n')
    choice = int(raw_input('Please select your choice: '))
    field =''
    if choice == 1:
        field ='title'
    if choice == 2:
        field = 'author'
    if choice ==3:
        field ='publisher'
    if choice == 4:
        field = 'pages'
    if choice == 5:
        field = 'price'
    book_id =raw_input('Please verify the Book ID :')
    value = raw_input('Please specify the new value :')
    if field =='pages' or field == 'price':
        sql_update = 'update library_book set ' + field + ' = '+value+' where id = '+book_id+';'
    else:
        sql_update = 'update library_book set ' + field + ' = "'+value+'" where id = '+book_id+';'
    print(sql_update)
    cursor.execute(sql_update)
# print statement gives the user the code that the new book details have been added in the librray_book successfully.
    print('\n\nYour Book record has been successfully updated.')
    connection.close()
    continuation = raw_input('\n\n Press 2 to continue')

## Below code snippet is for Update Member
# using the user-defined function in Python to update member  with the respective details
def update_member():
    connection = mysql.connector.connect(
       host='localhost', database='library', user='root', password='')
    cursor = connection.cursor()
# database details addition
    clean()
    print('Welcome to the Member Update Information Window')
    print('-'*120)
    print('\n1. Update Name')
    print('\n2. Update Email')
    print('\n3. Update Phone')
    print('\n4. Update Address')
    print('\n5. Update Section')
    print('\n\n')
    choice = int(raw_input('Please select your choice: '))
    field =''
    if choice == 1:
        field ='name'
    if choice == 2:
        field = 'email'
    if choice ==3:
        field ='phone'
    if choice == 4:
        field = 'address'
    if choice == 5:
        field = 'section'
    member_id =raw_input('Please verify the member ID :')
    value = raw_input('Please specify the new value :')
    sql_update = 'update library_member set '+ field +' = "'+value+'" where id = '+member_id+';'
    print(sql_update)
    cursor.execute(sql_update)
    connection.close()
# print statement gives the user the code that the new book details have been added in the librray_book successfully.
    print('\n\nYou Member record has been successfully updated.')
    continuation = raw_input('\n\n Press 2 to continue')

## Below code snippet is for Issue Book
# using the user-defined function in Python to Issue Book to the member with the respective details
def issue_thebook():
    connection = mysql.connector.connect(
       host='localhost', database='library', user='root', password='')
    cursor = connection.cursor()
# database details addition
    clean()
    print('\n You are viewing the BOOK ISSUE Window ')
    print('-'*120)
    book_id = raw_input('Please specify the Book  ID  for issuing: ')
    member_id  = raw_input('Please specify the Member  ID  for issuing:')
    output_book = status_book(book_id)
    output_member = status_member_issue(member_id)
    #print(output_member)
    today_date = date.today()
    if len(output_member) == 0:
        if result == 'available':
            sql_insert = 'insert into library_trans(b_id, m_id, date_of_issue) values('+book_id+','+member_id+',"'+str(today_date)+'");'
            sql_book_update = 'update library_book set status="issue" where id ='+book_id + ';'
            cursor.execute(sql_insert)
            cursor.execute(sql_book_update)
            print('\n\n\n The Book has been successfully ISSUED')
        else:
            print('\n\nThe Book is not available for ISSUING... The Current status says:',output_member)
     else:
         if len(output_member)<1:
             sql_insert = 'insert into library_trans(b_id, m_id, date_of_issue) values(' + \
             book_id+','+member_id+',"'+str(today)+'");'
             sql_book_update = 'update library_book set status="issue" where id ='+book_id + ';'
             cursor.execute(sql_insert)
             cursor.execute(sql_book_update)
             print('\n\n\n The Book has been successfully ISSUED')
         else:
             print('\n\nOne of the member has this book already issued to them')

# print statement gives the user the code that the new book details have been added in the librray_book successfully.
    print('\n\nYour Book record has been successfully updated.')
    connection.close()
    continuation = raw_input('\n\n Press 2 to continue')
    
    
## Below code snippet is for Return Book
# using the user-defined function in Python to Return Book to the library with the respective details
fine_perday =10.0 


def return_thebook():
    connection = mysql.connector.connect(
       host='localhost', database='library', user='root', password='')
    cursor = connection.cursor()
# database details addition
    global fine_perday
    clean()
    print('\n Welcome to the BOOK RETURN Window ')
    print('-'*120)
    book_id = raw_input('Please specify the Book  ID  for issuing: ')
    member_id  = raw_input('Please specify the Member  ID  for issuing:')
    output_book = status_book(book_id)
    output_member = status_member_issue(member_id)
    #print(output_member)
    today_date = date.today()
    result = issuestatus_book(book_id,member_id)
    if output==None:
        print('Oh No! This Book is not Issued...Please try again with checking Book Id and Member ID...')
    else:
        sql_status='update book set status ="available" where id ='+book_id +';'
        date_of_return = (today - result[3]).days
        fine = din * fine_perday    #  fine per data
        sql_status_1 = 'update transaction set dor ="'+str(today)+'" , fine='+str(fine)+' where b_id='+book_id +' and m_id='+member_id+' and date_of_return is NULL;' 
       
        cursor.execute(sql_status)
        cursor.execute(sql_status_1)
        print('\n\nThis Book has been successfully RETURNED')
    connection.close()
    continuation = raw_input('\n\n Press 2 to continue')
    
# below are the two functions status_book(book_id) and status_member_issue(member_id) which we have used in the above UDF. 


# to check the status of the book that is issued to one member like if it's back to the library or not.
def status_member_issue(mem_id):
    connection = mysql.connector.connect(
       host='localhost', database='library', user='root', password='')
    cursor = connection.cursor()
    sql_select ='select * from library_trans where m_id ='+member_id +' and date_of_return is NULL;'
    print(sql_select)
    cursor.execute(sql_select)
    results = cursor.fetchall()
    return results

# to check the status of the book that is issued to one member and the date of return is not at all mentioned.

def issuestatus_book(book_id,member_id):
    connection = mysql.connector.connect(
       host='localhost', database='library', user='root', password='')
    cursor = connection.cursor()
    sql_select = 'select * from library_trans where b_id ='+book_id + ' and m_id ='+ member_id +' and date_of_return is NULL;'
    cursor.execute(sql_select)
    result = cursor.fetchone()
    return result



# to check the status of the book 
def status_book(book_id):
    connection = mysql.connector.connect(
       host='localhost', database='library', user='root', password='')
    cursor = connection.cursor()
    sql_select = 'select * from library_book where id ='+book_id + ';'
    cursor.execute(sql_select)
    result = cursor.fetchone()
    return result[5]


## Below code snippet is for Search Menu
# using the user-defined function in Python to go to the Search Menu of the LMS system to search for any book or related details  
def menu_search():
    while True:
        clean()
        print(' Welcome to the Search Menu!! You can search from various options listed below')
        print("\n1.  Search for Title of the Book")
        print('\n2.  Search for Author of the Book')
        print('\n3.  Search for Publisher of the Book')
        print('\n4.  Take me back to Main Menu')
        print('\n\n')
        choice = int(raw_input('Please specify by your choice: '))
        field =''
        if choice == 1:
            field='title'
        if choice == 2:
            field = 'author'
        if choice == 3:
            field = 'publisher'
        if choice == 4:
            break
        search_book(field)
        
# to search a book in the table that we returned in the above UDF, below is its code snippet

def book_search(field):
    connection = mysql.connector.connect(
       host='localhost', database='library', user='root', password='')
    cursor = connection.cursor()
    clean()
    print('\n Welcome to the Search Window for Books!')
    print('-'*120)
    messsage ='Enter '+ field +' Value :'
    title = raw_input(message)
    sql_select ='select * from library_book where '+ field + ' like "%'+ title+'%"'
    cursor.execute(sql_select)
    records = cursor.fetchall()
    clear()
    print('The output after performing the search on the table in the database  for :',field,' :' ,title)
    print('-'*120)
    for result in results:
      print(result)
    connection.close()
    continuation = raw_input('\n\n Press 2 to continue')



## Below code snippet is for Report Menu 
# using the user-defined function in Python to go to the Report Menu of the LMS system to generate reports for any book or member-related details  
def report_menu():
    while True:
        clean()
        print(' Welcome to the Report Generation menu!!! Please select from the below-given list to generate the report: ')
        print("\n1. To generate report of all the books")
        print('\n2. To generate report of all the members')
        print('\n3. To generate report of all the issued books')
        print('\n4. To generate a report of all the available books')
        print('\n5. To generate report of all the weed out books')
        print('\n6. To generate a report of all the lost books')
        print('\n7. To generate a report of all the stolen books')
        print('\n8. To generate report of all the fine collections of books')
        print('\n9. Take me back to Main Menu')
        print('\n\n')
        choice = int(raw_input('Please specify your choice ...: '))
        if choice == 1:
            issuedbooks_report()
        if choice == 2:
            availablebooks_report()
        if choice == 3:
            lostbooks_report()
        if choice == 4:
            memberlist_report()
        if choice == 5:
            finecollection_report()
        if choice == 6:
            stolenbooks_report()
        if choice == 7:
            booklist_report()
        if choice == 8:
            weedoutbooks_report()
        if choice == 9:
            break
    
#### for all the options that are being returned we created their res[ective small user-defined functions in Python as shown below.

### To generate report of all the books: `booklist_report()`

def booklist_report():
    connection = mysql.connector.connect(
        host='localhost', database='library', user='root', password='')
    cursor = connection.cursor()
    clean()
    print('\n To generate report of all the books ')
    print('-'*120)
    sql_select ='select * from library_book'
    cursor.execute(sql_select)
    results = cursor.fetchall()
    for result in results:
       print(result)
    connection.close()
    continuation = raw_input('\n\n Press 2 to continue')
    
    
### To generate report of all the members: `memberlist_report()`

def memberlist_report():
    connection = mysql.connector.connect(
        host='localhost', database='library', user='root', password='')
    cursor = connection.cursor()
    clean()
    print('\n REPORT - Members List ')
    print('-'*120)
    sql = 'select * from library_member'
    cursor.execute(sql_select)
    results = cursor.fetchall()
    for result in results:
       print(result)
    connection.close()
    continuation = raw_input('\n\n Press 2 to continue')
    
    
### To generate a report of all the issued books: `issuedbooks_report()`

def issuedbooks_report():
    connection = mysql.connector.connect(
        host='localhost', database='library', user='root', password='')
    cursor = connection.cursor()
    clean()
    print('\n To generate report of all the issued books')
    print('-'*120)
    sql_select = 'select * from library_book where status = "issue";'
    cursor.execute(sql)
    results = cursor.fetchall()
    for result in results:
       print(result)
    connection.close()
    continuation = raw_input('\n\n Press 2 to continue')
    
    
### To generate report of all the available books: `availablebooks_report()`

def availablebooks_report():
    connection = mysql.connector.connect(
        host='localhost', database='library', user='root', password='')
    cursor = connection.cursor()
    clean()
    print('\n To generate report of all the available books ')
    print('-'*120)
    sql_select = 'select * from library_book where status = "available";'
    cursor.execute(sql_select)
    results = cursor.fetchall()
    for result in results:
       print(result)
    connection.close()
    continuation = raw_input('\n\n Press 2 to continue')
    
    
### To generate a report of all the weed-out books: `weedoutbooks_report()`


def weedoutbooks_report():
    connection = mysql.connector.connect(
        host='localhost', database='library', user='root', password='')
    cursor = connection.cursor()

    clean()
    print('\n To generate report of all the weed out books')
    print('-'*120)
    sql_select = 'select * from library_book where status = "weed-out";'
    cursor.execute(sql_select)
    results = cursor.fetchall()
    for result in results:
       print(result)
    connection.close()
    continuation = raw_input('\n\n Press 2 to continue')
    
    
### To generate report of all the lost books: `lostbooks_report()`

def lostbooks_report():
    connection = mysql.connector.connect(
        host='localhost', database='library', user='root', password='')
    cursor = connection.cursor()
    clean()
    print('\n REPORT - BOOK TITLES - lost')
    print('-'*120)
    sql = 'select * from library_book where status = "lost";'
    cursor.execute(sql_select)
    results = cursor.fetchall()
    for result in results:
       print(result)
    connection.close()
    continuation = raw_input('\n\n Press 2 to continue')
    
    
## To generate report of all the stolen books: `stolenbooks_report()`

def stolenbooks_report():
    connection = mysql.connector.connect(
        host='localhost', database='library', user='root', password='')
    cursor = connection.cursor()
    clean()
    print('\n To generate report of all the stolen books')
    print('-'*120)
    sql_select = 'select * from library_book where status = "stolen";'
    cursor.execute(sql_select)
    results = cursor.fetchall()
    for result in results:
       print(result)
    connection.close()
    continuation = raw_input('\n\n Press 2 to continue')
    
    
## To generate report of all the fine collected for books: `finecollection_report()`
 



def finecollection_report():
    connection = mysql.connector.connect(
        host='localhost', database='library', user='root', password='')
    cursor = connection.cursor()
    sql ='select sum(fine) from library_trans where date_of_return ="'+str(date.today())+'";'
    cursor.execute(sql_select)
    result = cursor.fetchone() 
# return tuple form of values
    clean()
    print('The book falling under fine collection')
    print('-'*120)
    print('The total fine collected today :',result[0])
    print('\n\n\n')
    connection.close()
    continuation = raw_input('\n\n Press 2 to continue')
    
## Below code snippet is for Return Book
# Use the user-defined function in Python to access the Special Book to the library with the respective details
def special_menu():

    while True:
        clean()
        print(' Welcome to the Special Menu!!! Please select from the below-given list  for accessing special command for the LMS system:  ')
        print('\n1. Special menu for accessing if a book is weed out')
        print('\n2. Special menu for accessing if a book is  lost' )
        print('\n3. Special menu for accessing if a book is stolen' )
        print('\n4. Special menu for accessing if a book is return book' )
        print('\n\n')
        choice = int(raw_input('Please specify your choice: '))
        status=''
        if choice == 1:
            status ='weed-out'
        if choice == 2:
            status = 'lost'
        if choice == 3:
            status = 'stolen'
        if choice == 4:
            break
        book_id = raw_input('Please enter the book id :')
        change_book_status(status,book_id)
      
# user-defined function for checking the change book status 

def bookstatus_changes(status,book_id):
    connection = mysql.connector.connect(
       host='localhost', database='library', user='root', password='')
    cursor = connection.cursor()
    sql_update = 'update book set status = "'+status +'" where id ='+book_id + ' and status ="available"'
    cursor.execute(sql_update)
    print('Now the booking status has been changed ',status)
    print('\n\n\n')
    connection.close()
    continuation = raw_input('\n\n Press 2 to continue')

