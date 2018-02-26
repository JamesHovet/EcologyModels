from mesa import Agent
import math
import random

class Habitat(Agent):
    '''Represents a Habitat'''

    def __init__(self, model, pos, radius, K, initialPopulation, ID):
        '''
        Create a habitat with a position, radius, K (carrying capacity), and initial population
        and initialize all of the
        '''
        super().__init__(pos, model)
        self.x, self.y = pos #unwrap the position tuple into the x and y components. (a tuple is kind of like a vector, it has multiple components)
        self.radius = radius
        self.K = K
        self.ID = ID
        self.geneticDiversity = 1
        self.population = initialPopulation
        self.densityIndependentMortality = model.densityIndependentMortality
        self.birthStdDev = model.birthStdDev
        self._nextPopulation = None
        self._nextDispersal = 0 # _variable is common practice to let the coder know that a varibale should only be used within the class definition, not messed with by other parts of the code

    def step(self):
        '''
        Compute the population at the next time step.

        P_next = P_current - dispersed - dead + births (as f of population and heterozygosity)
        '''

        population = self.population

        dispersalProb = self.model.dispersalProb
        self._nextDispersal = sum([random.random() < dispersalProb for i in range(population)])

        deathProb = self.model.deathProb
        deaths = sum([random.random() < deathProb for i in range(population)])

        if self.geneticDiversity > 1:
            self.geneticDiversity = 1

        lossOfHeterozygosity = .5 - (self.population * (1/(self.model.minStablePopulation * 2)))

        if lossOfHeterozygosity < 0:
            lossOfHeterozygosity = 0

        self.geneticDiversity -= lossOfHeterozygosity

        if self.geneticDiversity < 0:
            self.geneticDiversity = 0

        rawBirthProb = sampleFromNormal(self.model.birthProb, self.birthStdDev)

        rawBirthProb = rawBirthProb * self.geneticDiversity

        birthProb = (rawBirthProb * population * (1-(population/self.K)))/population if population > 0 else 0

        print("pop",self.population, "lossOfHetero",lossOfHeterozygosity, "diversity",self.geneticDiversity, "rawBirth", rawBirthProb, "birth",birthProb)

        births = sum([random.random() < birthProb for i in range(population)])

        densityIndependentDeaths = math.ceil(population * self.densityIndependentMortality)

        self._nextPopulation = population - densityIndependentDeaths - self._nextDispersal - deaths + births

        # if self.geneticDiversity > 1:
        #     self.geneticDiversity = 1
        # self.geneticDiversity -= self.model.geneticDiversityDecay
        #
        # if self.geneticDiversity > 0:
        #     self._nextPopulation = population - deaths + births
        # else:
        #     self._nextPopulation = 0




    def advance(self):
        '''
        Set the state to the new computed state -- computed in step().
        '''
        self.population = self._nextPopulation
        self.model.spawnNew(self._nextDispersal, (self.x,self.y), self.radius, self.ID)



def sampleFromNormal(mean, sigma):
    return random.normalvariate(mean, sigma)
