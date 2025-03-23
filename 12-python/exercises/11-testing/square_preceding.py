"""
Main module to be tested.
"""


def square_preceding(values):
    """ (list of number) -> NoneType
    
    Replace each item in the list with square the value of the
    preceding item, and replace the first item with 0.

    >>> L = [1, 2, 3]
    >>> square_preceding(L)
    >>> L
    [0, 1, 4]
    """
    # Save value of list index 0 in variable
    # and set to 0
    temp = values[0]
    values[0] = 0
    # Loop through the given list, limiting the start index to 1
    # with the range(1) built-in and limiting the end with the len(values)
    # built in (length of the list).
    for index in range(1, len(values)):
        values[index] = temp ** 2
        temp = values[index]

    return values

squares = square_preceding([2, 0, 6, 15])
print(squares)