#Deion Stewart and Joseph Candella
#Car Exercise

class Car:
    """ This class allows instances to turn left or right and drive forward and back. """

    def __init__ (self):
        """  Sets the following attributes to the values specified below:"""
        
        self.x = 0
        self.y = 0
        self.heading = "n"
    
    def turn (self, direction):
        """ Takes direction as a parameter and modifies the self.heading attribute with a proper heading (n,s,e,w). """
        
        if direction == "l" and self.heading == "n":
            self.heading = "w"
            
        elif direction == "r" and self.heading == "n":
            self.heading = "e"
            
        elif direction == "l" and self.heading == "w":
            self.heading = "s"
            
        elif direction == "r" and self.heading == "w":
            self.heading = "n"
            
        elif direction == "l" and self.heading == "s":
            self.heading = "e"
            
        elif direction == "r" and self.heading == "s":
            self.heading = "w"
        
        elif direction == "l" and self.heading == "e":
            self.heading = "n"
            
        elif direction == "r" and self.heading == "e":
            self.heading = "s"
            
    def drive (self, distance=1):
        """ Takes distance as a parameter and modifies the self.x and self.y attributes by adding distance based on the direction. """
        
        if self.heading == "n":
            self.y += distance
        elif self.heading == "e":
            self.x += distance
        elif self.heading == "s":
            self.y -= distance
        elif self.heading == "w":
            self.x -= distance 
    
    def status (self):
        """ Prints the current position of the car as coordinates and its heading (n,s,e,w). """
        
        print (f"Coordinates: {self.x , self.y}")
        print (f"Heading: {self.heading}")
            
        
        