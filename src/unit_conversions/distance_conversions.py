"""
Distance Conversion Module

This module provides functions for converting between common distance units.
All conversions use helper functions from simple_arithmetic for calculations.
"""

from helper_functions.simple_arithmetic import multiply


# Conversion factors
M_TO_KM = 0.001
KM_TO_M = 1000.0
M_TO_CM = 100.0
CM_TO_M = 0.01
MI_TO_FT = 5280.0
FT_TO_MI = 1 / 5280.0
FT_TO_IN = 12.0
IN_TO_FT = 1 / 12.0
M_TO_FT = 3.28084
FT_TO_M = 0.3048
KM_TO_MI = 0.621371
MI_TO_KM = 1.60934


def _validate_distance(value: float, unit: str) -> None:
    """
    Validate that a distance value is non-negative.
    
    Args:
        value (float): The distance value to validate
        unit (str): The unit name for error messaging
    
    Raises:
        ValueError: If the value is negative
    """
    if value < 0:
        raise ValueError(f"Distance in {unit} cannot be negative: {value}")


def m_to_km(meters: float) -> float:
    """
    Convert meters to kilometers.
    
    Args:
        meters (float): Distance in meters
    
    Returns:
        float: Distance in kilometers
    
    Raises:
        ValueError: If meters is negative
    
    Example:
        >>> m_to_km(1000)
        1.0
        >>> m_to_km(5000)
        5.0
    """
    _validate_distance(meters, "meters")
    return multiply(meters, M_TO_KM)


def km_to_m(kilometers: float) -> float:
    """
    Convert kilometers to meters.
    
    Args:
        kilometers (float): Distance in kilometers
    
    Returns:
        float: Distance in meters
    
    Raises:
        ValueError: If kilometers is negative
    
    Example:
        >>> km_to_m(1)
        1000.0
        >>> km_to_m(2.5)
        2500.0
    """
    _validate_distance(kilometers, "kilometers")
    return multiply(kilometers, KM_TO_M)


def m_to_cm(meters: float) -> float:
    """
    Convert meters to centimeters.
    
    Args:
        meters (float): Distance in meters
    
    Returns:
        float: Distance in centimeters
    
    Raises:
        ValueError: If meters is negative
    
    Example:
        >>> m_to_cm(1)
        100.0
        >>> m_to_cm(2.5)
        250.0
    """
    _validate_distance(meters, "meters")
    return multiply(meters, M_TO_CM)


def cm_to_m(centimeters: float) -> float:
    """
    Convert centimeters to meters.
    
    Args:
        centimeters (float): Distance in centimeters
    
    Returns:
        float: Distance in meters
    
    Raises:
        ValueError: If centimeters is negative
    
    Example:
        >>> cm_to_m(100)
        1.0
        >>> cm_to_m(250)
        2.5
    """
    _validate_distance(centimeters, "centimeters")
    return multiply(centimeters, CM_TO_M)


def mi_to_ft(miles: float) -> float:
    """
    Convert miles to feet.
    
    Args:
        miles (float): Distance in miles
    
    Returns:
        float: Distance in feet
    
    Raises:
        ValueError: If miles is negative
    
    Example:
        >>> mi_to_ft(1)
        5280.0
        >>> mi_to_ft(0.5)
        2640.0
    """
    _validate_distance(miles, "miles")
    return multiply(miles, MI_TO_FT)


def ft_to_mi(feet: float) -> float:
    """
    Convert feet to miles.
    
    Args:
        feet (float): Distance in feet
    
    Returns:
        float: Distance in miles
    
    Raises:
        ValueError: If feet is negative
    
    Example:
        >>> ft_to_mi(5280)
        1.0
        >>> ft_to_mi(2640)
        0.5
    """
    _validate_distance(feet, "feet")
    return multiply(feet, FT_TO_MI)


def ft_to_in(feet: float) -> float:
    """
    Convert feet to inches.
    
    Args:
        feet (float): Distance in feet
    
    Returns:
        float: Distance in inches
    
    Raises:
        ValueError: If feet is negative
    
    Example:
        >>> ft_to_in(1)
        12.0
        >>> ft_to_in(2.5)
        30.0
    """
    _validate_distance(feet, "feet")
    return multiply(feet, FT_TO_IN)


def in_to_ft(inches: float) -> float:
    """
    Convert inches to feet.
    
    Args:
        inches (float): Distance in inches
    
    Returns:
        float: Distance in feet
    
    Raises:
        ValueError: If inches is negative
    
    Example:
        >>> in_to_ft(12)
        1.0
        >>> in_to_ft(24)
        2.0
    """
    _validate_distance(inches, "inches")
    return multiply(inches, IN_TO_FT)


def m_to_ft(meters: float) -> float:
    """
    Convert meters to feet.
    
    Args:
        meters (float): Distance in meters
    
    Returns:
        float: Distance in feet
    
    Raises:
        ValueError: If meters is negative
    
    Example:
        >>> round(m_to_ft(1), 2)
        3.28
        >>> round(m_to_ft(10), 2)
        32.81
    """
    _validate_distance(meters, "meters")
    return multiply(meters, M_TO_FT)


def ft_to_m(feet: float) -> float:
    """
    Convert feet to meters.
    
    Args:
        feet (float): Distance in feet
    
    Returns:
        float: Distance in meters
    
    Raises:
        ValueError: If feet is negative
    
    Example:
        >>> round(ft_to_m(1), 2)
        0.3
        >>> round(ft_to_m(10), 2)
        3.05
    """
    _validate_distance(feet, "feet")
    return multiply(feet, FT_TO_M)


def km_to_mi(kilometers: float) -> float:
    """
    Convert kilometers to miles.
    
    Args:
        kilometers (float): Distance in kilometers
    
    Returns:
        float: Distance in miles
    
    Raises:
        ValueError: If kilometers is negative
    
    Example:
        >>> round(km_to_mi(1), 2)
        0.62
        >>> round(km_to_mi(10), 2)
        6.21
    """
    _validate_distance(kilometers, "kilometers")
    return multiply(kilometers, KM_TO_MI)


def mi_to_km(miles: float) -> float:
    """
    Convert miles to kilometers.
    
    Args:
        miles (float): Distance in miles
    
    Returns:
        float: Distance in kilometers
    
    Raises:
        ValueError: If miles is negative
    
    Example:
        >>> round(mi_to_km(1), 2)
        1.61
        >>> round(mi_to_km(10), 2)
        16.09
    """
    _validate_distance(miles, "miles")
    return multiply(miles, MI_TO_KM)
