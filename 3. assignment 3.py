largest_number = None
lowest_number = None
while True:
    number = input("Enter a number: ")
    if number == "":
        break
    number = float(number)
    if lowest_number is None or number < lowest_number:
        lowest_number = number
    if largest_number is None or number > largest_number:
        largest_number = number
if lowest_number is not None:
    print("largest number:", largest_number)
    print("lowest number:", lowest_number)
else:
    print("pls enter a number.")