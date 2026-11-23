from statistics import median, mode

# Function 1: Calculate the sum
def calculate_sum(numbers):
    return sum(numbers)


# Function 2: Calculate the mean (average)
def calculate_mean(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)


# Function 3: Calculate the median and mode
def calculate_median_mode(numbers):
    if len(numbers) == 0:
        return None, None

    med = median(numbers)

    # Handle multiple modes
    counts = {num: numbers.count(num) for num in set(numbers)}
    highest_count = max(counts.values())

    modes = [num for num, count in counts.items()
             if count == highest_count]

    if highest_count == 1:
        mod = "No mode"
    elif len(modes) == 1:
        mod = modes[0]
    else:
        mod = modes

    return med, mod


# Example usage
numbers = [2, 4, 4, 6, 8]

print("Numbers:", numbers)
print("Sum:", calculate_sum(numbers))
print("Mean:", calculate_mean(numbers))

median_value, mode_value = calculate_median_mode(numbers)

print("Median:", median_value)
print("Mode:", mode_value)
