import os
print("run.py", os.path.dirname(os.path.realpath(__file__)))

from metaPopulationModel.server import server

server.launch()
