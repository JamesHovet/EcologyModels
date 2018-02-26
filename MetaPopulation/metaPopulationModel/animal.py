from mesa import Agent
import random
import math
# from mesa.space import ContinuousSpace

class Animal(Agent):
    '''Represents a single animal outside of any habitat'''

    def __init__(self, model, pos, theta, original):
        super().__init__(pos, model)
        self.x, self.y = pos
        self.pos = pos
        self.theta = theta
        self.original = original
        self._nextPosition = pos
        self._nextAlive = True # _variable is common practice to let the coder know that a varibale should only be used within the class definition, not messed with by other parts of the code

    def step(self):


        #check if dead
        if random.random() < self.model.wildernessDeath:
            self._nextAlive = False
            return

        #move
        self.theta = self.theta + (random.random() - 0.5) * self.model.thetaRange
        distance = self.model.movementDistance
        self._nextPosition = (self.x + distance * math.cos(self.theta), self.y + distance * math.sin(self.theta))

        #if out of bounds, die
        if self.model.space.out_of_bounds(self._nextPosition):
            self._nextAlive = False

        #check if in habitat
        for hab in self.model.habitats:
            if self.model.space.get_distance(self.pos, (hab.x,hab.y)) < hab.radius:
                hab.population += 1
                self._nextAlive = False
                # print("absorbed by",hab)
                if self.original != hab.ID:
                    hab.geneticDiversity += self.model.geneticDiversityAdded
                return #break out of the function early

    def advance(self):
        if self._nextAlive:
            # print(self._nextPosition)
            self.model.space.move_agent(self, self._nextPosition)
            self.pos = self._nextPosition
            self.x, self.y = self._nextPosition
        else:
            self.model.animals.remove(self)
            self.model.schedule.remove(self)
