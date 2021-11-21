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
def make_dbwin(db_name, username, passwd, hostname):

    # I need a preliminary database connection to get answers for Tab 1.
    db_conn = database_conn(db_name, username, passwd, hostname)
    # Also need a cursor to get database information.
    cursor1 = db_conn.cursor(buffered=True)
    # Get all the digital displays information:
    sql_1 = "SELECT * FROM DigitalDisplay;"
    cursor1.execute(sql_1)
    answer = cursor1.fetchall()
    models = []
    for i in range (len(answer)):
        models.append(answer[i][2])

    # We will create the menu tabs to put into the window first.
    tab1_layout = [[sg.pin(sg.Button(f'{models[i]}', key=f'-{i}-', visible=False, enable_events=True)) for i in range(len(models))]]

    tab2_layout = [[sg.Text("Enter Scheduler System type:"), sg.InputText(key='-SS-'),
                    sg.Button('Search', bind_return_key=True)]]

    tab3_layout = [[sg.Text("Enter Serial Number:"), sg.InputText(key='-AddSN-')],
         [sg.Text("Enter Scheduler System type:"), sg.InputText(key='-AddSS-')],
         [sg.Text("Enter ModelNo Number:"), sg.InputText(key='-AddMN-'),sg.Button('Add Digital Display')],
                   ]
    

    tab4_layout = []
    
    tab5_layout = []

    tab_group = sg.TabGroup([[sg.Tab('1. Show Digital Displays', tab1_layout, key= '-TAB1-'),
                          sg.Tab('2. Search Digital Displays', tab2_layout, key= '-TAB2-'),
                          sg.Tab('3. Insert a Digital Display', tab3_layout, key= '-TAB3-'),
                          sg.Tab('4. Delete a Digital Display', tab4_layout, key= '-TAB4-'),
                          sg.Tab('5. Update a Digital Display', tab5_layout, key= '-TAB5-')]], enable_events=True, key = '-TABGROUP-')
    
    layout = [[tab_group],
              [sg.Output(size=(120,30), key = '-Output-')],
              [sg.Button('Logout'), sg.Button('Clear')]]

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

# dont change this value, unexpected behavior
old_tab_key = '-TAB0-'

def is_old_key(compKey):
    return True if compKey == old_tab_key else False

def set_old_key(key):
    global old_tab_key
    old_tab_key = key

def get_old_key():
    return old_tab_key

def get_current_key(window):
    return window.Element('-TABGROUP-').Get()


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
            db_name ='abc_media_db'         # delete after debugging
            username ='root'                # delete after debugging
            passwd = '1moreyearofschool'    # delete after debugging
            hostname ='localhost'           # delete after debugging
##            db_name = values['-DB']
##            username = values['-Uname-']
##            passwd = values['-PW-']
##            hostname = values['-HName-']
            
            # Hide login window to stop interaction with it.
            window1.hide()
            # Create the database interaction window.
            window2 = make_dbwin(db_name, username, passwd, hostname)

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
            window1.Finalize()
            window1.un_hide()

        elif window == window2 and event == 'Clear':
            window['-Output-'].Update('')

        # This will forcibly close window 2 if the user clicks X.
        elif window == window2 and event == sg.WIN_CLOSED:
            window2.close()
            window2 = None
            window1.Finalize()
            window1.un_hide()

        # This small section sets up Tab 1 so that we can display all Digital Displays info
        # and also display all the information about a specific model upon clicking that model
        # number button.
        sql1 = "SELECT * FROM DigitalDisplay;"
        mycursor.execute(sql1)
        answer1 = mycursor.fetchall()
        models = []
        for i in range(len(answer1)):
            models.append(answer1[i][2])

        # Checks the event for Tab 1: Show all digital displays.
        if window == window2 and get_current_key(window) == '-TAB1-' and not is_old_key(get_current_key(window)):
            set_old_key(get_current_key(window))
            print(table_headings())
            print(tabulate(answer1))
            for j in range(len(answer1)):
                window[f'-{j}-'].update(visible=True)
            window.Refresh()
            sg.read_all_windows(timeout=1000)

        if window == window2 and get_current_key(window) == '-TAB2-' and not is_old_key(get_current_key(window)):
            set_old_key(get_current_key(window))

        if window == window2 and get_current_key(window) == '-TAB3-' and not is_old_key(get_current_key(window)):
            set_old_key(get_current_key(window))

        if window == window2 and get_current_key(window) == '-TAB4-' and not is_old_key(get_current_key(window)):
            set_old_key(get_current_key(window))

        if window == window2 and get_current_key(window) == '-TAB5-' and not is_old_key(get_current_key(window)):
            set_old_key(get_current_key(window))

    
        # Checks Tab 1 subevents (the model number buttons).      
        elif window == window2 and event == '-0-':
            print("Button -0- works.")
