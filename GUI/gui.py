from CLI.todo_functions import read_file, get_todo_file_path, add_todo, edit_todo, complete_todo
import PySimpleGUI as sg

TODO_FILE = get_todo_file_path()

button_padding = (5, 10, 5, 10)
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="input_box")
add_button = sg.Button("Add", button_color="green", font=16, border_width=0, pad=button_padding)
list_box = sg.Listbox(values=read_file(TODO_FILE), key="listbox",
                      enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit", font=16, border_width=0, pad=button_padding)
complete_button = sg.Button("Complete", font=16, border_width=0, pad=button_padding)
exit_button = sg.Button("Exit", button_color="red", font=16, border_width=0, pad=button_padding)


window = sg.Window("My To-Do App",
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Poppins", 16), finalize=True,
                   background_color="lightgray")

while True:
    event, value = window.read()
    # helper print statements for window events and values
    print(1, window.read())
    print(2, event)
    print(3, value)
    match event:
        case "Add":
            new_todo = value["input_box"]
            add_todo(new_todo, TODO_FILE)
            window['listbox'].update(values=read_file(TODO_FILE))
        case "Edit":
            todo_to_edit = value['listbox'][0]
            new_todo = value['input_box'].strip()
            edit_todo(todo_to_edit, new_todo, TODO_FILE)
            window["listbox"].update(values=read_file(TODO_FILE))
        case "Complete":
            todo_to_complete = value['listbox'][0].strip()
            complete_todo(todo_to_complete, TODO_FILE)
            window["listbox"].update(values=read_file(TODO_FILE))
            window["input_box"].update(value="")
        case "listbox":
            value = value["listbox"][0].strip()
            window["input_box"].update(value=value)
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()