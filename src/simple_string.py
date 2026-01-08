from typing import Optional


"""
Simple String Operations Module

This module provides basic string manipulation functions for demonstration purposes.
"""


def concatenate(str1: str, str2: str) -> str:
    """
    Concatenate two strings together.
    
    Args:
        str1 (str): The first string
        str2 (str): The second string
    
    Returns:
        str: The concatenated string
    
    Example:
        >>> concatenate("Hello", "World")
        'HelloWorld'
    """
    return str1 + str2


def to_uppercase(text: str) -> str:
    """
    Convert a string to uppercase.
    
    Args:
        text (str): The string to convert
    
    Returns:
        str: The uppercase version of the string
    
    Example:
        >>> to_uppercase("hello")
        'HELLO'
    """
    return text.upper()


def to_lowercase(text: str) -> str:
    """
    Convert a string to lowercase.
    
    Args:
        text (str): The string to convert
    
    Returns:
        str: The lowercase version of the string
    
    Example:
        >>> to_lowercase("HELLO")
        'hello'
    """
    return text.lower()


def reverse_string(text: str) -> str:
    """
    Reverse a string.
    
    Args:
        text (str): The string to reverse
    
    Returns:
        str: The reversed string
    
    Example:
        >>> reverse_string("hello")
        'olleh'
    """
    return text[::-1]


def count_characters(text: str) -> int:
    """
    Count the number of characters in a string.
    
    Args:
        text (str): The string to count
    
    Returns:
        int: The number of characters
    
    Example:
        >>> count_characters("hello")
        5
    """
    return len(text)


def count_words(text: str) -> int:
    """
    Count the number of words in a string.
    
    Args:
        text (str): The string to count words in
    
    Returns:
        int: The number of words
    
    Example:
        >>> count_words("hello world")
        2
    """
    return len(text.split())


def replace_substring(text: str, old: str, new: str) -> str:
    """
    Replace all occurrences of a substring with a new substring.
    
    Args:
        text (str): The original string
        old (str): The substring to replace
        new (str): The replacement substring
    
    Returns:
        str: The string with replacements made
    
    Example:
        >>> replace_substring("hello world", "world", "Python")
        'hello Python'
    """
    return text.replace(old, new)


def split_string(text: str, delimiter: str = " ") -> list[str]:
    """
    Split a string into a list of substrings.
    
    Args:
        text (str): The string to split
        delimiter (str): The delimiter to split on (default: space)
    
    Returns:
        list[str]: A list of substrings
    
    Example:
        >>> split_string("hello,world", ",")
        ['hello', 'world']
    """
    return text.split(delimiter)


def join_strings(strings: list[str], separator: str = " ") -> str:
    """
    Join a list of strings with a separator.
    
    Args:
        strings (list[str]): The list of strings to join
        separator (str): The separator to use (default: space)
    
    Returns:
        str: The joined string
    
    Example:
        >>> join_strings(["hello", "world"], " ")
        'hello world'
    """
    return separator.join(strings)


def starts_with(text: str, prefix: str) -> bool:
    """
    Check if a string starts with a given prefix.
    
    Args:
        text (str): The string to check
        prefix (str): The prefix to look for
    
    Returns:
        bool: True if the string starts with the prefix, False otherwise
    
    Example:
        >>> starts_with("hello world", "hello")
        True
    """
    return text.startswith(prefix)


def ends_with(text: str, suffix: str) -> bool:
    """
    Check if a string ends with a given suffix.
    
    Args:
        text (str): The string to check
        suffix (str): The suffix to look for
    
    Returns:
        bool: True if the string ends with the suffix, False otherwise
    
    Example:
        >>> ends_with("hello world", "world")
        True
    """
    return text.endswith(suffix)


def contains_substring(text: str, substring: str) -> bool:
    """
    Check if a string contains a given substring.
    
    Args:
        text (str): The string to search in
        substring (str): The substring to look for
    
    Returns:
        bool: True if the substring is found, False otherwise
    
    Example:
        >>> contains_substring("hello world", "lo wo")
        True
    """
    return substring in text


def get_substring(text: str, start: int, end: Optional[int] = None) -> str:
    """
    Extract a substring from a string.
    
    Args:
        text (str): The original string
        start (int): The starting index
        end (int, optional): The ending index (default: None, goes to end)
    
    Returns:
        str: The extracted substring
    
    Example:
        >>> get_substring("hello world", 0, 5)
        'hello'
    """
    if end is None:
        return text[start:]
    return text[start:end]


def is_numeric(text: str) -> bool:
    """
    Check if a string contains only numeric characters.
    
    Args:
        text (str): The string to check
    
    Returns:
        bool: True if the string is numeric, False otherwise
    
    Example:
        >>> is_numeric("12345")
        True
    """
    return text.isdigit()


def is_alphabetic(text: str) -> bool:
    """
    Check if a string contains only alphabetic characters.
    
    Args:
        text (str): The string to check
    
    Returns:
        bool: True if the string is alphabetic, False otherwise
    
    Example:
        >>> is_alphabetic("hello")
        True
    """
    return text.isalpha()
