def reverse_string(input_string):
    """
    Reverse the given string.

    Parameters:
    input_string (str): The string to be reversed.

    Returns:
    str: The reversed string.
    """
    # Reverse the string using slicing
    reversed_string = input_string[::-1]

    reversed_string = f"The reversed string is: {reversed_string}\n\n.Executed using the reverse_string function."
    # print (f"DEBUG: reversed_string: {reversed_string}")
    return reversed_string

