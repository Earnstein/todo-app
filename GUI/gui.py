from CLI.todo import get_todo_file_path, add_todo, show_todo, edit_todo, complete_todo
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")
window = sg.Window("My To-Do App", layout=[[label], [input_box, add_button]])
window.read()
window.close()