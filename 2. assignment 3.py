while True:
    inch = int(input("Enter a number: "))
    if inch < 0:
        break
    else:
         centimets = inch * 2.54
    print(f"{inch} inch = {centimets} centimets")