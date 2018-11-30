'''
lander.py
A module for writing a Lunar Lander game

Authors: Andy Exley and Nammy Kasaraneni
'''

import interfaces

class LunarLander:
    '''creates a lunar lander and keeps track of its attributes
    '''
    def __init__(self, alt, vel, fuel):
        '''Constructor for a LunarLander object'''
        self.altitude = alt
        self.velocity = vel
        self.fuel = fuel

    def get_altitude(self):
        '''Returns this LunarLander's altitude'''
        return self.altitude

    def get_velocity(self):
        '''Returns this LunarLander's velocity'''
        return self.velocity

    def get_fuel(self):
        '''Returns this LunarLander's fuel'''
        return self.fuel

    def update(self, thrustamount):
        '''Update LunarLander attributes after some fuel is spent to fire
        the engine.'''
        # 1. Expend thrustamount units of fuel, or what is left
        if thrustamount > self.fuel:
            thrustamount = self.fuel
        self.fuel = self.fuel - thrustamount

        # 2. For each unit of fuel burnt, increase ship velocity by 4
        self.velocity = self.velocity + 4 * thrustamount

        # 3. Gravity
        self.velocity = self.velocity - 2

        # 4. Calculate new altitude
        self.altitude = self.altitude + self.velocity


class LanderGame:
    '''This class represents a Lunar Lander Game
    '''

    def __init__(self):
        '''Constructor for the game'''
        self.interface = interfaces.GraphicLanderInterface()
        self.lander = LunarLander(200, 0, 30)

    def play(self):
        '''This is the method that plays the game'''
        difficulty = self.interface.show_intro()
        while self.lander.get_altitude() > 0:
            self.interface.show_info(self.lander)
            amt = self.interface.get_thrust(difficulty)
            self.lander.update(amt)
            
        if self.lander.get_velocity() < -10:
            self.interface.show_crash(self.lander)
        else:
            self.interface.show_landing(self.lander)
        
        self.interface.close()

def main():
    game = LanderGame()
    game.play()

if __name__ == '__main__':
    main()
