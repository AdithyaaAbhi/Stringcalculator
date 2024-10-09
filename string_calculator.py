def add(numbers):
    if numbers == "":
        return 0

    # Check for different delimiters
    delimiter = ","
    if numbers.startswith("//"):
        delimiter, numbers = parse_delimiter(numbers)

    # Replace newlines with the specified delimiter for splitting
    numbers = numbers.replace("\n", delimiter)
    
    # Split numbers by the specified delimiter
    number_list = split_numbers(numbers, delimiter)

    # Validate and calculate the sum
    return calculate_sum(number_list)

def parse_delimiter(numbers):
    delimiter_section, numbers = numbers.split("\n", 1)
    delimiter = delimiter_section[2:]  # Skip the "//"
    return delimiter, numbers

def split_numbers(numbers, delimiter=","):
    # Split numbers using the provided delimiter
    return numbers.split(delimiter)

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
