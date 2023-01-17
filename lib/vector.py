#diese Datei ist im Vergleich zu den anderen auf deutsch, da es hier um Mathematische Operationen
#handelt und die Begriffe mir die Begriffe auf deutsch geläufiger sind.

import math

class Vector():
    def __init__(self,x,y):
        self.x = x
        self.y = y 

    def normalen_vector(self):   
        #zeigt hier immer nach links im 90 Grad winkel 
        return Vector(-self.y,self.x)

    def skalar_produkt(self,node):  
        #kann bsp benutzt werden ob Vektoren die eingegeben werden Rechteck sind vllt anders noch :0
        return self.x * node.x + self.y * node.y

    def länge(self):
        #Gibt länge zurück
        return math.sqrt(self.x * self.x + self.y * self.y)

    def normalisieren(self):
        #ändert die Länge vom Vektor auf 1, behält aber die Richtung bei
        l = self.länge()
        if l == 0:
            return Vector(0,0)
        return Vector(self.x/l,self.y/l)
    
    def __repr__(self) -> str:
        #damit wenn print(Vector) aufgerufen wird, beide Koordinaten aufgerufen geprinted werden
        return f"Vector ({self.x},{self.y})"