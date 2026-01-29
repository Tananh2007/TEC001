size_limit = 42
length = float(input('Please enter a number: '))
if length >= size_limit:
      print (" Congratulations! Your fish have reached the required size ")
elif length < size_limit:
      centimeters = size_limit - length
      print (f"Your_fish_is_only: {centimeters}  centimeters short of its recommended size ")
      print (" please, return it to the lake ")
