#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__ (self, name="test", breed = "Corgi"):
        self.name = name
        self.breed = breed

    def get_name (self):
        return self._name
    
    def set_name (self, name):
        if name == "" or not isinstance(name, str) or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = name

    def set_breed (self, breed):
        if bool(breed not in APPROVED_BREEDS) == True:
            print("Breed must be in list of approved breeds.")
        else:
            self._breed = breed

    def get_breed (self):
        return self._breed
    
    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)

    # def __init__(self, name="", breed=""):
    #     if breed in APPROVED_BREEDS:
    #         print("Breed must be in list of approved breeds.")

    #     if name == "" or not isinstance(name, str) or len(name) > 25:
    #         print("Name must be string between 1 and 25 characters.")
    #     else:
    #         self.name = name

    #     self.breed = breed

    # def set_breed(self, breed):
    #     if breed not in APPROVED_BREEDS:
    #         print("Breed must be in list of approved breeds.")
    #     self.breed = breed

    

    # def set_na)me(self):
    #     if name == "":
    #         print("Name must be string between 1 and 25 characters.")
    #     else:
    #         self._name = name

    # breed = property(set_breed)


# cliff = Dog("hola")

# print(cliff)

