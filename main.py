import os


def gimme_shell():
    # RCE
    directory = input("Enter the directory to list: ")
    command = f"ls {directory}"  # Vulnerable to Command Injection
    os.system(command)


def gimme_files():
    # Directory Traversal
    user_input = input("Enter filename: ")
    with open(user_input, 'r') as file:
        content = file.read()


def gimme_sql():
    user_input = input("Enter your username: ")
    query = "SELECT * FROM users WHERE username = '" + user_input + "';"
    print(f"Your SQL command: {query}")


def main():
    gimme_shell()
    gimme_files()
    gimme_sql()


if __name__ == "__main__":
    main()
