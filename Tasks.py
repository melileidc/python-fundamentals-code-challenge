# File: assessment.py

# Function to add two numbers
def add_numbers(num1, num2):
    return num1 + num2

# Function to check if a number is even
def is_even(number):
    return number % 2 == 0

# Function to reverse a string
def reverse_string(text):
    return text[::-1]

# Function to count the number of vowels in a string
def count_vowels(text):
    text = text.lower()
    vowels = 'aeiou'
    return sum(1 for char in text if char in vowels)

# Function to calculate the factorial of a non-negative integer
def calculate_factorial(n):
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Decorator function that prints a message before calling the original function
def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

# Function to apply the decorator to a function
def apply_decorator(func):
    return decorator_func(func)

# Function to sort a list of tuples by age
def sort_by_age(list_of_tuples):
    return sorted(list_of_tuples, key=lambda x: x[1])

# Function to merge two dictionaries, summing values for common keys
def merge_dicts(dict1, dict2):
    merged_dict = {}
    for key, value in dict1.items():
        merged_dict[key] = value
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict

# Class definition for Car
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

# Example usage of the functions and class

if __name__ == "__main__":
    # Test add_numbers
    print("add_numbers(5, 2):", add_numbers(5, 2))  # Output: 7

    # Test is_even
    print("is_even(4):", is_even(4))  # Desired Output: True
    print("is_even(7):", is_even(7))  #Desired Output: False

    # Test reverse_string
    print("reverse_string('hello'):", reverse_string("hello"))  # Output: 'olleh'

    # Test count_vowels
    print("count_vowels('Hello World'):", count_vowels("Hello World"))  # Output: 3

    # Test calculate_factorial
    print("calculate_factorial(5):", calculate_factorial(5))  # Output: 120

    # Test apply_decorator
    @apply_decorator
    def my_function():
        print("Function Called")

    my_function()  # Output: "Decorator Applied" followed by "Function Called"

    # Test sort_by_age
    people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
    print("sort_by_age(people):", sort_by_age(people))  # Output: [('Bob', 25), ('Alice', 30), ('Charlie', 35)]

    # Test merge_dicts
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    print("merge_dicts(dict1, dict2):", merge_dicts(dict1, dict2))  # Output: {'a': 1, 'b': 5, 'c': 4}

    # Test Car class
    my_car = Car("Toyota", "Corolla", 2020)
    print("Car Info:")
    my_car.display_info()
    # Desired Output:
    # Make: Toyota
    # Model: Corolla
    # Year: 2020
