# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import random
slovar = 'abcdefghijklmnopqrstuvwxyz'

def generate_random_name():
    while True:
        yield f"{''.join(random.choice(slovar) for _ in range(random.randint(1, 15)))} {''.join(random.choice(slovar) for _ in range(random.randint(1, 15)))}"


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))