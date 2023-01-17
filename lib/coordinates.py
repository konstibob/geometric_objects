from lib.vector import Vector
from lib.forms import Polygon, Rectangle, Circle

class Coordinate_system():
    def __init__(self,min_x = 0,max_x = 10,min_y = 0,max_y = 10):   #default size for coordinate system

        self.geometric_objects = []

        if not (min_x < max_x and min_y < max_y):
            raise ValueError("Error: min_x should be less than max_x and min_y should be less than max_y.Coordinate system was created with default values")

        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
    
    #add Object to Coordinate System
    def add_Obj(self,obj):
        #checks that two objects dont have the same name
        for elem in self.geometric_objects:
            if obj.name == elem.name:
                raise NameError("Cant Name two Objects the same way")
        try:
            assert not self.over_coordinates(obj)

        except AssertionError:
            print("you cant input this object, cause its overlapping with the coordinate System")
            return    

        self.geometric_objects.append(obj)

    #remove Object from Coordinate System
    def remove_Obj(self,obj):  
        if obj not in self.geometric_objects:
            print(f"Object not in Coordinate System")
            return
        else:
            self.geometric_objects.remove(obj)
    
    def get_overlap(self):
        collisiondict = {}  #dictionary for object and Value if its Intersecting with any other Object
        nocollision = True
        for i in range(len(self.geometric_objects)):
            for j in range(len(self.geometric_objects)):
                if j != i:
                    if self.geometric_objects[i].collision(self.geometric_objects[j]):
                        collisiondict.update({self.geometric_objects[i].name: "is overlapping"})
                        nocollision = False
                        break

            if nocollision:
                collisiondict.update({self.geometric_objects[i].name: "is not overlapping"})
            else:
                nocollision = True  
        return collisiondict

    #checks if object is over the coordinate System
    def over_coordinates(self,obj):
        #if its Circle -> over_coordinates is used for the overlap checking and therefore using Over_coordinate function 
        if isinstance(obj,Circle): 
            for point in obj.over_coordinate():
                if self.isover(point):
                    return True
            return False

        else:
            points = obj.get_projection_vertices("doesnt matter")
            for point in points:
                if self.isover(point):
                    return True
            return False

    #function that should replace the long checking
    def isover(self,point):
        if not (point.x >= self.min_x and point.x <= self.max_x and point.y >= self.min_y and point.y <= self.max_y):
            return True

    #if print(Coordinate_system) is called -> all objects are displayed
    def __repr__(self) -> str:
        return f"All Geometric Objects ({self.geometric_objects})"

    def all_geometric_objects(self):
        return self.geometric_objects