def triangle_area(base, height):
    """"
     compute area of triangle

     Args: 
      base(float): The triangle's base
      height(float): The triangle's height

      returns:
       float: the area of triangle calculated as (base*height)/2

       Examples:
        >>> triangle_area(10, 5)
        25.0

        >>> triangle_area(3.5, 2)
        3.5
    """

    return (base*height)/2

print(triangle_area(3.5, 2))