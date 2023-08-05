import PySimpleGUI as sg
import time
from CLI.todo_functions import read_file, get_todo_file_path, add_todo, edit_todo, complete_todo


TODO_FILE = get_todo_file_path()
BUTTON_PADDING = (5, 10)
THEME = "DarkGrey12"

sg.theme(THEME)
clock = sg.Text("", key="clock")
TODAY = time.strftime("%b %d, %Y %H:%M:%S")


label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="input_box")
add_button = sg.Button("Add", button_color="green", font=16, border_width=0, pad=BUTTON_PADDING)
list_box = sg.Listbox(values=read_file(TODO_FILE), key="listbox",
                      enable_events=True, size=(44, 10))

edit_button = sg.Button("Edit", font=16, border_width=0, pad=BUTTON_PADDING)
complete_button = sg.Button("Complete", font=16, border_width=0, pad=BUTTON_PADDING)
exit_button = sg.Button("Exit", button_color="red", font=16, border_width=0, pad=BUTTON_PADDING)

window = sg.Window("My To-Do App",
                   layout=[[clock], [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Poppins", 16))

while True:
    event, value = window.read(timeout=500)
    window["clock"].update(value=TODAY)
    match event:
        case "Add":
            new_todo = value["input_box"]
            if new_todo == "":
                sg.popup("Input field is empty")
            else:
                add_todo(new_todo, TODO_FILE)
                window['listbox'].update(values=read_file(TODO_FILE))
        case "Edit":
            try:
                todo_to_edit = value['listbox'][0]
                new_todo = value['input_box'].strip()
                edit_todo(todo_to_edit, new_todo, TODO_FILE)
                window["listbox"].update(values=read_file(TODO_FILE))
            except IndexError:
                sg.popup("Choose an item before proceeding", font=("Poppins", 16))
        case "Complete":
            try:
                todo_to_complete = value['listbox'][0].strip()
                complete_todo(todo_to_complete, TODO_FILE)
                window["listbox"].update(values=read_file(TODO_FILE))
                window["input_box"].update(value="")
            except IndexError:
                sg.popup("Choose an item before proceeding")
        case "listbox":
            value = value["listbox"][0].strip()
            window["input_box"].update(value=value)
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()
