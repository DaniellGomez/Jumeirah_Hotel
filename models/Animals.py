from unicodedata import name


class Pet:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what I say")

class Cat(Pet):
    
    def __init__(self, name, age, color):
        super().__init__(name, age )
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color} ")

class Dog(Pet):
    def speak(self):
        print("Bark")


class Fish(Pet):
    pass

pet_1= Pet("Lara", 23)
pet_1.show()

cat_1 = Cat("Mush", 16, "White")
cat_1.show()
cat_1.speak()

dog_1 = Dog("Crispeta", 2)
dog_1.show()
dog_1.speak()

fish_1 = Fish("Jose", 2)
fish_1.speak()