text = input("Enter a string: ")
length = len(text)
mid = length // 2
if length % 2 == 0:
    print(text[mid - 1: mid + 1])
else:
    print(text[mid])