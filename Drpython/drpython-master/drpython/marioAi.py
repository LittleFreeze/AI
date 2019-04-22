#gets the proper imports for this 
from sklearn import tree
from joblib import dump, load
import pygame

class AiPlayer():
    
    def __init__(self):

        
        ##gets the predefined tree
##        
##        theTree = tree.DecisionTreeClassifier()
##        fileName = 'doc.joblib'
##        theTree = load(fileName)

        filename = "dr"
        X = []
        try:
            f = open(filename + ".txt","r")
        except:
            print("File name not found.")
            return
        for line in f:
            l = line
            try:
                x = [int(i) for i in l.split()]
            except:
                print("The tree only accepts integer training data")
                return
            X.append(x)
        f.close()

        filename2 = "mar"
        Y = []
        try:
            f2 = open(filename2 + ".txt","r")
        except:
            print("File name not found.")
            return
        for line2 in f2:
            Y.append(line2.strip())
        f2.close()
        self._theTree = tree.DecisionTreeClassifier()
        self._theTree = self._theTree.fit(X,Y)
        print("Tree created")

    def sameColor():
        #gets color
        a, b = self.brick.blocks
        color = a.color

        ##rotates to be vertical
        self.rotate()

        #finds the goal based on color
        if color == RED:
            xGoal = 0
        elif color == BLUE:
            xGoal = 1
        else:
            xGoal = 2

        #the starting location
        cur = 3

        #moves left till it hits goal
        while (xGoal != cur):
            self.moveLeft()
            cur = cur - 1

    def moveLeft(self):
        ev = pygame.event.Event(pygame.KEYDOWN)
        ev.key = pygame.K_LEFT
        pygame.event.post(ev)
        
    def rotate(self):
        ev = pygame.event.Event(pygame.KEYDOWN)
        ev.key = pygame.K_SPACE
        pygame.event.post(ev)

    def rbColor():
        a, b = self.brick.blocks
        LColor = a.color

        if LColor == BLUE:
            self.rotate()
            self.rotate()
        
        self.moveLeft()
        self.moveLeft()
        self.moveLeft()


    def byColor():
        a, b = self.brick.blocks
        LColor = a.color

        if LColor == YELLOW:
            self.rotate()
            self.rotate()

        self.moveLeft()
        self.moveLeft()

    def ryColor():
        a, b = self.brick.blocks
        LColor = a.color

        if LColor == RED:
            self.rotate()
            self.rotate()

        self.moveLeft()


    def aiMain(self,LColor, RColor):
        ##gets the color of both sides of the pill
##        a, b = self.brick.blocks
##        LColor = a.color
##        RColor = b.color

        ##checks tree for what function is needed
        ans = self._theTree.predict([[LColor, RColor]])

        #calls a function based on the the predict
        if ans == 1:
            sameColor()
        elif ans == 2:
            rbColor()
        elif ans == 3:
            byColor()
        elif ans == 4:
            ryColor()

    @property
    def theTree(self):
        return self._theTree


