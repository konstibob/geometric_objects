class Projection():
    def __init__(self,min,max):
        self.min = min
        self.max = max
    def has_seperating_axes(self,proj):
        return self.max < proj.min or self.min > proj.max


