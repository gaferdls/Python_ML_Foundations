# --- Basic try-except block ---
print("--- Example 1: Basic ZeroDivisionError ---")

try:
    result = 10 / 0
    print(result) # this line will not be reached
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
print("Program continues after handling the error.")

print("\n--- Example 2: Handling a specific error (ValueError) ---")
user_input = "abc" #imagine this came from an user
try:
    num = int(user_input)
    print(f"Successfully converted to integer: {num}")
except ValueError:
    print("Error: Could not convert '{user_unput}' to an integer. Please enter a valid number.")

print("\n--- Example 3: Handling multiple specific errors ---")
data_list = [1, 2,'three', 4]
try:
    value = data_list[2] # Accessing an element
    result = int(value) / 0
    print(result)
except ValueError:
    print("Error: Could not convert '{value}' to an integer. Please enter a valid number.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except IndexError:
    print("Error: Index out of range!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print("\n--- Example 4: try-except=else-finally ---")
def divide_numbers(a,b):
    try:
        quotient = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    except TypeError:
        print("Error: Both input must be numbers.")
        return None
    else:
        print("Dvision successful")
        return quotient
    finally:
        print("Division attempt complete")

print(divide_numbers(10,2))
print("-" * 20)
print(divide_numbers(10,0))
print("-" * 20)
print(divide_numbers(10,'a'))
print("-" * 20)

print("\n--- Example 5: Raising custom exceptions ---")
def process_positive_number(num):
    if not isinstance(num, (int, float)):
        raise TypeError("Input must be a number.")
    if num < 0:
        raise ValueError("Input must be positive.")
    return f"Processed positive number: {num}"
try:
    print(process_positive_number(10))
    print(process_positive_number(0))
    print(process_positive_number(-3))
except ValueError as ve:
    print(f"Caught custom error: {ve}")
except TypeError as te:
    print(f"Caught custom error: {te}")

print("\nEnd of error handling examples.")