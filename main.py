from lib.vector import Vector
from lib.forms import Polygon, Rectangle, Circle
from lib.projection import Projection
from lib.coordinates import Coordinate_system
 
def main():
    
    c = Coordinate_system()

    x = Rectangle("A",[0,0,2,2],[0,2,2,0])
    y = Rectangle("B",[5,5,3,3],[0,4,3,0])
    z = Circle("C",Vector(5,5),4)


    c.add_Obj(x)
    c.add_Obj(z)

    print(c.get_overlap())
    

    

if __name__ == '__main__':
    main()