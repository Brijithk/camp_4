class Box:
    def __init__(self,width,height,depth):
        self.width=width
        self.height=height
        self.depth=depth
    def get_volume(self):
        volume=self.width*self.height*self.depth
        print(f"The volume is {volume}")
    
box_1=Box(1,2,3)
box_2=Box(10,20,30)

box_1.get_volume()
box_2.get_volume()