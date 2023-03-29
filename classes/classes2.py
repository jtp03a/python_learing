import math

# Refer to README.md for the problem instructions

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100.0
        self.x_pos = 0.0
        self.y_pos = 0.0
        self.dmg_reduc = 0.5
        
    def report_pos(self):
        return (self.x_pos, self.y_pos)
    
    def reduce_health(self, dmg):
        dmg_taken = dmg * self.dmg_reduc
        if (self.health - dmg_taken <= 0):
            self.health = 0.0
        else:
            self.health -= dmg_taken
    
    def move(self, x_pos, y_pos):
        distance = math.sqrt((x_pos * x_pos) + (y_pos * y_pos))
        
        print(distance)
        
        self.x_pos += x_pos
        self.y_pos += y_pos
        
        if (y_pos < 0 ):
            if (distance >= 5):
                self.reduce_health(distance)
                if (self.health == 0):
                    print("Your are out of health!")
        
        return self.health
        
    
paladin = Player("Jake")

pos = paladin.report_pos()

paladin.reduce_health(50)

curr_hp = paladin.health

print(f'Current hp is: {curr_hp}, Exp: 75.0')

paladin.move(125, -125)

print(f'Current hp is: {paladin.health}')

print(paladin.report_pos())
