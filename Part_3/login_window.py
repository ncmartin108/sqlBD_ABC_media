import PySimpleGUI as py_sg

# Sets a theme.
py_sg.theme('LightBrown1')

# This section modifies the window layout, text and buttons.
layout = [
    [py_sg.Text("Database Login")],
    [py_sg.Text("Enter name of database:"), py_sg.InputText()],
    [py_sg.Text("Enter username:"), py_sg.InputText()],
    [py_sg.Text("Enter password:"), py_sg.InputText()],
    [py_sg.Button("Login"), py_sg.Button("Reset"), py_sg.Button("Exit")]
    ]

# Creates a window.
window = py_sg.Window("Project Part 3", layout)

# Creates the event loop.
while True:
    event, values = window.read()
    
    # This ends the program if the user closes the window or presses the Exit button.
    if event in ("Exit", py_sg.WIN_CLOSED):
        break

    # This will save the values input in the login window.
    #if event 
    
# Close up the window.
window.close()

