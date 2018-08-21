# password checker
def main():
    MIN_LENGTH = 4
    print("Please enter a valid password")
    print("Your password must be at least", MIN_LENGTH, "characters long")
    password = get_password()
    while len(password) < MIN_LENGTH:
        print("Not enough characters!")
        password = get_password()
    print(password_printer(password))


def get_password():
    password = input("> ")
    return password


def password_printer(password):
    hidden_password = len(password) * '*'
    return hidden_password


main()
