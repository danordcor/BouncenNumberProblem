"""Problem:

Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number;
for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525)
are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers
is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
"""


def is_increasing_number(number_as_list):
    """
    Check if a number is a increasing
    Args:
        number_as_list []: The number for check as a list
    Returns:
        True if no digit is exceeded by the digit to its left
    """
    return sorted(number_as_list) == number_as_list


def is_decreasing_number(number_as_list):
    """
    Check if a number is a decreasing
    Args:
        number_as_list []: The number for check as a list
    Returns:
        True if no digit is exceeded by the digit to its right
    """
    return sorted(number_as_list, reverse=True) == number_as_list


def is_bouncy_number(n):
    """
    Check if n is a bouncy number
    Args:
        n (int): Positive integer for check if is bounce number
    Returns:
        True if n is neither increasing nor decreasing.
    """
    number_as_list = list(str(n))
    return not (is_increasing_number(number_as_list) or is_decreasing_number(number_as_list))


def least_bouncy_number_of_proportion(proportion):
    """
    Iterate through numbers until the bouncy count is a proportion of the total count
    Args:
        proportion (int): Proportion (%) of bouncy numbers for which the least number will be obtained
    Returns:
        n: The least number for the proportion of bouncy numbers
    """
    n = 1  # Least number
    count = 0  # Counter bouncy numbers seen
    while (count * 100 / n) < proportion:
        n += 1
        count += bool(is_bouncy_number(n))
    return n


if __name__ == "__main__":
    print("Least number for which the proportion of bouncy numbers is exactly 99% is :",
          least_bouncy_number_of_proportion(99))
