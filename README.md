# Session 11 Readme file 
# Assignment details:

# Problem #1
The starting point for this project is the Polygon class and the 
Polygons sequence type we created in the previous project.

The code for these classes along with the unit tests for the 
Polygon class are below if you want to use those as your starting point. 
But use whatever you came up with in the last project.

Goal:
Refactor the Polygons (sequence) type, into an iterable. You'll need to implement both an iterable, and an iterator.
   Create a Polygon Class:
        where initializer takes in:
              o  number of edges/vertices
              o  circumradius
        that can provide these properties:
              o edges
              o vertices
              o interior angle
              o edge length
              o apothem
              o area
              o perimeter
        that has these functionalities:
              o a proper __repr__ function
              o implements equality (==) based on # vertices and circumradius (__eq__)
              o implements > based on number of vertices only (__gt__)
# Solution - Part 1
    * The Polygon Class given and Polygon class from last assignment were named
    as Polygon() and MyPolygon()
    
    Both were tested for the tests given 

    The __repr__() function prints the following information
        * Regular polygon with {self.edges} sides and circum radius = {self.radius}')
        The class object with the following parameters initialized')
            + edges     --> No. of edges = {self.edges}
            + radius    --> circum radius = {self.radius}
            + int_angle --> Interior angle = {self.int_angle}
            + edge_len  --> length of one edge = {self.edge_len}
            + apothem   --> distance between the center and line joining two verticesi = {self.apothem}
            + area      --> area of the polygon = {self.area}
            + perimeter --> perimeter  = {self.perimeter}
            + vertices  --> No of vertices = {self.vertices}
    
# Solution - Part 2
    In order to make the Polygon class object as iterable, the PolygonSequence
    class object is modified as PolygonIterator Class where iter() function
    and next() function are added and the one test case checks for the iteration
    on this object.
    
    The Class PolygonSeq from last assignment is renamed as MyPolygonSeq.
    
   * The MyPolygonSeq class object initialized as follows
        self.n = n  # Maximum no. of polygon available in the sequence
        self.r = r
        self.max_eff_n = 3
        self.max_eff = 0
        self.curr_poly = n  # default polygon index
     and the maximum efficiency polygon is computed as follows
        max_eff = 0
        for i in range(3, n + 1):
            temp_poly = self._polygon(i, r)
            eff = temp_poly.area / temp_poly.perimeter
            if self.max_eff < eff:
                self.max_eff = eff
                self.max_eff_n = i
    where the getitem for each entry in the sequence is computed and cached used lru_cache
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

    * The __repr__() function displays the following
        + Polygon sequence of length = {self.n} with radius = {self.r}
        + The maximum efficiency polygon is with edges = {self.max_eff_n}
        + The maximum efficiency (area/perimeter) is {self.max_eff}

# Test cases

   * The following test cases are added:
   
     o Test case 1: Checks invalid poygon order
     
     o Test case 2: Checks the function outputs and internal variables
     
     o Test case 3: Checks the area computation and side length
     
     o Test case 4: Checks the area computation and side length
     
     o Test case 5: Checks the area and interior angle computation
     
     o Test case 6: Checks the comparison operations
     
     o Test case 7: Checks the Polygon Sequence creation and iteration
     
# A readme file 
    * (this file) describes the code and solution approach and the test cases. 

# A py notebook 
    * which tests the above are given for verification in colab. 

# End of file
 