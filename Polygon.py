##########################################################################
# Session11 assignment for EPAi3 - Module Polygon
#
# Ganesan Thiagarajan, 24th July 2021
##########################################################################
#
from functools import wraps
import math
from functools import lru_cache

# Timed decorator for all functions - but using a global variable for elapsed time in case we want it at __main__ level
elapsed_time = 0

def timed(fn: 'Function name') -> 'Time for execution of the function':
    """
    A function decorator to compute the execution time for all the functions in this module when called
    from the test script.
    Params:
    fn - Function name
    Returns:
        Time for execution in seconds
    """
    from time import perf_counter
    @wraps(fn)
    def inner(*args, **kwargs):
        global elapsed_time
        start_time = perf_counter()
        result = fn(*args, **kwargs)
        end_time = perf_counter()
        elapsed_time = end_time - start_time
        print(f"Function {fn.__name__}() took {elapsed_time} secs to execute")
        return result

    return inner


# Function decorator for checking the docstring of functions
def check_doc_string(
        fn: 'Function name that needs to be parsed') -> 'Returns True if the function has 50 words of description':
    """
    This function checks whether the function passed on to this has atleast 50 words of
    description.
    :param fn: Function name that is passed to this function
    :return: Returns a closure which allows the free variables can be accessed later
             The inner function Returns True if it has 50 or more words in its docstring description, else False
    Question: Will the docstring include the argument description function as well?  A BIG NO!
    """
    comment_len = 50
    """
    Doc string for inner function
    :param args: Positional arguments for the function
    :param kwargs:Function arguments for the function
    :return: The function output
    """
    if fn.__doc__ is None:
        return False
    else:
        fn_doc_string = fn.__doc__.split(sep=" ")
        # print(f'No. of words in the docstring comment for {fn.__name__}() is : {len(fn_doc_string)}')
        if len(fn_doc_string) < comment_len:
            return False
        else:
            return True

class Polygon:
    """
    Class definiion for a regular Polygon with n equal sides and n-vertices
    Args:
        n - No. of edges (or sides)
        R - circum radius - i.e., distance between the center and one of the vertices

    Returns:
        Polygon class object
    """
    def __init__(self, n, R):
        """
        Sets the initial values of the internal variables n (#sides) and R (circum radius)
        Args:
            n - No. of edges (or sides)
            R - circum radius - i.e., distance between the center and one of the vertices
        """
        if n < 3:
            raise ValueError('Polygon must have at least 3 vertices.')
        self._n = n
        self._R = R

    def __repr__(self):
        """
        __repr__() for the Polygon class objects
        Returns:
            Prints the class objects internal variables
        """
        return f'Polygon(n={self._n}, R={self._R})'

    @property
    def count_vertices(self):
        """
        Count the number of vertices in the polygon as a property, i.e., Object.count_vertices
        Returns:
            The number of vertices
        """
        return self._n

    @property
    def count_edges(self):
        """
        Count the number of edges in the polygon as a property, i.e., Object.count_edges
        Returns:
            The number of edges
        """
        return self._n

    @property
    def circumradius(self):
        """
        Get the circum radius as a property, i.e., Object.circumradius
        Returns:
            Returns the circum radius
        """
        return self._R

    @property
    def interior_angle(self):
        """
        Compute the interior angle and return as a property, i.e., Object.interior_angle
        Returns:
            Returns the interior angle in degrees
        """
        return (self._n - 2) * 180 / self._n

    @property
    def side_length(self):
        """
        Compute the length of the edges and return as a property, i.e., Object.side_length
        Returns:
            Returns the side_length in the same units as the circum radius
        """
        return 2 * self._R * math.sin(math.pi / self._n)

    @property
    def apothem(self):
        """
        Compute the length of the apothem nd return as a property, i.e., Object.apothem
        Returns:
            Returns the apothem in the same units as the circum radius
        """
        return self._R * math.cos(math.pi / self._n)

    @property
    def area(self):
        """
        Compute the area of the polygon nd return as a property, i.e., Object.area
        Returns:
            Returns the area in the same units as the circum radius**2
        """
        return self._n / 2 * self.side_length * self.apothem

    @property
    def perimeter(self):
        """
        Compute the perimeter of the polygon return as a property, i.e., Object.perimeter
        Returns:
            Returns the apothem in the same units as the circum radius
        """
        return self._n * self.side_length

    def __eq__(self, other):
        """
        Checks if two given polygons (self and other) are equal.
        Equality is true when the no. of edges and circum radius are equal
        Args:
            self - self Polygon object
            other - other Polygon objects
        Returns:
            Returns True if the no. of edges and circum radius are equal, else False
        """
        if isinstance(other, self.__class__):
            return True if (self.count_edges == other.count_edges
                    and self.circumradius == other.circumradius) else False
        else:
            raise TypeError("other is not an instance of Polygon class")
            #return NotImplemented

    def __gt__(self, other):
        """
        Checks if one of the given polygons (self and other) is relatively greater than the other
        Relative operator gt is true when the no. of edges is self is greater than that in other

        Args:
            self - self Polygon object
            other - other Polygon objects
        Returns:
            Returns True if the no. of edges in self is greater than that of other
        """
        if isinstance(other, self.__class__):
            return True if (self.count_vertices > other.count_vertices) else False
        else:
            raise TypeError("other is not an instance of Polygon class")
            #return NotImplemented

