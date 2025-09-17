import random

value = random.uniform(1, 10)
print(value)

value = random.randint(1, 10)
print(value)


greetings = ['Hey', "bye", 'hello', 'good bye', 'ohh']

greet = random.choices(greetings)

print(greet)

list = list(range(1, 53))

random.shuffle(list)

print(list)