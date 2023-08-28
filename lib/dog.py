#!/usr/bin/env python3
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
    def __init__(self, name=None, breed=None):
        self._name = None
        self._breed = None
        if name is not None:
            self.set_name(name)
        if breed is not None:
            self.set_breed(breed)    
            
            
    def set_name(self, name):
     if isinstance(name, str) and (1 <= len(name) <= 25):
        print(f"Setting name to {name}")
        self._name = name.title()
     else:
        print("Name must be string between 1 and 25 characters.")

    def get_name(self):
        return self._name
    
    name = property(get_name, set_name)
    
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            print(f"Setting breed to {breed}")
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")
            
    def get_breed(self):
        return self._breed
   
    breed = property(get_breed, set_breed)