class MyPolygon:
    """
    Class definition for a n-Polygon: creating a regular polygon of equal sides with n sides
    """

    @timed
    def __init__(self, s: 'No. of sides (int)' = 3, r: 'Circum radius' = 1):
        """
        Init for polygon class
        Args:
            s: No. of edges or vertices (integer) - default 3
            r: Circum radius, i.e., distance between the center and one of the vertices - default 1
        Returns: None - Initializes the object
            The class object with the following parameters initialized
                int_angle = (s-2) * 180.0/s  --> Interior angle
                edge_len = 2 * r * math.sin(math.pi/s)  --> length of one edge
                apothem = r * math.cos(math.pi/s)   --> distance between the center and line joining two vertices
                area = 0.5 * s * self.edge_len * self.apothem  --> area of the polygon
                perimeter = s * edge_len  --> Perimeter
                vertices = No. of vertices = no. of edges --> No of vertices
        """
        if s < 3:
            raise ValueError("No. of edges cannot be less than 3")

        self.edges = s
        self.radius = r
        self.interior_angle = (s - 2) * 180.0 / s
        self.side_length = 2 * r * math.sin(math.pi / s)
        self.apothem = r * math.cos(math.pi / s)
        self.area = 0.5 * s * self.side_length * self.apothem
        self.perimeter = s * self.side_length
        self.vertices = s

    def __repr__(self):
        print(f'Regular polygon with {self.edges} sides and circum radius = {self.radius}')
        print(f'The class object with the following parameters initialized')
        print(f'edges     --> No. of edges = {self.edges}')
        print(f'radius    --> circum radius = {self.radius}')
        print(f'int_angle --> Interior angle = {self.int_angle}')
        print(f'edge_len  --> length of one edge = {self.edge_len}')
        print(f'apothem   --> distance between the center and line joining two verticesi = {self.apothem}')
        print(f'area      --> area of the polygon = {self.area}')
        print(f'perimeter --> perimeter  = {self.perimeter}')
        print(f'vertices  --> No of vertices = {self.vertices}')

    def __eq__(self, other):
        """
        Checks whether two polygons are equal or not. The first polygon is self
        Args:
            other: The second polygon
        Returns:
            True if no. of sides and radius are equal else False
        """
        return True if (self.edges == other.edges and self.radius == other.radius) else False

    def __gt__(self, other):
        """
        Checks whether one of two polygons is greater than the other. The first polygon is self
        Args:
            other: The second polygon
        Returns:
            True if no. of sides of first is more than the second's
        """
        return True if (self.edges > other.edges) else False

# End of file