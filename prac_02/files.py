NAME_FILE = "name.txt"
out_file = open(NAME_FILE, 'w')
name = input("Please enter your name: ")
print(name, file = out_file)
out_file.close()

read_file = open(NAME_FILE, 'r')
name = read_file.readline()
print("Your name is {}".format(name))
read_file.close()
