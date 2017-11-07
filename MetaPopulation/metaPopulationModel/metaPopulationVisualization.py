from mesa.visualization.ModularVisualization import VisualizationElement

class MetaPopulationVisualization(VisualizationElement):
    """ A CanvasHexGrid object functions similarly to a CanvasGrid object. It takes a portrayal dictionary and talks to HexDraw.js to draw that shape.

    A portrayal as a dictionary with the following structure:
        "x", "y": Coordinates for the circle.
        "radius": The radius of the habitat.
        "population" : The population of the habitat.
        "K" : The carrying capacity of the habitat.
        "percent" : The percent filled the habitat is.
        "type" : what kind of object (always "habitat")




    Attributes:
        portrayal_method: Function which generates portrayals from objects, as
                          described above.
        grid_height, grid_width: Size of the grid to visualize, in cells.
        canvas_height, canvas_width: Size, in pixels, of the grid visualization
                                     to draw on the client.
        template: "canvas_module.html" stores the module's HTML template.

    """
    package_includes = []
    local_includes = ["d3.js","MetaPopDraw.js"]
    portrayal_method_habitat = None
    portrayal_method_animal = None

    def __init__(self, portrayal_method_habitat, portrayal_method_animal,
                 space_width, space_height, canvas_width=500, canvas_height=500):
        """ Instantiate a new MetaPopulationVisualization

        Args:
            portrayal_method_habitat: a function to convert each habitat into a portrayal, as
                described above.
            space_width, space_height: size of the space
            canvas_height, canvas_width: Size of the canvas to draw in the
                                         client, in pixels. (default: 500x500)
        """

        self.portrayal_method_habitat = portrayal_method_habitat
        self.portrayal_method_animal = portrayal_method_animal
        self.space_width = space_width
        self.space_height = space_height
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height

        new_element = ("new MetaPopulationVisualization({}, {}, {}, {})"
            .format(self.space_width, self.space_height,
                self.canvas_width, self.canvas_height))

        self.js_code = "elements.push(" + new_element + ");"

    def render(self, model):
        out = {
            "habitats" : [self.portrayal_method_habitat(hab) for hab in model.habitats],
            "animals" : [self.portrayal_method_animal(animal) for animal in model.animals]
        }
        # print(out)
        return out
