def second_maximum(numbers):
    if len(numbers) < 2:
        return None
    first_max = second_max = float('-inf')
    for number in numbers:
        if number > first_max:
            second_max = first_max
            first_max = number
        elif first_max > number > second_max:
            second_max = number
    return second_max

# Example usage
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("The second maximum number is:", second_maximum(numbers))