import PySimpleGUI as py_sg

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

# This section modifies the window layout, text and buttons.
layout = [
    [py_sg.Text("Database Login")],
    [py_sg.Text("Enter name of database:"), py_sg.InputText(key='-DB-')],
    [py_sg.Text("Enter username:"), py_sg.InputText(key='-Uname-')],
    [py_sg.Text("Enter password:"), py_sg.Input(password_char='*', key='-PW-')],
    [py_sg.Button("Login"), py_sg.Button("Reset"), py_sg.Exit()]
    ]

# Creates the main window, with the layout as defined above.
window = py_sg.Window("Project Part 3", layout)

# Creates the event loop.
while True:
    event, values = window.read()
    
    # This ends the program if the user closes the window or presses the Exit button.
    if event in ('Exit', py_sg.WIN_CLOSED):
        break

    # This will save the values input in the login window.
    elif event == 'Login':
        db_name = values['-DB-']
        username = values['-Uname-']
        passwd = values['-PW-']

        # TEMP PRINT to make sure that we saved the input
        print(db_name, '\t', username, '\t' , passwd)

    # This resets the text just typed into the window.
    elif event == 'Reset':
        window['-DB-'].update('')
        window['-Uname-'].update('')
        window['-PW-'].update('')
        
    
# Close up the window.
window.close()



