import os


def read_file(todo_file):
    """ Read a text file and returns the list
    of to-do items.
    """
    try:
        with open(todo_file, "r") as file:
            todos = file.readlines()
    except:
        todos = ["Your todo list is empty"]
    return todos


def get_todo_file_path():
    """
    :return: The file path of a text file
    """
    file_path = os.path.abspath(__file__)
    dir_path = os.path.dirname(file_path)
    return os.path.join(dir_path, 'todos.txt')


def add_todo(new_todo, todo_file):
    """
    Reads a text file and adds a new to-do in the text file

    :param new_todo: The to-do to be added
    :param todo_file:To-do text file
    :return: A Text file with the added to-do item.
    """
    with open(todo_file, "a") as file:
        file.write(new_todo + "\n")


def show_todo(todo_file):
    """
    Displays the to-do items in a text file.
    :param todo_file: To-do text file.
    :return: None
    """
    try:
        todos = read_file(todo_file)
        for index, item in enumerate(todos, start=1):
            print(f"{index}- {item.strip()}")
        if not todos:
            print("Your todo list is empty, start adding items now")
    except FileNotFoundError:
        print("Your todo list is empty, start adding items now")


def edit_todo(old_todo, new_todo, todo_file):
    """
    Edits to-do item in a text file
    :param old_todo: to-do item to be edited.
    :param todo_file: To-do text file.
    :return: A new text file with the edited to-do item.
    """
    todos = read_file(todo_file)
    try:
        old_todo_index = todos.index(old_todo)
        todos[old_todo_index] = new_todo + "\n"
        with open(todo_file, "w") as file:
            file.writelines(todos)
    except ValueError:
        try:
            todo_index = int(old_todo) - 1
            if 0 <= todo_index < len(todos):
                todos[todo_index] = new_todo + "\n"
                with open(todo_file, "w") as file:
                    file.writelines(todos)
            else:
                print(f"Invalid index. Please provide a number in the range 1-{len(todos)}.")
        except ValueError:
            print("Todo not found.")


def complete_todo(completed_todo, todo_file):
    """
    Removes a completed to-do item from a text file
    :param completed_todo: completed item to be removed.
    :param todo_file: To-do text file.
    :return: A new text file without the completed to-do item.
    """
    try:
        completed_todo_index = int(completed_todo) - 1
        todos = read_file(todo_file)
        if 0 <= completed_todo_index < len(todos):
            todo_to_remove = todos.pop(completed_todo_index).strip()
            with open(todo_file, "w") as file:
                file.writelines(todos)
        else:
            print("Invalid item number.")
    except ValueError:
        todos = read_file(todo_file)
        stripped_todos = [todo.strip() for todo in todos]
        completed_todo = completed_todo.strip()
        if completed_todo in stripped_todos:
            stripped_todos.remove(completed_todo)
            todos = [f"{todo}\n" for todo in stripped_todos]
            with open(todo_file, "w") as file:
                file.writelines(todos)
        else:
            print("Invalid input")


if __name__ == "__main__":
    print("hello world")
