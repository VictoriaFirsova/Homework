"""Task 4.4. Create hierarchy out of birds. Implement 4 classes:

class Bird with an attribute name and methods fly and walk.
class FlyingBird with attributes name, ration, and with the same methods. ration must have default value.
Implement the method eat which will describe its typical ration.
class NonFlyingBird with same characteristics but which obviously without attribute fly.
Add same "eat" method but with other implementation regarding the swimming bird tastes.
class SuperBird which can do all of it: walk, fly, swim and eat. But be careful which "eat" method you inherit.
Implement str() function call for each class."""


class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print('any bird can fly')

    def walk(self):
        print('any bird can walk')

    def __str__(self):
        return f'{self.name} can walk and fly'


class FlyingBird(Bird):
    def __init__(self, name, ration='mouse'):
        super().__init__(name)
        self.ration = ration

    def fly(self):
        print(f'{self.name} can fly')

    def walk(self):
        print(f'{self.name} can walk')

    def eat(self):
        print(f'{self.name} typical ration is:{self.ration}')

    def __str__(self):
        return f'{self.name} can walk and fly'


class NonFlyingBird(Bird):
    def __init__(self, name, ration='flies'):
        super().__init__(name)
        self.ration = ration

    def swim(self):
        print(f'{self.name} can swim')

    def eat(self):
        print(f'{self.name} typical ration is:{self.ration}')

    def __str__(self):
        return f'{self.name} can swim'


class SuperBird(FlyingBird, NonFlyingBird):
    def __init__(self, name, ration='all'):
        super().__init__(name)
        self.ration = ration

    def walk(self):
        print(f'{self.name} can walk')

    def swim(self):
        print(f'{self.name} can swim')

    def fly(self):
        print(f'{self.name} can fly')

    def eat(self):
        print(f'{self.name} typical ration is:{self.ration}')

    def __str__(self):
        return f'{self.name} can walk, swim and fly'
# Example:


b = Bird("Any")
b.walk()
# "Any bird can walk"

p = NonFlyingBird("Penguin", "fish")
p.swim()
# "Penguin bird can swim"

p.eat()
# "It eats mostly fish"

c = FlyingBird("Canary")
print(str(c))
# "Canary can walk and fly"
c.eat()
# "It eats mostly grains"

s = SuperBird("Gull")
print(str(s))
# "Gull bird can walk, swim and fly"
s.eat()
# "It eats fish"
# Have a look at mro method of your last class.
