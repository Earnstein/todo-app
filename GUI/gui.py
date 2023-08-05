from CLI.todo_functions import read_file, get_todo_file_path, add_todo, show_todo, edit_todo, complete_todo
import PySimpleGUI as sg

TODO_FILE = get_todo_file_path()

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="input_box")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=read_file(TODO_FILE), key="listbox",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")

window = sg.Window("My To-Do App",
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=("Poppins", 16))

while True:
    event, value = window.read()
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
        case "listbox":
            window["input_box"].update(value=value["listbox"][0])
        case sg.WIN_CLOSED:
            break

window.close()