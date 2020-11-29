class WPData:

    def __init__(self, temp, depth1, depth2,
        depth3, depth4, lifts, trails):
        
        self.temp = temp
        self.depth_total = depth1
        self.depth_overnight = depth2
        self.depth_24 = depth3
        self.depth_48 = depth4
        self.lifts = lifts
        self.trails = trails

    def print(self):
        print(
        'Temp: ' + self.temp +"\n"+
        'Depth total: ' + self.depth_total +"\n"+
        'Depth overnight: ' + self.depth_overnight +"\n"+
        'Depth 24hr: ' + self.depth_24 +"\n"+
        'Depth 48hr: ' + self.depth_48 +"\n"+
        'Lifts open: ' + self.lifts +"\n"+
        'Trails open: ' + self.trails +"\n"
        )

