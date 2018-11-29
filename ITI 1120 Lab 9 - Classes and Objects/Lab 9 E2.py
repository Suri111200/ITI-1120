class Car:
    #Method to initialize class
    def __init__(self, bb='Ford', cc='Red'):
        self.brand = bb
        self.color = cc
        self.pilote = 'Person'
        self.speed = 0

    def __repr__(self):
        return "(%s, %s, %s, %s)" % (self.brand, self.color, self.pilote, self.speed)

    #def __eq__(self):

    
    #Method to change driver
    def choice_driver(self, dd):
        if dd:
            self.pilote = dd

    #Method to accelerate car
    def accelerate(self,flow=0,duration=0):
        if flow != 0 and duration != 0 and self.pilote == 'Person':
            print("This car does not have a driver!")
        else:
            self.speed += flow*duration
    #Method to display all info
    def display_all(self):
        print(self.color,self.brand,'driven by',self.pilote+', speed =',self.speed)
        
