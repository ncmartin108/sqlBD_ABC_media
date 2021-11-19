import PySimpleGUI as sg
import mysql.connector
from tabulate import tabulate

#---------------------------------------------------------------------------
# Project Part 3
# Authors: Nasley Chumacero-Martin, Matthew Horrocks, Kashka Calvin
# CS 482 Database Management Systems I
#
# Program Description: This program uses PySimpleGUI module to create an
#   interactive application to manage the database abc_media_db. The
#   database was created in Part 1 of the Project (see crtdb.sql). That
#   same database was populated with sample entries in Part 1 of the
#   Project (see insdb.sql). In this program, a person will login to the
#   database using a set of preset crendentials, which are provided in a
#   plaintext file DB_Login.txt. Then, the application will allow the
#   person to interact with the database through menu options.
#---------------------------------------------------------------------------

# Sets a theme.
sg.theme('LightBrown1')


# In this section we will create the login window. The layout is where we
# modify the window layout, text and buttons that appear.
def make_loginwin():
    layout = [
        [sg.Text("Enter name of database:"), sg.InputText(key='-DB-')],
        [sg.Text("Enter the hostname:"), sg.InputText(key='-HName-')],
        [sg.Text("Enter username:"), sg.InputText(key='-Uname-')],
        [sg.Text("Enter password:"), sg.Input(password_char='*', key='-PW-')],
        [sg.Button("Login", bind_return_key=True), sg.Button("Reset"), sg.Exit()]
    ]
    # Creates the login window, with the layout as defined above.
    return sg.Window("Database Login", layout, finalize=True)


# In this second section we create the second window with menus. In this window
# the person will interact directly with the database after logging in.
def make_dbwin():
    # We will create the menu tabs first.
    tab1_layout = [
        [sg.Text("Show all Digital Displays?"), sg.Button('Yes')]
        ]
    tab2_layout = [
<<<<<<< Updated upstream

         [py_sg.Text("Enter Scheduler System type:"), py_sg.InputText(key='-SS-'), py_sg.Button('Search')],
         

        ]
    tab3_layout = [
         [py_sg.Text("Enter Serial Number:"), py_sg.InputText(key='-AddSN-')],
         [py_sg.Text("Enter Scheduler System type:"), py_sg.InputText(key='-AddSS-')],
         [py_sg.Text("Enter ModelNo Number:"), py_sg.InputText(key='-AddMN-'),py_sg.Button('Add')],
         
=======
         [sg.Text("Enter Scheduler System type:"), sg.InputText(key='-SS-'), sg.Button('Search', bind_return_key=True)]
        ]
    tab3_layout = [
         [sg.Text("Enter Serial Number:"), sg.InputText(key='-AddSN-')],
         [sg.Text("Enter Scheduler System type:"), sg.InputText(key='-AddSS-')],
         [sg.Text("Enter ModelNo Number:"), sg.InputText(key='-AddMN-'),sg.Button('Add')],
>>>>>>> Stashed changes
        ]
    tab4_layout = [
        ]
    tab5_layout = [
        ]
    layout = [
<<<<<<< Updated upstream
        [py_sg.TabGroup([[py_sg.Tab('1. Show Digital Displays', tab1_layout, key= '-TAB1'),
                          py_sg.Tab('2. Search Digital Displays', tab2_layout),
                          py_sg.Tab('3. Insert a Digital Display', tab3_layout),
                          py_sg.Tab('4. Delete a Digital Display', tab4_layout),
                          py_sg.Tab('5. Update a Digital Display', tab5_layout)]])],

        [py_sg.Output(size=(100,30), key = '_output_')],
        [py_sg.Button('Clear')],
        [py_sg.Button('Logout')],
=======
        [sg.TabGroup([[sg.Tab('1. Show Digital Displays', tab1_layout, key= '-TAB1-'),
                          sg.Tab('2. Search Digital Displays', tab2_layout),
                          sg.Tab('3. Insert a Digital Display', tab3_layout),
                          sg.Tab('4. Delete a Digital Display', tab4_layout),
                          sg.Tab('5. Update a Digital Display', tab5_layout)]])],
        [sg.Output(size=(80,30), key = '-Output-')],
        [sg.Button('Logout'), sg.Button('Clear')]
>>>>>>> Stashed changes
        ]
   
    # Creates the database interaction window, with the layout as specified above.
    return sg.Window("Main Database Menu", layout, finalize=True)


# This method creates the database connection.
def database_conn(db_name, username, passwd, hostname):
    mydb = None
    try:
        mydb = mysql.connector.connect(
            host = hostname,
            user = username,
            password = passwd,
            database = db_name )
        if mydb.is_connected():
            print('Connected to MySQL database')
    except Error as e:
        print(e)
    return mydb


# This method creates the table headings for menu option 1.
def table_headings():
    return "serialNo   schedulerSystem   modelNo"

