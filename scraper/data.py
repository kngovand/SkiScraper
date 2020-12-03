class data:

    def __init__(self, temp, depth1, depth2, lifts, trails):

        self.temp = temp
        self.depth_total = depth1
        self.depth_overnight = depth2
        self.lifts = lifts
        self.trails = trails

    def print(self):
        print(
        'Temp: ' + self.temp + '\n' 
        'Depth total: ' + self.depth_total + '\n' 
        'Snow overnight: ' + self.depth_overnight + '\n' 
        'Lifts open: ' + self.lifts + '\n'
        'Trails open: ' + self.trails + '\n'
        )

