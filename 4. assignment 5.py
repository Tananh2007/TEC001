def remove_odds(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers
original_list = [10, 11, 22, 140, 36, 67, 77]

new_list = remove_odds(original_list)

print("Original list:", original_list)
print("List without odd numbers:", new_list)