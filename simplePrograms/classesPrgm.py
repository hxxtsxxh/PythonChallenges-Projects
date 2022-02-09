# using classes
# make a dog class

class Dog:
    def __init__(self, name, age, color, breed):
        self.name = name
        self.age = age
        self.color = color
        self.breed = breed


    def bark(self):
        print(f'Hey I am {self.name} and a {self.breed} dog.')
        print(f'I am {self.age} years old!')
        print(f'I am of the color {self.color}')
        return ''


dog_one = Dog("Heet Shah", 15, "red", "Golden Retriever") #created object dog_one
dog_two = Dog("Joe Mama", 25, "brown", "Doodle") #created object dog_two
print(dog_one.bark())
print()
print(dog_two.bark())


