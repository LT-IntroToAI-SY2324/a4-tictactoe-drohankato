# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog:
    #functions that start with __ are not intender to be called directly 
    def __int__(self, fc ="", a = 0, w = 0.0, n = "") -> None:
        pass
    """Create an instance of the dog class and set attriutes"""
    self.fur_color = fc
    self.age = a
    self.weight = w
    self.name = n 
    self.fetch_count = 0 

    def __str__(self) -> str:
        s = "dogs name is" + self.name + "\n"
        s += "and their name is" + str(self.age) + ("\n")
        s += "and their fur color is" + self.fur_color + ("\n")
        return s
    
    def play_fetch(self, num_times)
        self.fetch_count += num_times

bergdog = dog("black", 7, 78.2, "logan")
ninadog = Dog("brown", 3, 100, "hobbes")

print(bergdog)
print(ninadog)

bergdog