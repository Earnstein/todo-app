import streamlit as st
from functions import read_file, get_todo_file_path, add_todo, edit_todo, complete_todo
todo_file = get_todo_file_path()
todos = read_file(todo_file)
todo_contents = [todo.strip() for todo in todos]
st.title("My Todo App")

for todo in todo_contents:
    if todo == "Your todo list is empty":
        st.write("Your todo list is empty, start adding to-dos")
    else:
        st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...")