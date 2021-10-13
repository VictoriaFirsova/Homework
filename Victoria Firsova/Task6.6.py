"""Task 4.6. A singleton is a class that allows only a single instance of itself to be created and gives
access to that created instance. Implement singleton logic inside your custom class using a method
to initialize class instance."""


class Sun:
    __instance = None

    def __init__(self):
        if Sun.__instance:
            __instance = Sun.__instance

    @classmethod
    def inst(cls):
        if not cls.__instance:
            cls.__instance = Sun()
        return cls.__instance


# Example:

p = Sun.inst()
f = Sun.inst()
print(p is f)
# True