"""
Weight Conversion Module

This module provides functions for converting between common weight units.
All conversions use helper functions from simple_arithmetic for calculations.
"""

from helper_functions.simple_arithmetic import multiply


# Conversion factors
KG_TO_G = 1000.0
G_TO_KG = 0.001
G_TO_MG = 1000.0
MG_TO_G = 0.001
LB_TO_OZ = 16.0
OZ_TO_LB = 1 / 16.0
KG_TO_LB = 2.20462
LB_TO_KG = 0.453592
G_TO_OZ = 0.035274
OZ_TO_G = 28.3495


def _validate_weight(value: float, unit: str) -> None:
    """
    Validate that a weight value is non-negative.
    
    Args:
        value (float): The weight value to validate
        unit (str): The unit name for error messaging
    
    Raises:
        ValueError: If the value is negative
    """
    if value < 0:
        raise ValueError(f"Weight in {unit} cannot be negative: {value}")


def kg_to_g(kilograms: float) -> float:
    """
    Convert kilograms to grams.
    
    Args:
        kilograms (float): Weight in kilograms
    
    Returns:
        float: Weight in grams
    
    Raises:
        ValueError: If kilograms is negative
    
    Example:
        >>> kg_to_g(1)
        1000.0
        >>> kg_to_g(2.5)
        2500.0
    """
    _validate_weight(kilograms, "kilograms")
    return multiply(kilograms, KG_TO_G)


def g_to_kg(grams: float) -> float:
    """
    Convert grams to kilograms.
    
    Args:
        grams (float): Weight in grams
    
    Returns:
        float: Weight in kilograms
    
    Raises:
        ValueError: If grams is negative
    
    Example:
        >>> g_to_kg(1000)
        1.0
        >>> g_to_kg(2500)
        2.5
    """
    _validate_weight(grams, "grams")
    return multiply(grams, G_TO_KG)


def g_to_mg(grams: float) -> float:
    """
    Convert grams to milligrams.
    
    Args:
        grams (float): Weight in grams
    
    Returns:
        float: Weight in milligrams
    
    Raises:
        ValueError: If grams is negative
    
    Example:
        >>> g_to_mg(1)
        1000.0
        >>> g_to_mg(2.5)
        2500.0
    """
    _validate_weight(grams, "grams")
    return multiply(grams, G_TO_MG)


def mg_to_g(milligrams: float) -> float:
    """
    Convert milligrams to grams.
    
    Args:
        milligrams (float): Weight in milligrams
    
    Returns:
        float: Weight in grams
    
    Raises:
        ValueError: If milligrams is negative
    
    Example:
        >>> mg_to_g(1000)
        1.0
        >>> mg_to_g(2500)
        2.5
    """
    _validate_weight(milligrams, "milligrams")
    return multiply(milligrams, MG_TO_G)


def lb_to_oz(pounds: float) -> float:
    """
    Convert pounds to ounces.
    
    Args:
        pounds (float): Weight in pounds
    
    Returns:
        float: Weight in ounces
    
    Raises:
        ValueError: If pounds is negative
    
    Example:
        >>> lb_to_oz(1)
        16.0
        >>> lb_to_oz(2.5)
        40.0
    """
    _validate_weight(pounds, "pounds")
    return multiply(pounds, LB_TO_OZ)


def oz_to_lb(ounces: float) -> float:
    """
    Convert ounces to pounds.
    
    Args:
        ounces (float): Weight in ounces
    
    Returns:
        float: Weight in pounds
    
    Raises:
        ValueError: If ounces is negative
    
    Example:
        >>> oz_to_lb(16)
        1.0
        >>> oz_to_lb(32)
        2.0
    """
    _validate_weight(ounces, "ounces")
    return multiply(ounces, OZ_TO_LB)


def kg_to_lb(kilograms: float) -> float:
    """
    Convert kilograms to pounds.
    
    Args:
        kilograms (float): Weight in kilograms
    
    Returns:
        float: Weight in pounds
    
    Raises:
        ValueError: If kilograms is negative
    
    Example:
        >>> round(kg_to_lb(1), 2)
        2.2
        >>> round(kg_to_lb(10), 2)
        22.05
    """
    _validate_weight(kilograms, "kilograms")
    return multiply(kilograms, KG_TO_LB)


def lb_to_kg(pounds: float) -> float:
    """
    Convert pounds to kilograms.
    
    Args:
        pounds (float): Weight in pounds
    
    Returns:
        float: Weight in kilograms
    
    Raises:
        ValueError: If pounds is negative
    
    Example:
        >>> round(lb_to_kg(1), 2)
        0.45
        >>> round(lb_to_kg(10), 2)
        4.54
    """
    _validate_weight(pounds, "pounds")
    return multiply(pounds, LB_TO_KG)


def g_to_oz(grams: float) -> float:
    """
    Convert grams to ounces.
    
    Args:
        grams (float): Weight in grams
    
    Returns:
        float: Weight in ounces
    
    Raises:
        ValueError: If grams is negative
    
    Example:
        >>> round(g_to_oz(100), 2)
        3.53
        >>> round(g_to_oz(500), 2)
        17.64
    """
    _validate_weight(grams, "grams")
    return multiply(grams, G_TO_OZ)


def oz_to_g(ounces: float) -> float:
    """
    Convert ounces to grams.
    
    Args:
        ounces (float): Weight in ounces
    
    Returns:
        float: Weight in grams
    
    Raises:
        ValueError: If ounces is negative
    
    Example:
        >>> round(oz_to_g(1), 2)
        28.35
        >>> round(oz_to_g(5), 2)
        141.75
    """
    _validate_weight(ounces, "ounces")
    return multiply(ounces, OZ_TO_G)
