from lib.vector import Vector
from lib.projection import Projection
import math 

class Shape:
    # abstract method
    def get_projection_vertices(self, axis):
        raise NotImplementedError()
    
    # abstract method
    def get_projection_axes(self):
        raise NotImplementedError()

    #1 -> alle axen generieren
    #2 -> alle objekte auf achse projektieren
    #3 -> für jedes gucken ob es gap gibt
    def collision(self,other):
        allaxes = self.get_projection_axes() + other.get_projection_axes()

        for achse in allaxes:
            proj1 = self.project(achse)
            proj2 = other.project(achse)
            
            if proj1.has_seperating_axes(proj2):
                return False

        return True

    def project(self,axis):
        minimal = math.inf
        maximal = -math.inf

        #projection of point of object on axis and tracking for each vertex the min and max
        for vertex in self.get_projection_vertices(axis):
            projection = axis.skalar_produkt(vertex)

            if projection < minimal:
                minimal = projection
            if projection >= maximal:
                maximal = projection
                
        return Projection(minimal, maximal) #object that can be used to compare the Projection between multiple objects on Axis


class Polygon(Shape):
    def __init__(self, name, x, y):
        self.name = name
        self.vectors = []

        if len(x) != len(y):    
            raise ValueError("the amount of x and y coordinates arent the same!")
        if len(x) >= 10:
            raise ValueError("Too many edges on this Polygon")
        for i in range(len(x)):
            self.vectors.append(Vector(x[i],y[i]))

    def get_projection_vertices(self, _axis):
        return self.vectors
    
    def get_projection_axes(self):
        axes = []
        for i in range(len(self.vectors)):
            
            if i == len(self.vectors) - 1:
                node = Vector(self.vectors[i].x - self.vectors[0].x,self.vectors[i].y - self.vectors[0].y)
            else:  
                node = Vector(self.vectors[i].x - self.vectors[i+1].x,self.vectors[i].y - self.vectors[i+1].y)

            axes.append(node.normalen_vector().normalisieren())
            
        return axes


class Rectangle(Polygon):
    def __init__(self,name, x, y):
        if len(y) != 4 or len(x) != 4:
            print("you need 4 x and 4 y Coordinates for a Rectangle")
            return 
        else:
            super().__init__(name,x, y)
            #checks if inputted form is an Rectangle if not then destroy it 
            if not self.isRectangular():
                print("The Object here isnt an Rectangle but you can still use it ")

    #checks if this object is a Rectangle. Points have to be inserted against Clock Cycle
    def isRectangular(self):
        axestocheck = self.get_projection_axes()
    
        for j in range(len(axestocheck)):
            found = True
            if j != len(axestocheck) - 1:
                if axestocheck[j].skalar_produkt(axestocheck[j+1]) != 0:
                    return False
                    
            else:   
                if axestocheck[0].skalar_produkt(axestocheck[j]) != 0:
                    return False
        return True

class Circle(Polygon):
    #c is a Vector 
    #r is a number
    def __init__(self, name, c, r): 
        self.name = name   
        self.center = c
        self.radius = r

    #project axis on center of circle
    def get_projection_vertices(self, axis):
        return [Vector(self.center.x + (axis.normalen_vector().y * self.radius),
                        self.center.y + (-axis.normalen_vector().x * self.radius)),
                Vector(self.center.x + (-axis.normalen_vector().y * self.radius),
                        self.center.y + (axis.normalen_vector().x * self.radius))
                ]
    #collision for two Circles made seperate, cause two Circles dont have any projection_axes
    def collision(self,other):
        if isinstance(other, Circle):
            #dist -> distance between both centerpoints
            vecdis = Vector(self.center.x - other.center.x, self.center.y - other.center.y) 
            dist = vecdis.länge() 
            #if any radius is bigger than dist it means both Circles are touching
            if dist >= max(self.center.länge(), other.center.länge()):
                return False
            else:
                return True
        else:
            #Collision between Circle and Rectangle or Polygon
            return super().collision(other)
    
    #has no Projection axes
    def get_projection_axes(self):
        return []
    
    #Points to check for Coordinate System
    def over_coordinate(self):
        x = self.center.x
        y = self.center.y 
        r = self.radius
        return [Vector(x,y+r),
                Vector(x,y-r),
                Vector(x+r,y),
                Vector(x-r,y)
                ]