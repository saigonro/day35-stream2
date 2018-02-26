# Create a class called Donut. When the class is instantiated it should have a size of 100 (meaning 100% of the donut is there). Add an bite method that reduces the size of the donut
# by 25%. If the bite method is called when the size of the donut is 0, do not reduce the size any further.
# You can use print(d.size) to display the size of a Donut d. Check that 4 bites leaves the size at 0, and 5 bites still leaves it at zero.

class Donut():
    
    def __init__(self):
        self.total = 100
        
    
    def bite(self):
        self.bitesize = 25
        self.total -= self.bitesize
        if self.total > 0:
            print(self.total)
        else:
            print("Nothing left")
        
d = Donut()
e = Donut()
d.bite()
d.bite()
d.bite()
d.bite()
d.bite()
print(e.total)
        