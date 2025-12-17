while True:
    pwd = input("Enter password: ")
    if pwd == "stop":
        print("Access granted. Loop terminated.")
        break
    else:
        print("Wrong password. Try again.")
