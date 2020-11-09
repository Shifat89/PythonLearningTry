age = 'John'
name = 90

print('My name is', name, 'and my age is', age)

numbers = [1, 2, 3, 4, 5]
numbers.pop()
numbers.remove(1)
print(numbers)

def print_square_value(numbers):
    for number in numbers:
        if number != 2:
            squared = number * number
            print(squared)

numbers = [1, 2, 3, 4]

print_square_value(numbers)