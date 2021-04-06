secret_msg = "pyladies"
secret_msg_user = ""

#loops trough the user input until the right password is given 
while secret_msg_user != secret_msg:
    secret_msg_user = input("Input the password: ")
    if secret_msg_user == secret_msg:
        print("Hello, PyLady! Meeting is schedule on Tuesday at 6pm!")
    else:
        print("Hello, alien! Please, type the right password")


