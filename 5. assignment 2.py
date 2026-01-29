import math

print("The first pizza")
diameter_one = float(input("enter the diameter of the pizza(cenimeter) "))
cost_one = float(input("enter the cost of the pizza(USD) "))
print("The second pizza")
diameter_two = float(input("enter the diameter of the pizza(cenimeter) "))
cost_two = float(input("enter the cost of the pizza(USD) "))
price_one = cost_one / ((((diameter_one / 100) / 2) ** 2) * math.pi)
price_two =cost_two / ((((diameter_two / 100) / 2) ** 2) * math.pi)
if price_one > price_two:
    print("The first pizza is better than the second pizza")
elif price_two > price_one:
    print("The second pizza is better than the first pizza")
else:
    print("both pizzas have the same value")

