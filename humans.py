class Human():
    def __init__(self, name="None", age=43, weight=74):
        self.name = name
        self.age = age
        self.weight = weight

    def give_name(self):
        print(f"My name is {self.name}")

    def give_age(self):
        print(f"My name is {self.age}")

h = Human(
    "Jeff",
    32,
)
r = Human("Frank")

h.give_name()
r.give_name()

h.give_age()
r.give_age()