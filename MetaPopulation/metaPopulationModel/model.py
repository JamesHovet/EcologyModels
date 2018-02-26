from mesa import Model
from mesa.time import SimultaneousActivation
from mesa.space import ContinuousSpace
from mesa.datacollection import DataCollector
import mesa
import math
import random

from metaPopulationModel.habitat import Habitat
from metaPopulationModel.animal import Animal

class MetaPopulationModel(Model):
    '''
    Represents the collection of all the habitats and animals and the space they live in
    '''

    def __init__(self, height, width, habitats, dispersalProb, deathProb, birthProb, thetaRange, movementDistance, wildernessDeath, geneticDiversityAdded, densityIndependentMortality, birthStdDev, minStablePopulation):
        '''
        Create a new model with a width, height, and a list of habitats
        '''

        self.dispersalProb = dispersalProb
        self.deathProb = deathProb
        self.birthProb = birthProb
        self.thetaRange = math.radians(thetaRange)
        self.movementDistance = movementDistance
        self.wildernessDeath = wildernessDeath
        self.geneticDiversityAdded = geneticDiversityAdded
        self.densityIndependentMortality = densityIndependentMortality
        self.birthStdDev = birthStdDev
        self.minStablePopulation = minStablePopulation

        self.habitats = []
        self.animals = []

        self.schedule = SimultaneousActivation(self)

        self.space = ContinuousSpace(height, width, torus=True)

        self.datacollector = DataCollector(
                model_reporters={"totalPopulation": lambda m: sum([h.population for h in self.habitats])}
                # agent_reporters={"population": lambda a: a.population}
            )

        ##create habitats

        habID = 0

        for hab in habitats:
            x = hab["x"]
            y = hab["y"]
            r = hab["r"]
            K = hab["K"]
            initialPopulation = hab["initialPopulation"]
            newHabitat = Habitat(self, (x,y), r, K, initialPopulation, habID)
            self.space.place_agent(newHabitat, (x,y))
            self.schedule.add(newHabitat)
            self.habitats.append(newHabitat)
            habID += 1

        self.running = True

    def step(self):
        '''
        Have the scheduler advance each cell by one step
        '''
        self.schedule.step()
        self.datacollector.collect(self)

    def spawnNew(self, n, pos, radius, ID):
        print("spawing",n,"new at",pos)

        radius = radius + 1
        for i in range(n):
            randomTheta = random.random() * math.pi * 2
            newPosition = (pos[0] + radius * math.cos(randomTheta), pos[1] + radius * math.sin(randomTheta))
            newAnimal = Animal(self, newPosition, randomTheta, ID)
            self.animals.append(newAnimal)
            self.space.place_agent(newAnimal, newPosition)
            self.schedule.add(newAnimal)
