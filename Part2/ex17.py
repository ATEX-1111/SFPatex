import random

name = input("What is your name?\n")

adjectives = ["Happy", "Sad", "Beautiful", "Trendy", "Cunning"]
animals = ["Horse", "Rabbit", "Tiger", "Dog", "Cat", "Owl"]

adjective = random.choice(adjectives)
animal = random.choice(animals)
result = adjective + " " + animal

print(name +", "+"your codename is:",result)

number = random.randint(1, 99)
print("Your lucky number is:", number)
