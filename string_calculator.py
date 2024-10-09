def add(numbers):
    if numbers == "":
        return 0

    # Check for different delimiters
    if numbers.startswith("//"):
        delimiter, numbers = parse_delimiter(numbers)

    # Split numbers by delimiter (comma and newline)
    number_list = split_numbers(numbers)

    # Validate and calculate the sum
    return calculate_sum(number_list)

def parse_delimiter(numbers):
    delimiter_section, numbers = numbers.split("\n", 1)
    delimiter = delimiter_section[2:]  # Skip the "//"
    return delimiter, numbers

def split_numbers(numbers):
    import re
    # Split by comma and new line
    return re.split(r'[,\n]', numbers)

def calculate_sum(number_list):
    total = 0
    negatives = []

    for number in number_list:
        if number:  # Check if number is not an empty string
            try:
                num = int(number)  # Convert to integer
            except ValueError:
                raise ValueError(f"Invalid input: {number}")  # Raise error for non-integer input

            if num < 0:
                negatives.append(num)
            total += num

    if negatives:
        raise ValueError(f"negative numbers not allowed: {', '.join(map(str, negatives))}")
    
    return total
