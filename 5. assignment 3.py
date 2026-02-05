username_true = "python"
password_true = "rules"
wrong = 0
while wrong < 5:
    username = input("Enter a username:")
    password = input("Enter a password:")
    if username == username_true and password == password_true:
        print("Welcome")
        break
    else:
        wrong += 1
        print("wrong")
if wrong == 5:
    print("Access denied")