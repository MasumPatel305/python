import math

def circle_area(radius):
    """
    Calculate the area of a circle given its radius.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle, calculated as pi * radius^2.

    Examples:
        >>> circle_area(1)
        3.141592653589793

        >>> circle_area(2.5)
        19.634954084936208
    """
    return math.pi*radius**2

print(circle_area(2.5))