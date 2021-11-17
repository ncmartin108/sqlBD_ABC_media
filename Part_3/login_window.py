import PySimpleGUI as py_sg
import mysql.connector

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
py_sg.theme('LightBrown1')


# In this section we will create the login window. The layout is where we
# modify the window layout, text and buttons that appear.
def make_loginwin():
    layout = [
        [py_sg.Text("Enter name of database:"), py_sg.InputText(key='-DB-')],
        [py_sg.Text("Enter the hostname:"), py_sg.InputText(key='-HName-')],
        [py_sg.Text("Enter username:"), py_sg.InputText(key='-Uname-')],
        [py_sg.Text("Enter password:"), py_sg.Input(password_char='*', key='-PW-')],
        [py_sg.Button("Login"), py_sg.Button("Reset"), py_sg.Exit()]
    ]
    # Creates the login window, with the layout as defined above.
    return py_sg.Window("Database Login", layout, finalize=True)


# In this second section we create the second window with menus. In this window
# the person will interact directly with the database after logging in.
def make_dbwin():
    # We will create the menu tabs first.
    tab1_layout = [
        ]
    #tab1_layout = [
     #   [py_sg.Table(values=select_allDisplays(), headings=table_headings(),max_col_width=25,
      #               auto_size_columns=True, display_row_numbers=True, justification='right',
       #              num_rows=30, alternating_row_color='light blue',key='-TABLE-', row_height=35)]
        #]
    tab2_layout = [
        ]
    tab3_layout = [
        ]
    tab4_layout = [
        ]
    tab5_layout = [
        ]
    layout = [
        [py_sg.TabGroup([[py_sg.Tab('1. Show Digital Displays', tab1_layout, key= '-TAB1'),
                          py_sg.Tab('2. Search Digital Displays', tab2_layout),
                          py_sg.Tab('3. Insert a Digital Display', tab3_layout),
                          py_sg.Tab('4. Delete a Digital Display', tab4_layout),
                          py_sg.Tab('5. Update a Digital Display', tab5_layout)]])],
        [py_sg.Output(size=(100,30))],
        [py_sg.Button('Logout')]
        ]
   
    # Creates the database interaction window, with the layout as specified above.
    return py_sg.Window("Main Database Menu", layout, finalize=True)


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


# This method is for menu option 1: Display all displays. It will query the database and then return
# all available tuples.
def select_allDisplays():
    return [0, 10]  # temp data until we add a function


# This method creates the table headings for menu option 1.
def table_headings():
    return ['serialNo', 'schedulerSystem','ModelNo']


# Main part of the program to open and run the windows.
def main():
    # Start with only the login window active.
    window2 = None
    window1 = make_loginwin()
    
    # Creates the event loop.
    while True:
        window, event, values = py_sg.read_all_windows()
    
        # This ends the program if the user closes the login window or presses the Exit button.
        if window == window1 and event == py_sg.WIN_CLOSED or window == window1 and event == 'Exit':
            break

        # This will save the values input in the login window. Also, we will launch the
        # second window here.
        elif event == 'Login' and not window2:
            db_name = values['-DB-']
            username = values['-Uname-']
            passwd = values['-PW-']
            hostname = values['-HName-']

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

        # This will close window 2 if logout.
        elif window == window2 and event == 'Logout':
            window2.close()
            window2 = None
            window1.un_hide()

        # This will forcibly close window 2 if the user clicks X.
        elif window == window2 and event == py_sg.WIN_CLOSED:
            window2.close()
            window2 = None
            window1.un_hide()

        # Check the tab events.
        #elif window == window2 and event == 'TAB1':
        

    # Close window 1. 
    window1.close()


# Run main program.
if __name__ == '__main__':
    main()