# Main part of the program to open and run the windows.
def main():
    # Start with only the login window active.
    window2 = None
    window1 = make_loginwin()
    
    # Creates the event loop.
    while True:
        window, event, values = sg.read_all_windows()
    
        # This ends the program if the user closes the login window or presses the Exit button.
        if window == window1 and event == sg.WIN_CLOSED or window == window1 and event == 'Exit':
            break
            # Close the sql connection.
            if(mydb.is_connected()):
                mydb.close()
                mycursor.close()
                print("MySQL database connection is closed.")
    

        # This will save the values input in the login window. Also, we will launch the
        # second window here.
        elif event == 'Login' and not window2:
            db_name ='abc_media_db'
            username ='root'
            passwd = '1moreyearofschool'
            hostname ='localhost'
##            db_name = values['-DB']
##            username = values['-Uname-']
##            passwd = values['-PW-']
##            hostname = values['-HName-']
            
            # TEMP PRINT to make sure that we saved the input
            print(db_name, '\t', username, '\t' , passwd)
            # Hide login window to stop interaction with it.
            window1.hide()
            # Create the database interaction window.
            window2 = make_dbwin()

            # Create the database connection and login.
            mydb = database_conn(db_name, username, passwd, hostname)
            # Create a cursor object to manipulate database.
            mycursor = mydb.cursor(buffered=True)

        # This resets the text just typed into the login window.
        elif window == window1 and event == 'Reset':
            window['-DB-'].update('')
            window['-Uname-'].update('')
            window['-PW-'].update('')
            window['-HName-'].update('')

        # This will close window 2 if logout.
        elif window == window2 and event == 'Logout':
            window2.close()
            window2 = None
            window1.un_hide()

        elif window == window2 and event == 'Clear':
<<<<<<< Updated upstream
            window.FindElement('_output_').Update('')
=======
            window['-Output-'].Update('')
>>>>>>> Stashed changes

        # This will forcibly close window 2 if the user clicks X.
        elif window == window2 and event == sg.WIN_CLOSED:
            window2.close()
            window2 = None
            window1.un_hide()


        # Check Tab 1 event:
        elif window == window2 and event == 'Yes':
            sql = "SELECT * FROM DigitalDisplay;"
            mycursor.execute(sql)
            answer = mycursor.fetchall()
            print(table_headings())
            print(tabulate(answer))
            
<<<<<<< Updated upstream
        # Check the tab events.

        # Check the tab event search.

=======
        # Check Tab2 event.
>>>>>>> Stashed changes
        elif window == window2 and event == 'Search':
             SchedulerSystem = values['-SS-']
             sql1 = "SELECT * FROM DigitalDisplay WHERE schedulerSystem = '"+ SchedulerSystem + "';"
             mycursor.execute(sql1)
             myresults=mycursor.fetchall()
             print(table_headings())
             print(tabulate(myresults))
             window1.close()

<<<<<<< Updated upstream
        #check the tab event add.
=======
        # check the tab event add.
>>>>>>> Stashed changes
        elif window == window2 and event == 'Add':
            AddSerialNumber = values['-AddSN-']
            AddSchedulerSystem = values['-AddSS-']
            AddModelNumber = values['-AddMN-']
            check=True
<<<<<<< Updated upstream
            sql1= "SELECT modelNo FROM Model WHERE modelNo = '"+AddModelNumber+"';"
            print(sql1)
            mycursor.execute(sql1)
            searchres=mycursor.fetchall()
            test=[] 
            if searchres ==test:
                check=False
            print(table_headings())
            print(tabulate(searchres))
=======
            sql2 = "SELECT modelNo FROM Model WHERE modelNo = '"+AddModelNumber+"';"
            print(sql2)
            mycursor.execute(sql2)
            searches=mycursor.fetchall()
            test=[] 
            if searches ==test:
                check=False
            print(searches)
>>>>>>> Stashed changes

            try:
                sql= "INSERT INTO DigitalDisplay VALUES ('"+AddSerialNumber+"','"+AddSchedulerSystem+"','"+AddModelNumber+"');"
                #sql= "INSERT INTO DigitalDisplay VALUES ('serial2','random','VH356693');"
                mycursor.execute(sql)
                mydb.commit()
                check==True
            except:
               #insert code for new window asking for model data to be added.
                if check==False:
<<<<<<< Updated upstream
                     print("Could not insert Digital display because modelno not found")
=======
                     print("modelno not found")
>>>>>>> Stashed changes
            finally:
                if check==True:
                    print("modelno added")
            sql1= "SELECT * FROM DigitalDisplay;"    
            mycursor.execute(sql1)
            myresults=mycursor.fetchall()
<<<<<<< Updated upstream
            print(table_headings())
            print(tabulate(myresults))


=======
            print(myresults)


    # Finish the program by closing the window.
    window.close()
    
>>>>>>> Stashed changes

# Run main program.
if __name__ == '__main__':
    main()

