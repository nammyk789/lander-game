'''
interfaces.py

contains a text and graphics class that creates an interface for users
to play the game in the lander.py module

 by Andy Exley and Nammy Kasaraneni
'''

import sys
import button as b
try: 
    import graphics
except ImportError:
    sys.stderr.write("Couldn't import graphics.py (the Zelle graphics module.)\n")
    sys.stderr.write("This is fine for Part I of the assignment.\n")
    sys.stderr.write("For Part II you should make sure that graphics.py" +
                             " is in the same directory as this code.\n\n")


class TextLanderInterface:
    """Text-based interface for lander game. Use this one for testing"""

    def show_info(self, lander):
        """Display lander's status to user"""
        print ("Lander Status: Altitude %d, Velocity %d, Fuel %d" % 
            (lander.get_altitude(), lander.get_velocity(), lander.get_fuel()))

    def get_thrust(self):
        """Get thrust amount from user"""
        amtstr = input("Thrust amount?")
        while not amtstr >= 0:
            print('Thrust amount has to be at least 0')
            amtstr = input("Thrust amount?")
        return int(amtstr)

    def show_crash(self):
        """Display to user that we crashed"""
        print("Crash! Oh noes!")

    def show_landing(self):
        """Display to user that we landed safely"""
        print("Hooray, the Eagle has landed!")

    def close(self):
        """Close the interface"""
        print("Goodbye")

