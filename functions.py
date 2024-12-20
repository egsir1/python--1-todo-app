FILE_PATH = "todos.txt"


def get_todos(filepath=FILE_PATH):
    """Read a text file and returm the list
    of to do items
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


# print(help(get_todos))


def write_todos(todos_arg, filepath=FILE_PATH):
    """Write the to do items list in the text file."""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


# if __name__ == "__main__":
#     print(get_todos())
