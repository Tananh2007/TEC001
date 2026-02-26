numbers = []
while True:
    user_input = input("Enter a number (press Enter to quit): ")
    if user_input == "":
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Please enter a valid number.")
numbers.sort(reverse=True)
top_five = numbers[:5]
print("The five largest numbers in descending order are:")
for num in top_five:
    print(num)