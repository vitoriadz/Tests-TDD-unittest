"""Simple calculator with four basic operations."""

def addition(x, y):
    """Addition calculation."""
    return x + y

def subtraction(x, y):
    """Subtraction calculation."""
    return x - y

def multiplication(x, y):
    """Multiplication calculation."""
    return x * y

def division(x, y):
    """Division calculation."""
    if y == 0:
        raise ValueError("The second division parameter cannot be zero.")
    return x / y
