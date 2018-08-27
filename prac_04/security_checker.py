usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username_attempt = input("Please enter your username: ")
for username in usernames:
    if username == username_attempt:
        result = "Access Granted"
        break
    else:
        result = "Access Denied"
print(result)
