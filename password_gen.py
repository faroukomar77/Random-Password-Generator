import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

result = ""
while nr_letters > 0 or nr_symbols > 0 or nr_numbers > 0:
    random_number = random.randint(1, 3)
    if random_number == 1 and nr_letters > 0:
        random_num = random.randint(0, len(letters) - 1)
        result += letters[random_num]
        nr_letters -= 1
    elif random_number == 2 and nr_symbols > 0:
        random_num = random.randint(0, len(symbols) - 1)
        result += symbols[random_num]
        nr_symbols -= 1
    elif random_number == 3 and nr_numbers > 0:
        random_num = random.randint(0, len(numbers) - 1)
        result += numbers[random_num]
        nr_numbers -= 1

print(result)
