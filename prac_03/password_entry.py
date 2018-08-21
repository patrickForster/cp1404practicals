# password checker
MIN_LENGTH = 4


def main():
    print("Please enter a valid password")
    print("Your password must be at least", MIN_LENGTH, "characters long")
    password = get_password(MIN_LENGTH)
    print_password(password)


def get_password(min_length):
    password = input("> ")
    while len(password) < min_length:
        print("Not enough characters!")
        password = input("> ")
    return password


def print_password(password):
    hidden_password = len(password) * '*'
    print(hidden_password)


main()
