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
    tab1_layout = [[sg.pin(sg.Button(f'{models[i]}', key=f'{i}', visible=True, enable_events=True)) for i in range(len(models))]]

    tab2_layout = [[sg.Text("Enter Scheduler System type:"), sg.InputText(key='-SS-'),
                    sg.Button('Search', bind_return_key=True)]]

    tab3_layout = [[sg.Text("Enter Serial Number:"), sg.InputText(key='-AddSN-')],
         [sg.Text("Enter Scheduler System type:"), sg.InputText(key='-AddSS-')],
         [sg.Text("Enter ModelNo Number:"), sg.InputText(key='-AddMN-'),sg.Button('Add Digital Display',enable_events=True)]]
    
    tab4_layout = [[sg.Text("Enter the Serial Number of the Digital Display to Delete:"), sg.InputText(key='-DEL-'),
                    sg.Button('Delete', bind_return_key=True)]]
    
    tab5_layout = [[sg.Text("Serial Number of Item to Update:"), sg.InputText(key='-S2Update-')],
                   [sg.Text("New Scheduler System"), sg.InputText(key='-SSys2Update-'), sg.Button('Update Scheduler System', bind_return_key=True)],
                   [sg.Text("New Model Number"), sg.InputText(key='-MN2Update-'), sg.Button('Update Model No.', bind_return_key=True)]]

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


# This method queries the database for model number information.
def print_model_info(mydb, mycursor, model_no):
    sql = "SELECT * FROM Model WHERE modelNo ='" + model_no + "';"
    mycursor.execute(sql)
    newresults = mycursor.fetchall()
    print(model_headings())
    print(tabulate(newresults))


# This method updates the Scheduler system given the serial number of a digital display. 
def update_scheduler(mydb, mycursor, serial_no, sched_sys):
    try:
        sql = "UPDATE DigitalDisplay SET schedulerSystem = '" + sched_sys + "' WHERE serialNo = '"+ serial_no + "';"
        mycursor.execute(sql)
        mydb.commit()
        print("The display has been updated.")
        print_displays(mycursor)
    except:
        print("The Digital Display could not be updated. Try again.")


# This method updates the model number given the serial number of a digital display. 
def update_modelNo(mydb, mycursor, serial_no, model_no):
    # First check if model number exists.
    sql = "SELECT modelNo FROM Model WHERE modelNo = '"+ model_no +"';"
    mycursor.execute(sql)
    model_res = mycursor.fetchall()

    if model_res == []:
        model_check = False
    else:
        model_check = True

    # If model number doesn't exist, then add it.
    if model_check == False:
        print("That model number does not exist yet. Add the model information first.")
        AddWidth = sg.popup_get_text('Width', 'Must be numbers')
        AddHeight = sg.popup_get_text('Height', 'Must be numbers')
        AddWeight = sg.popup_get_text('Weight', 'Must be numbers')
        AddDepth = sg.popup_get_text('Depth', 'Must be numbers')
        AddScreenS = sg.popup_get_text('Screen Size', 'Must be numbers')

        sql1= "INSERT INTO Model VALUES ('"+ model_no +"','" +AddWidth +"','"+ AddHeight +"','"+AddWeight+"','"+ AddDepth +"','"+ AddScreenS +"');"
        mycursor.execute(sql1)
        mydb.commit()

        sql2 = "UPDATE DigitalDisplay SET modelNo = '" + model_no + "' WHERE serialNo = '"+ serial_no + "';"
        mycursor.execute(sql2)
        mydb.commit()
        print("The Digital Display has been updated.")
        print_displays(mycursor)
    else:
        try:
            sql3 = "UPDATE DigitalDisplay SET modelNo = '" + model_no + "' WHERE serialNo = '"+ serial_no + "';"
            mycursor.execute(sql3)
            mydb.commit()
            print("The display has been updated.")
            print_displays(mycursor)
        except:
            print("The Digital Display could not be updated. Try again.")
        

def print_displays(mycursor):
    sql1= "SELECT * FROM DigitalDisplay;"
    mycursor.execute(sql1)
    myresults=mycursor.fetchall()
    print("\n")
    print(ddisplay_headings())
    print(tabulate(myresults))
    

