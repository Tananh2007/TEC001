import random
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0
    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours
cars = []
for i in range(1, 11):
    max_speed = random.randint(150, 200)
    cars.append(Car(f"ABC-{i}", max_speed))
while True:
    for car in cars:
        change = random.randint(-10, 15)
        car.accelerate(change)
        car.drive(1)
    if any(car.travelled_distance >= 10000 for car in cars):
        break
print(f"{'Reg Number':<10} {'Max Speed':<12} {'Speed':<10} {'Distance':<12}")
print("-" * 46)
for car in cars:
    print(f"{car.registration_number:<10} "
          f"{car.maximum_speed:<12} "
          f"{car.current_speed:<10} "
          f"{round(car.travelled_distance, 2):<12}")