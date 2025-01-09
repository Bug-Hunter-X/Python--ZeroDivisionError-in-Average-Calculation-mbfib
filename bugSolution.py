def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    if len(numbers) == 0:
        return 0 # Handle ZeroDivisionError
    average = total / len(numbers)
    return average

# Example usage:
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

my_numbers_2 = []
average_empty_2 = calculate_average(my_numbers_2)
print(f"The average of an empty list is: {average_empty_2}") 