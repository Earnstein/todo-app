import streamlit as st
from functions import read_file, get_todo_file_path, add_todo, complete_todo

todo_file = get_todo_file_path()
todos = read_file(todo_file)
todo_contents = [todo.strip() for todo in todos]


def add_new_todo():
    todo = st.session_state["new_todo"].strip()
    add_todo(todo, todo_file)
    st.session_state["new_todo"] = ""


st.title("My Todo App")

for index, todo in enumerate(todo_contents):
    if todo == "Your todo add_new_todolist is empty":
        st.write("Your todo list is empty, start adding to-dos")
    else:
        checkbox = st.checkbox(todo, key=index)
        if checkbox:
            complete_todo(todo, todo_file)
            del st.session_state[index]
            st.experimental_rerun()


st.text_input(label="todo",
              label_visibility="hidden",
              placeholder="Add new todo...",
              key='new_todo',
              )
if st.session_state["new_todo"] == "":
    pass
else:
    st.button("add", on_click=add_new_todo, key="add_button")
