# -*- coding: utf-8 -*-
"""test_session11_pynotes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cbojvIXjCPt18ewfD5hi68XpBlTAjOhB

## Polygon Class Definition
"""

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

"""## Polygon Iterator Class Definition

"""

class PolygonIterator(Polygon):
    """
    Definition for Polygon Iterator Class object
    """
    def __init__(self, n, r):
        """
        Initializes the Polygon sequence object
        Args:
            n: Maximum number of edges in the sequence of polygons
            r: Circum radius for the polygon
        Returns:
            None
            But computes the internal list of polygons in self._polygons
            And sets the current_poly as 3 to make it iterable
        """
        self._n = n
        self._r = r
        self._polygons = [Polygon(i, r) for i in range(3, n + 1)]
        self._current_poly = 3

    def __len__(self):
        """
        Returns the length of the Iterator
        """
        return self._n

    def __next__(self):
        """
        Calls the iter() function for iteration
        Returns: the object returned by iter function
        """
        return self.__iter__()

    def __iter__(self):
        """
        next function to make this sequence as iterable
        Returns:
            The current poly and increments the counter until the maximum limit
        """
        #print(f'Current polygon inside _next() is : {self._current_poly}')
        if self._current_poly >= self._n:
            raise StopIteration
        else:
            try:
                item = self._polygons[self._current_poly]
                self._current_poly += 1
            except IndexError:
                raise StopIteration
        return self

    def __len__(self):
        """
        Get the number of polygons in the sequence
        Returns:
            self.n-2 since first valid polygon has 3 sides always
        """
        return self._n - 2

    def __repr__(self):
        """
        __repr__() function for the PolygonIterator class object
        Returns:
            The format string with m and R information
        """
        return f'Polygons(n={self._n}, R={self._r})'

    #def __getitem__(self, s):
    #    return self._polygons[s]

    @property
    def max_efficiency_polygon(self):
        """
        Compute the area efficiency (ratio of area to perimeter) for all polygons in the sequence
        and return the one with maximum efficiency
        Returns:
            The polygon class object with maximum efficiency as a property, i.e., seqObject.max_efficiency_polygon
        """
        sorted_polygons = sorted(self._polygons,
                                 key=lambda p: p.area / p.perimeter,
                                 reverse=True)
        return sorted_polygons[0]

class MyPolygonSeq(MyPolygon):
    """
    Polygon sequence class derived from the polygon class object
    """

    def __init__(self, n, r):
        """
        Creates a polygon sequence with the largest polygon with n sides and r radius
        Also computes the maximum efficiency polygon which has the highest area to perimeter ratio
        Args:
            n: Maximum no. of edges or sides
            r: Circum radius of all polygons
        """
        self.n = n  # Maximum no. of polygon available in the sequence
        self.r = r
        self.max_eff_n = 3
        self.max_eff = 0
        self.curr_poly = n  # default polygon index

        max_eff = 0
        for i in range(3, n + 1):
            temp_poly = self._polygon(i, r)
            eff = temp_poly.area / temp_poly.perimeter
            if self.max_eff < eff:
                self.max_eff = eff
                self.max_eff_n = i

    @staticmethod
    @lru_cache(maxsize=100)
    def _polygon(s, r):
        """
        Computes the polygon of given order and radius
        Args:
            s: Polygon order
            r: Circum radius of the polygon
        Returns:
            The polygon class object
        """
        return MyPolygon(s, r)

    def __repr__(self):
        """
        Gives the description of the PolygonSeq class objects.
        Returns:
            Print statement of the length (maximum order), radius and the maximum efficiency polygon
        """
        print(f'Polygon sequence of length = {self.n} with radius = {self.r}')
        print(f'The maximum efficiency polygon is with edges = {self.max_eff_n}')
        print(f'The maximum efficiency (area/perimeter) is {self.max_eff}')

    def __len__(self):
        """
        Returns the length of the polygon sequence. The length refers to the maximum order in the sequence
        Returns:
            The highest polygon order
        """
        return self.n

    def __getitem__(self, s):
        """
        Gets the polygon of order s
        Args:
            s: The order of the polygon
        Returns:
            The polygon of order s
        """
        if isinstance(s, int):
            if s < 3 or s > self.n:
                raise IndexError
            else:
                return self._polygon(s, self.r)

    def _next(self):
        """
        Return the next polygon in the sequence.
        The polygon class object which is next in the sequence is returned.
        The current sequence number is updated.
        """
        if self.curr_poly < self.n:
            self.curr_poly += 1
            return self.__getitem__(self.curr_poly)
        else:
            print("Reached the end of sequence")
            return self.__getitem__(self.n)
            # raise IndexError

    def _prev(self):
        """
        Return the previous polygon in the sequence
        The polygon class object which is previous in the sequence is returned.
        The current sequence number is updated.
        """
        if self.curr_poly >= 4:
            self.curr_poly -= 1
            return self.__getitem__(self.curr_poly)
        else:
            print("Reached start of sequence")
            return self.__getitem__(3)
            # raise IndexError

"""## Tests

"""

gon3 = Polygon(3, 1)
print(gon3.__repr__())
gon6 = Polygon(6, 2)
print(gon3 == gon6)
print(gon6 > gon3)

test1 = PolygonIterator(10,1)
print(test1._current_poly)
print(f'Description of PolygonIterator Claas Object is : {test1.__repr__()}')
print(f'Current Polygon object Description is : {test1.__iter__().__repr__()}')
print(f'No. of polygons in the iterator is : {test1._polygons.__len__()}')
print(f'No. of edges in the current polygon is : {test1.__next__()._current_poly}')
test1.__next__()    # Move to next polygon
print(f'No. of edges in the current polygon is : {test1.__next__()._current_poly}')