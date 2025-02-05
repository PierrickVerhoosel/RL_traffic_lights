# Cross Road Class

# Define the class

class CrossRoad:
    def __init__(self,lanes_south, lanes_east, lanes_north, lanes_west, size_crossroad_sn, size_crossroad_we):
        self.lanes_south = lanes_south # Number of lanes in the south direction
        self.lanes_east = lanes_east # Number of lanes in the east direction
        self.lanes_north = lanes_north # Number of lanes in the north direction
        self.lanes_west = lanes_west # Number of lanes in the west direction
        self.size_crossroad_sn = size_crossroad_sn # Size of the crossroad in the north-south direction measured in meters
        self.size_crossroad_we = size_crossroad_we # Size of the crossroad in the west-east direction measured in meters
    
    def display(self):
        print("Crossroad ID: ", self.id)
        print("Number of lanes in the south direction: ", self.lanes_south)
        print("Number of lanes in the east direction: ", self.lanes_east)
        print("Number of lanes in the north direction: ", self.lanes_north)
        print("Number of lanes in the west direction: ", self.lanes_west)
        print("Size of the crossroad in the north-south direction: ", self.size_crossroad_sn)
        print("Size of the crossroad in the west-east direction: ", self.size_crossroad_we)

    



