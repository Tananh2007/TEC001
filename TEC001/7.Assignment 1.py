import random
code1 = "number_one"
for i in range(3):
    code1 += str(random.randint(0, 9))
code2 = "number_two"
for i in range(4):
    code2 += str(random.randint(1, 6))

print("3-digit code (0–9):", code1)
print("4-digit code (1–6):", code2)
