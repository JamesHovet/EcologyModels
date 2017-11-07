def portrayHabitat(habitat):
    '''
    This function is registered with the visualization server to be called
    each tick to indicate how to draw the habitat in its current state.
    :param cell:  the cell in the simulation
    :return: the portrayal dictionary.
    '''
    assert habitat is not None
    return {
        "type" : "habitat",
        "x" : habitat.x,
        "y" : habitat.y,
        "radius" : habitat.radius,
        "population" : habitat.population,
        "K" : habitat.K,
        "percent" : habitat.population/habitat.K,
        "geneticDiversity" : habitat.geneticDiversity

    }


def portrayAnimal(animal):
    '''
    This function is registered with the visualization server to be called
    each tick to indicate how to draw the habitat in its current state.
    :param cell:  the cell in the simulation
    :return: the portrayal dictionary.
    '''
    assert animal is not None
    return {
        "type" : "animal",
        "x" : animal.x,
        "y" : animal.y,
        "theta" : animal.theta
    }
