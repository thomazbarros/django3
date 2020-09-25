class Dog:
    dogInfo = "Hey dogs are cool!"

    def bark(self, str):
        print("BARK!" + str)

mydog = Dog()
mydog.bark("Bark again.")
mydog.name = "Kenzo"
mydog.age = 10
print(mydog.name)
print(mydog.age)

Dog.dogInfo = "Hey there"
print(Dog.dogInfo)