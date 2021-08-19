def say_color(self):
    print(f"My color is {self.color}")

class Car:
    color = 0
    speed = 0

    def move(self, x, y):
        print(f"Moving to {x}, {y}")

    def say_color(self):
        print(f"My color is")


my_car1 = Car()
my_car1.move(10, 20)

my_car2 = Car()
my_car2.color = "Red"

my_car3 = Car()
my_car3.color = "Green"

my_car1.say_color()  # Car.say_color(my_car1)
my_car2.say_color()
my_car3.say_color()




