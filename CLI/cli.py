from todo_functions import get_todo_file_path, add_todo, show_todo, edit_todo, complete_todo
import time

def main():
    """
    A program that runs a CLI to-do app
    """
    today = time.strftime("%b %d, %Y %H:%M:%S")
    print(f"Welcome today's date is {today}. ")
    todo_file = get_todo_file_path()
    while True:
        user_action = input("Type add, show, edit, complete, or exit: ").strip().lower()
        if user_action.startswith('add'):
            todo = user_action[4:].strip()
            add_todo(todo, todo_file)
        elif user_action.startswith("show"):
            show_todo(todo_file)
        elif user_action.startswith('edit'):
            todo = user_action[5:].strip()
            edit_todo(todo, todo_file)
        elif user_action.startswith("complete"):
            todo = user_action[9:].strip()
            complete_todo(todo, todo_file)
        elif user_action.startswith('exit'):
            break
        else:
            print("Command is not valid. The commands are add, show, edit, complete, or exit.")

    print('Bye!')


if __name__ == "__main__":
    main()
