Overview :-

This project is a simple String Calculator that adds numbers from a string input. It follows the principles of Test-Driven Development (TDD) and can handle various formats of input.

Features :-

Basic Addition:

Returns 0 for an empty string.
Returns the integer value for a single number.
Sums multiple numbers separated by commas.

New Line Support:-

Supports new lines as delimiters (e.g., "1\n2,3" returns 6).
Custom Delimiters:

Allows custom delimiters specified in the input (e.g., "//;\n1;2" returns 3).

Error Handling:-

Raises an error for negative numbers, showing all negatives in the message.

How It Works:-

The main method is add, which takes a string and returns the sum of the numbers.
It checks for empty strings, splits numbers by commas or new lines, and handles custom delimiters.
If there are negative numbers, it raises a ValueError.


Examples:-
Here are some examples of how to use the add method:

python
Copy code
add("")                 # Returns 0
add("1")                # Returns 1
add("1,5")             # Returns 6
add("1\n2,3")          # Returns 6
add("//;\n1;2")        # Returns 3
add("1,-2,3,-4")       # Raises ValueError

Conclusion:-

The String Calculator project demonstrates a working solution for adding numbers from a string while handling various input formats and errors.

