# Python Coding Assessment

## Overview

This repository contains solutions for a Python coding assessment focused on fundamental Python concepts. The implementation includes functions and a class designed to address specific tasks related to basic data structures, functions, decorators, sequences, sets, dictionaries, and object-oriented programming.

## Tasks and Implementations

### Functions

1. **`add_numbers(num1, num2)`**
   - **Description**: Returns the sum of two numbers.
   - **Example**: `add_numbers(5, 2)` returns `7`.

2. **`is_even(number)`**
   - **Description**: Returns `True` if the number is even, otherwise `False`.
   - **Example**: `is_even(4)` returns `True`.

3. **`reverse_string(text)`**
   - **Description**: Returns the reversed version of the input string.
   - **Example**: `reverse_string("hello")` returns `'olleh'`.

4. **`count_vowels(text)`**
   - **Description**: Counts the number of vowels (`a`, `e`, `i`, `o`, `u`) in the string, case insensitive.
   - **Example**: `count_vowels("Hello World")` returns `3`.

5. **`calculate_factorial(n)`**
   - **Description**: Returns the factorial of a non-negative integer `n`.
   - **Example**: `calculate_factorial(5)` returns `120`.

6. **`apply_decorator(func)`**
   - **Description**: Applies a decorator that prints "Decorator Applied" before calling the provided function.
   - **Usage**: Decorate a function using `@apply_decorator`.

7. **`sort_by_age(list_of_tuples)`**
   - **Description**: Sorts a list of tuples (name, age) by age in ascending order.
   - **Example**: `sort_by_age([("Alice", 30), ("Bob", 25), ("Charlie", 35)])` returns `[('Bob', 25), ('Alice', 30), ('Charlie', 35)]`.

8. **`merge_dicts(dict1, dict2)`**
   - **Description**: Merges two dictionaries. If keys are common, their values are summed.
   - **Example**: `merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4})` returns `{'a': 1, 'b': 5, 'c': 4}`.

### Class

**`Car`**

- **Description**: Represents a car with attributes for make, model, and year. Includes a method to display car information.
- **Methods**:
  - `__init__(self, make, model, year)`: Initializes a new car object.
  - `display_info(self)`: Prints the car's make, model, and year.

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone git@github.com:melileidc/python-fundamentals-code-challenge.git

how to run the code: python3 Tasks.py
