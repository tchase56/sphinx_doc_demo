"""
Simple Arithmetic Operations Module

This module provides basic arithmetic functions for demonstration purposes.
"""
print("FooFooFooFooFooFooFooFooFooFooFooFooFooFooFooFooFooFooFooFooFooFooFooFooFooFooFooFooFooFooFooFooFooFooFooFooFooFooFooFooFooFooFooFooFooFooFooFooFooFooFoo")

if __name__ == "__main__":
    print("MainMainMainMainMainMainMainMainMainMainMainMainMainMainMainMainMainMainMainMainMainMainMainMainMainMainMainMainMainMainMainMainMainMainMainMainMainMainMainMainMainMainMainMainMainMain")


def add(a: float, b: float) -> float:
    """
    Add two numbers together.
    
    Args:
        a (float): The first number
        b (float): The second number
    
    Returns:
        float: The sum of a and b
    
    Example:
        >>> add(2, 3)
        5
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Subtract the second number from the first.
    
    Args:
        a (float): The number to subtract from
        b (float): The number to subtract
    
    Returns:
        float: The difference of a and b
    
    Example:
        >>> subtract(5, 3)
        2
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers together.
    
    Args:
        a (float): The first number
        b (float): The second number
    
    Returns:
        float: The product of a and b
    
    Example:
        >>> multiply(4, 5)
        20
    """
    print("TestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTest")
    return a * b


def divide(a: float, b: float) -> float:
    """
    Divide the first number by the second.
    
    Args:
        a (float): The dividend
        b (float): The divisor
    
    Returns:
        float: The quotient of a and b
    
    Raises:
        ValueError: If b is zero
    
    Example:
        >>> divide(10, 2)
        5.0
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a: float, b: float) -> float:
    """
    Raise the first number to the power of the second.
    
    Args:
        a (float): The base
        b (float): The exponent
    
    Returns:
        float: a raised to the power of b
    
    Example:
        >>> power(2, 3)
        8
    """
    return a ** b


def modulo(a: float, b: float) -> float:
    """
    Calculate the remainder of division.
    
    Args:
        a (float): The dividend
        b (float): The divisor
    
    Returns:
        float: The remainder of a divided by b
    
    Raises:
        ValueError: If b is zero
    
    Example:
        >>> modulo(10, 3)
        1
    """
    if b == 0:
        raise ValueError("Cannot calculate modulo with zero")
    return a % b


def floor_divide(a: float, b: float) -> int:
    """
    Perform floor division (integer division).
    
    Args:
        a (float): The dividend
        b (float): The divisor
    
    Returns:
        int: The floor quotient of a divided by b
    
    Raises:
        ValueError: If b is zero
    
    Example:
        >>> floor_divide(10, 3)
        3
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a // b


def absolute(a: float) -> float:
    """
    Get the absolute value of a number.
    
    Args:
        a (float): The number
    
    Returns:
        float: The absolute value of a
    
    Example:
        >>> absolute(-5)
        5
    """
    return abs(a)


def negate(a: float) -> float:
    """
    Negate a number (multiply by -1).
    
    Args:
        a (float): The number to negate
    
    Returns:
        float: The negated value of a
    
    Example:
        >>> negate(5)
        -5
    """
    return -a