# This method creates the table headings for the Digital Display table.
def ddisplay_headings():
    return "serialNo   schedulerSystem   modelNo"

# This method creates the table headings for the Model table.
def model_headings():
    return "\nmodelNo width height weight depth screenSize"
    

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
##            db_name ='abc_media_db'         # Only uncomment to hardcode the database login
##            username ='root'                # Only uncomment to hardcode the database login
##            passwd = '1moreyearofschool'    # Only uncomment to hardcode the database login
##            hostname ='localhost'           # Only uncomment to hardcode the database login
            db_name = values['-DB-']
            username = values['-Uname-']
            passwd = values['-PW-']
            hostname = values['-HName-']
            
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
        serialNos = []
        for i in range(len(answer1)):
            models.append(answer1[i][2])
        for j in range(len(answer1)):
            serialNos.append(answer1[j][0])
        
        # Checks the event for Tab 1: Show all digital displays.
        if window == window2 and get_current_key(window) == '-TAB1-':
            set_old_key(get_current_key(window))
            window.Refresh()
            sg.read_all_windows(timeout=50)
            print(ddisplay_headings())
            print(tabulate(answer1))

            if event == '0':
                model_no = models[0]
                print_model_info(mydb, mycursor, model_no)
                window.Refresh()
            elif event == '1':
                model_no = models[1]
                print_model_info(mydb, mycursor, model_no)
                window.Refresh()
            elif event == '2':
                model_no = models[2]
                print_model_info(mydb, mycursor, model_no)
                window.Refresh()
            elif event == '3':
                model_no = models[3]
                print_model_info(mydb, mycursor, model_no)
                window.Refresh()
            elif event == '4':
                model_no = models[4]
                print_model_info(mydb, mycursor, model_no)
                window.Refresh()
            elif event == '5':
                model_no = models[5]
                print_model_info(mydb, mycursor, model_no)
                window.Refresh()
            elif event == '6':
                model_no = models[6]
                print_model_info(mydb, mycursor, model_no)
                window.Refresh()
            elif event == '7':
                model_no = models[7]
                print_model_info(mydb, mycursor, model_no)
                window.Refresh()
            elif event == '8':
                model_no = models[8]
                print_model_info(mydb, mycursor, model_no)
                window.Refresh()
            elif event == '9':
                model_no = models[9]
                print_model_info(mydb, mycursor, model_no)
                window.Refresh()
            elif event == '10':
                model_no = models[10]
                print_model_info(mydb, mycursor, model_no)
                window.Refresh() 


        # Check Tab2 event.
        elif window == window2 and get_current_key(window) == '-TAB2-' and event== 'Search':
            set_old_key(get_current_key(window))
            SchedulerSystem = values['-SS-']
            sql1 = "SELECT * FROM DigitalDisplay WHERE schedulerSystem = '"+ SchedulerSystem + "';"
            mycursor.execute(sql1)
            myresults=mycursor.fetchall()
            print("\n")
            print(ddisplay_headings())
            print(tabulate(myresults))
             

        # Check the tab event add (TAB 3).
        elif window == window2 and get_current_key(window) == '-TAB3-' and event == 'Add Digital Display':
            set_old_key(get_current_key(window))
            window.Refresh()
            AddSerialNumber = values['-AddSN-']
            AddSchedulerSystem = values['-AddSS-']
            AddModelNumber = values['-AddMN-']

            sql1= "SELECT serialNo FROM DigitalDisplay WHERE serialNo = '"+ AddSerialNumber +"';"
            mycursor.execute(sql1)
            search_res=mycursor.fetchall()

            #check to see if display (by serial number) was found, or returned empty.
            if search_res == []:
                serial_check = False
            else:
                serial_check = True

            # Now check if model number exists.
            sql2 = "SELECT modelNo FROM Model WHERE modelNo = '"+ AddModelNumber +"';"
            mycursor.execute(sql2)
            model_res = mycursor.fetchall()

            if model_res == []:
                model_check = False
            else:
                model_check = True

            # If model number doesn't exist either, then add it.
            if serial_check == False and model_check == False:
                print("Model number was not found, add the model information first.")
                AddWidth = sg.popup_get_text('Width', 'Must be numbers')
                AddHeight = sg.popup_get_text('Height', 'Must be numbers')
                AddWeight = sg.popup_get_text('Weight', 'Must be numbers')
                AddDepth = sg.popup_get_text('Depth', 'Must be numbers')
                AddScreenS = sg.popup_get_text('Screen Size', 'Must be numbers')
                try:
                    sql3= "INSERT INTO Model VALUES ('"+AddModelNumber+"','"+AddWidth+"','"+AddHeight+"','"+AddWeight+"','"+AddDepth+"','"+AddScreenS+"');"
                    mycursor.execute(sql3)
                    mydb.commit()
                    print("Model added, the Digital Display will now be added.")
                except:
                    print("Could not add model info.")
                    print("Try again.") 

                sql4 = "INSERT INTO DigitalDisplay VALUES ('"+AddSerialNumber+"','"+AddSchedulerSystem+"','"+AddModelNumber+"');"
                mycursor.execute(sql4)
                mydb.commit()
                print("Digital Display added.")
                print_displays(mycursor)
                    
            elif serial_check == False and model_check == True:
                print("That model number already exists. Only the Digital Display with a different serial number will be added.")
                sql5 = "INSERT INTO DigitalDisplay VALUES ('"+AddSerialNumber+"','"+AddSchedulerSystem+"','"+AddModelNumber+"');"
                mycursor.execute(sql5)
                mydb.commit()
                print("Digital Display added.")
                print("\n")
                print_displays(mycursor)

            elif serial_check == True and model_check == True:
                print("That Digital Display already exists in the database. Nothing will be added.")
                print_displays(mycursor)


        elif window == window2 and get_current_key(window) == '-TAB4-' and event == 'Delete':
            set_old_key(get_current_key(window))
            print_displays(mycursor)

            del_serialNo = values['-DEL-']
            #First check if the serial number exists in the database.
            sql1 = "SELECT * FROM DigitalDisplay WHERE serialNo = '"+ del_serialNo +"';"
            mycursor.execute(sql1)
            answer = mycursor.fetchall()
            
            # If display not in database, do nothing.
            if answer == []:
                print("That Digital Display does not exist in the database. \nTry again.")
            # Delete the display.
            else:
                model_no = answer[0][2]
                sql2 = "DELETE FROM DigitalDisplay WHERE serialNo = '" + del_serialNo + "';"
                mycursor.execute(sql2)
                mydb.commit()
                print("The Digital Display has been deleted.")

                # Find out if that is the last model number in that digital display table.
                sql3 = "SELECT serialNo, modelNo FROM DigitalDisplay WHERE modelNo = '"+ model_no +"';"
                mycursor.execute(sql3)
                answer2 = mycursor.fetchall()

                # If that is the last model number, delete it from Model numbers.
                if answer2 == []:
                    sql4 = "DELETE FROM Model WHERE modelNo = '" + model_no + "';"
                    mycursor.execute(sql4)
                    mydb.commit()
                    print_displays(mycursor)
                    print("The Model Number: " + model_no + " has also been deleted.")
                else:
                    print("There is one more display remaning with that model number.")
                    print_displays(mycursor)
                
                        
        elif window == window2 and get_current_key(window) == '-TAB5-':
            if event == 'Update Scheduler System':
                serial_no = values['-S2Update-']
                sched_sys = values['-SSys2Update-']
                update_scheduler(mydb, mycursor, serial_no, sched_sys)
                
            elif event == 'Update Model No.':
                serial_no = values['-S2Update-']
                model_no = values['-MN2Update-']
                update_modelNo(mydb, mycursor, serial_no, model_no)
    
            else:
                set_old_key(get_current_key(window))
                window.Refresh()
                sg.read_all_windows(timeout=50)
                # Make sure the displays are printed
                print('Current existing Digital Displays:')
                print_displays(mycursor)

            
    # Finish the program by closing the window.
    window.close()
    

# Run main program.
if __name__ == '__main__':
    main()

