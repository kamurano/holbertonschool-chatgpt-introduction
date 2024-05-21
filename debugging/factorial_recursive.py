#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number recursively.

    Function Description:
    ---------------------
    This function calculates the factorial of a given non-negative integer using recursion.
    The factorial of a number n is the product of all positive integers less than or equal to n.

    Parameters:
    -----------
    n : int
        The number whose factorial is to be calculated.

    Returns:
    --------
    int
        The factorial of the input number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get the input argument from the command line
f = factorial(int(sys.argv[1]))
# Print the factorial
print(f)

