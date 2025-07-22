def reverse_string(text: str) -> str:
    """
    Reverses the input string.

    Args:
        text (str): The string to reverse.

    Returns:
        str: The reversed string.
    """
    return text[::-1]


if __name__ == "__main__":
    user_input = input("Enter a string to reverse: ")
    reversed_text = reverse_string(user_input)
    print(f"Reversed string: {reversed_text}")
