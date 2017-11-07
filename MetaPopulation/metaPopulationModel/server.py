from mesa.visualization.ModularVisualization import ModularServer

# from metaPopulationModel.portrayal import portrayModel
from metaPopulationModel.model import MetaPopulationModel
from metaPopulationModel.portrayal import portrayHabitat
from metaPopulationModel.portrayal import portrayAnimal
from metaPopulationModel.metaPopulationVisualization import MetaPopulationVisualization
from mesa.visualization.UserParam import UserSettableParameter
import math

class Variables():
    def __init__(self, dispersalProb, deathProb, birthProb):
        self.dispersalProb = dispersalProb
        self.deathProb = deathProb
        self.birthProb = birthProb


habitats = [
    {
        "x": 50,
        "y": 50,
        "r": 10, #radius
        "K": 400,
        "initialPopulation" : 300
    },
    {
        "x": 200,
        "y": 200,
        "r": 15, #radius
        "K": 400,
        "initialPopulation" : 200
    },
    {
        "x": 50,
        "y": 200,
        "r": 20, #radius
        "K": 500,
        "initialPopulation" : 200
    },
    {
        "x": 100,
        "y": 100,
        "r": 20, #radius
        "K": 500,
        "initialPopulation" : 200
    }
]

space_width = 300
space_height = 300

dispersal_slider = UserSettableParameter('slider', "dispersal percentage", 0.05, 0.01, 0.2, 0.01)
death_slider = UserSettableParameter('slider', "death percentage", 0.1, 0, 1, 0.05)
birth_slider = UserSettableParameter('slider', "birth percentage", 1.2, 0, 2, 0.05)
theta_slider = UserSettableParameter('slider', "theta range (degrees)", 30, 0, 360, 5)
movement_slider = UserSettableParameter('slider', "movement range", 5, 2, 10, 0.1)
wildernessDeath_slider = UserSettableParameter('slider', "wilderness death percentage", 0.1, 0, 1, 0.05)
geneticDiversityAdded_slider = UserSettableParameter('slider', "genetic diversity added", 1, 0, 1, 0.05)
geneticDiversityDecay_slider = UserSettableParameter('slider', "genetic diversity decay", 0.01, 0, 0.1, 0.001)
densityIndependentMortality_slider = UserSettableParameter('slider', "density independent mortality", 0.02, 0, 0.05, 0.001)
birthStdDev_slider = UserSettableParameter('slider', 'birth rate standard deviation', 0.001, 0, 0.01, 0.0005)
minStablePopulation_slider = UserSettableParameter('slider', "minimum genetically stable population", 500, 200, 1000, 50)

element = MetaPopulationVisualization(
    portrayHabitat,
    portrayAnimal,
    space_width, space_height,
    canvas_width=800, canvas_height=800)

server = ModularServer(
    MetaPopulationModel,
    [element],
    "MetaPopulationModel",
    {
        "height" : space_width,
        "width" : space_height,
        "habitats" : habitats,
        "dispersalProb" : dispersal_slider,
        "deathProb" : death_slider,
        "birthProb" : birth_slider,
        "thetaRange" : theta_slider,
        "movementDistance" : movement_slider,
        "wildernessDeath" : wildernessDeath_slider,
        "geneticDiversityAdded" : geneticDiversityAdded_slider,
        "geneticDiversityDecay" : geneticDiversityDecay_slider,
        "densityIndependentMortality" : densityIndependentMortality_slider,
        "birthStdDev" : birthStdDev_slider,
        "minStablePopulation" : minStablePopulation_slider
    })