class GraphicLanderInterface:
    """GraphicLanderInterface class is a graphical interface 
        for your lunar lander game"""

    def __init__(self):

        # initialize window
        self.win = graphics.GraphWin("Lunar Lander Game", 300, 500)
        
        # transform coordinates
        self.win.setCoords(0, -10, 300, 600)

        self.surface_polygon = self.create_surface()
        self.surface_polygon.draw(self.win)

        self.lander_polygon = None
        
        #creates thrust buttons
        self.thrust1 = b.Button(graphics.Point(250, 10), graphics.Point(290, 30), 'thrust 1')
        self.thrust1.label.setSize(7)
        self.thrust1.color('SpringGreen1')
        self.thrust2 = b.Button(graphics.Point(250, 40), graphics.Point(290, 60), 'thrust 2')
        self.thrust2.label.setSize(7)
        self.thrust2.color('PaleTurquoise1')
        self.thrust3 = b.Button(graphics.Point(250, 70), graphics.Point(290, 90), 'thrust 3')
        self.thrust3.label.setSize(7)
        self.thrust3.color('light coral')
        
        #creates no-thrust button
        self.no_thrust = b.Button(graphics.Point(10, 10), graphics.Point(50, 30), 'no thrust')
        self.no_thrust.label.setSize(7)
        self.no_thrust.color('red2')
        
        
        #info labels
        self.f_label = graphics.Text(graphics.Point(150, 450), '')
        self.alt_label = graphics.Text(graphics.Point(150, 400), '')
        self.v_label = graphics.Text(graphics.Point(150, 350), '')

        
        #intro buttons
        self.easy = b.Button(graphics.Point(130, 520), graphics.Point(180, 550), 'easy')
        self.easy.color('purple1')
        self.easy.label.setTextColor('snow')
        self.difficult = b.Button(graphics.Point(130, 420), graphics.Point(180, 450), 'difficult')
        self.difficult.color('purple4')
        self.difficult.label.setTextColor('snow')
        self.xxx = b.Button(graphics.Point(130, 320), graphics.Point(180, 350), 'XXX')
        self.xxx.color('gray1')
        self.xxx.label.setTextColor('snow')


    
    def show_intro(self):
        ''' intro screen in which player can choose between Buttons
        representing easy, difficult, or extremely difficult levels
        '''
        self.easy.draw(self.win)
        self.difficult.draw(self.win)
        self.xxx.draw(self.win)
        point = self.win.getMouse()
        
        warning = graphics.Text(graphics.Point(150, 100), 'please '\
                                    'choose difficulty')
        
        while self.easy.is_clicked(point) == False and \
        self.difficult.is_clicked(point) == False and \
        self.xxx.is_clicked(point) == False:
            warning = graphics.Text(graphics.Point(150, 100), 'please '\
                                    'choose difficulty')
            warning.draw(self.win)
            point = self.win.getMouse()
        
        warning.undraw()
            
        if self.easy.is_clicked(point) == True:
            
            self.easy.undraw()
            self.difficult.undraw()
            self.xxx.undraw()
           
            self.thrust1.draw(self.win)
            self.thrust2.draw(self.win)
            self.thrust3.draw(self.win)
            self.no_thrust.draw(self.win)
            self.f_label.draw(self.win)
            self.alt_label.draw(self.win)
            self.v_label.draw(self.win)
        
            return 1
        
        elif self.difficult.is_clicked(point) == True:
            
            self.easy.undraw()
            self.difficult.undraw()
            self.xxx.undraw()
            
            self.thrust1.draw(self.win)
            self.thrust2.draw(self.win)
            self.thrust3.draw(self.win)
            self.no_thrust.draw(self.win)
            self.f_label.draw(self.win)
            self.alt_label.draw(self.win)
            self.v_label.draw(self.win)
        
            return 2
        
        else:
            
            self.easy.undraw()
            self.difficult.undraw()
            self.xxx.undraw()
           
            self.thrust1.draw(self.win)
            self.no_thrust.draw(self.win)
            self.f_label.draw(self.win)
            self.alt_label.draw(self.win)
            self.v_label.draw(self.win)
        
            return 3
        
        
    def show_info(self, lander):
        """This method currently gets the lander info then draws it.
        That's it. It doesn't actually show any information."""
        alt = lander.get_altitude()

        # if lander polygon is drawn, undraw it
        if self.lander_polygon:
            self.lander_polygon.undraw()
        
        fuel = 'FUEL: ' + str(lander.get_fuel())
        altitude = 'ALTITUDE: ' + str(lander.get_altitude())
        velocity = 'VELOCITY: ' + str(lander.get_velocity())
            
        self.f_label.setText(fuel)
        self.alt_label.setText(altitude)
        self.v_label.setText(velocity)
        
        self.lander_polygon = graphics.Polygon(graphics.Point(self.win.width / 2 - 10, alt),
                graphics.Point(self.win.width/2 - 3, alt + 10),
                graphics.Point(self.win.width/2 + 3, alt + 10),
                graphics.Point(self.win.width/2 + 10, alt))
        self.lander_polygon.setFill("blue")
        self.lander_polygon.draw(self.win)
        

    def get_thrust(self, difficulty):
        """waits for a user's mouse click, depending on which button 
        is hit (thrust/no thrust) returns 1 or 0 """
       
        # user clicks
        point = self.win.getMouse()
        
        while self.thrust1.is_clicked(point) == False and \
        self.thrust2.is_clicked(point) == False and \
        self.thrust3.is_clicked(point) == False and \
        self.no_thrust.is_clicked(point) == False:
            warning = graphics.Text(graphics.Point(150, 100), 'please '\
                                    'click either thrust or no thrust')
            warning.draw(self.win)
            point = self.win.getMouse()
            
        if difficulty == 1:   
            if self.thrust1.is_clicked(point) == True:
                return 1
            elif self.thrust2.is_clicked(point) == True:
                return 3
            elif self.thrust3.is_clicked(point) == True:
                return 5
            elif self.no_thrust.is_clicked(point) == True:
                return 0
            
        elif difficulty == 2:   
            if self.thrust1.is_clicked(point) == True:
                return 1
            elif self.thrust2.is_clicked(point) == True:
                return 5
            elif self.thrust3.is_clicked(point) == True:
                return 10
            elif self.no_thrust.is_clicked(point) == True:
                return 0
        else:
            self.thrust2.undraw()
            self.thrust3.undraw()
            if self.thrust1.is_clicked(point) == True:
                return 10
            elif self.no_thrust.is_clicked(point) == True:
                return 0
            
    def score(self, lander):
        '''creates final score for the game
        '''
        score = -1 * (lander.fuel + lander.velocity)
        final_score = 'SCORE: ' + str(score)
        score_text = graphics.Text(graphics.Point(150, 100), final_score)
        score_text.draw(self.win)

    def show_crash(self, lander):
        """Crash message"""
        crash = graphics.Text(graphics.Point(150, 200), "Crash! Oh noes!")
        crash.setTextColor('red1')
        crash.draw(self.win)
        self.score(lander)

    def show_landing(self, lander):
        """Landing message"""
        land = graphics.Text(graphics.Point(150, 100), "Hooray, Firefly has landed!")
        land.setTextColor('green1')
        land.draw(self.win)
        self.score(lander)
    
    
    def close(self):
        point = self.win.getMouse()
        while True:
            self.win.close()

    def create_surface(self):
        """Draws the surface of the moon"""
        circle = graphics.Circle(graphics.Point(150,-50), 100)
        circle.setFill("gray")
        return circle
