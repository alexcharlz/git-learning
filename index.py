from getpass import getpass

username = str(input("Enter your username: "))
password = getpass("Enter your Password: ")
if username == "gabriel" and password == "password":
    print("authenticated")
print("not authenticated")
print("exit..")
