from lib.vector import Vector
from lib.forms import Polygon, Rectangle, Circle
from lib.projection import Projection
from lib.coordinates import Coordinate_system


import unittest

class Test(unittest.TestCase):
    def test_no_collision_2_rectangles(self):
        x = Rectangle("A",[0,2,2,0],[0,0,2,2])
        y = Rectangle("B",[5,5,3,3],[0,2,2,0])
        colliding = x.collision(y)
        self.assertEqual(colliding, False)
    
    def test_collision_2_rectangles(self):
        x = Rectangle("A",[0,2,2,0],[0,0,2,2])
        y = Rectangle("B",[1,3,3,1],[0,0,2,2])
        colliding = x.collision(y)
        self.assertEqual(colliding, True)

    def test_collision_rectangle_Circle(self):
        x = Rectangle("A",[0,2,2,0],[0,0,2,2])
        y = Circle("B",Vector(3,1), 2)
        colliding = x.collision(y)
        self.assertEqual(colliding,True)

    def test_no_collision_rectangle_Circle(self):
        x = Rectangle("A",[0,2,2,0],[0,0,2,2])
        y = Circle("B",Vector(7,7), 2)
        colliding = x.collision(y)
        self.assertEqual(colliding,False)

    def test_collision_two_Circles(self):
        x = Circle("A",Vector(1,1),3)
        y = Circle("B",Vector(1,6),4)
        colling = x.collision(y)
        self.assertEqual(colling,True)

    def test_no_collision_two_Circles(self):
        x = Circle("A",Vector(0,0),2)
        y = Circle("B",Vector(0,6),2)
        colling = x.collision(y)
        self.assertEqual(colling,False)

    #function should print error
    def test_overlapping_coordinates(self):
        c = Coordinate_system()
        x = Circle("A",Vector(0,0),2)
        c.add_Obj(x)

    def test_remove_Circle_Rectangle(self):
        c = Coordinate_system()
        x = Rectangle("A",[0,2,2,0],[0,0,2,2])
        y = Circle("B",Vector(7,7), 2)

        c.add_Obj(x)
        c.add_Obj(y)

        c.remove_Obj(x)
        c.remove_Obj(y)

        self.assertEqual(c.all_geometric_objects(),[])

    
        


if __name__ == "__main__":
    unittest.main()