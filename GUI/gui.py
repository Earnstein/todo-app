from CLI.todo_functions import get_todo_file_path, add_todo, show_todo, edit_todo, complete_todo
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App",
                   layout=[[label], [input_box, add_button]],
                   font=("Poppins", 16))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos_file = get_todo_file_path()
            new_todo = values["todo"]
            add_todo(new_todo, todos_file)
        case sg.WIN_CLOSED:
            break

window.close()