##            model_num = VH356693
##            print(model_num)
##            sql2 = "SELECT * FROM Model WHERE modelNo = '" + model_num + "';"
##            newresults = mycursor.fetchall()
##            print(table_headings())
##            print(tabulate(newresults))

        elif window == window2 and event == '-1-':
            print("Button -1- works.")

        elif window == window2 and event == '-2-':
            print("Button -2- works.")

        elif window == window2 and event == '-3-':
            print("Button -3- works.")

        elif window == window2 and event == '-4-':
            print("Button -4- works.")     

        # Check Tab2 event.
        elif window == window2 and event == 'Search':
             SchedulerSystem = values['-SS-']
             sql1 = "SELECT * FROM DigitalDisplay WHERE schedulerSystem = '"+ SchedulerSystem + "';"
             mycursor.execute(sql1)
             myresults=mycursor.fetchall()
             print(table_headings())
             print(tabulate(myresults))

        # check the tab event add.
        elif window == window2 and event == 'Add Digital Display':
            AddSerialNumber = values['-AddSN-']
            AddSchedulerSystem = values['-AddSS-']
            AddModelNumber = values['-AddMN-']
            check=True
            sql1= "SELECT modelNo FROM Model WHERE modelNo = '"+AddModelNumber+"';"
            #print(sql1)
            mycursor.execute(sql1)
            search_res=mycursor.fetchall()
            test=[] 
            if search_res ==test:
                check=False
            #print(table_headings())
            #print(tabulate(search_res))

            sql2 = "SELECT modelNo FROM Model WHERE modelNo = '"+AddModelNumber+"';"
            #print(sql2)
            mycursor.execute(sql2)
            search_res=mycursor.fetchall()
            test=[] 
            if search_res ==test:#check to see if model was not found and returned empty.
                check=False
            print(search_res)


            try:
                sql= "INSERT INTO DigitalDisplay VALUES ('"+AddSerialNumber+"','"+AddSchedulerSystem+"','"+AddModelNumber+"');"
                #sql= "INSERT INTO DigitalDisplay VALUES ('serial2','random','VH356693');"
                mycursor.execute(sql)
                mydb.commit()
                check==True
            except:
               #insert code for new window asking for model data to be added.
                if check==False:
                     print("Could not insert Digital display because modelno not found, add model info")
                     
                     AddWidth = sg.popup_get_text('Width', 'input the width')
                     AddHeight = sg.popup_get_text('Height', 'input the heigth')
                     AddWeight = sg.popup_get_text('Weight', 'input the weight')
                     AddDepth = sg.popup_get_text('Depth', 'input the depth')
                     AddScreenS = sg.popup_get_text('Screen Size', 'input the screen size')
                     
                     sql= "INSERT INTO Model VALUES ('"+AddModelNumber+"','"+AddWidth+"','"+AddHeight+"','"+AddWeight+"','"+AddDepth+"','"+AddScreenS+"');"
                     mycursor.execute(sql)
                     mydb.commit()
                     print("Model added, you can now add the Digital display")

                     
                     
            finally:
                if check==True:
                    print("Digital Display added")
            sql1= "SELECT * FROM DigitalDisplay;"    
            mycursor.execute(sql1)
            myresults=mycursor.fetchall()
            print(table_headings())
            print(tabulate(myresults))


    # Finish the program by closing the window.
    window.close()
    

# Run main program.
if __name__ == '__main__':
    main()

