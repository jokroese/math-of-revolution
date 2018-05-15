from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.UserParam import UserSettableParameter
from mesa.visualization.modules import ChartModule

from .model import CivilViolenceModel
from .agent import Citizen, Cop


COP_COLOR = "Black"
AGENT_QUIET_COLOR = "Blue"
AGENT_REBEL_COLOR = "Red"
JAIL_COLOR = "Grey"


def citizen_cop_portrayal(agent):
    if agent is None:
        return

    portrayal = {"Shape": "circle",
                 "x": agent.pos[0], "y": agent.pos[1],
                 "Filled": "true"}

    if type(agent) is Citizen:
        color = AGENT_QUIET_COLOR if agent.condition == "Quiescent" else \
            AGENT_REBEL_COLOR
        color = JAIL_COLOR if agent.jail_sentence else color
        portrayal["Color"] = color
        portrayal["r"] = 0.8
        portrayal["Layer"] = 0

    elif type(agent) is Cop:
        portrayal["Color"] = COP_COLOR
        portrayal["r"] = 0.5
        portrayal["Layer"] = 1
    return portrayal

height=70
width=70

model_params = {
    'height':height,
    'width':width,
    # 'height': UserSettableParameter('slider', 'Height', 40, 10, 100, 1,
    #                                                description='Citizen Density'),
    # 'width': UserSettableParameter('slider', 'Width', 40, 10, 100, 1,
    #                                                description='Citizen Density'),
    'citizen_density': UserSettableParameter('slider', 'Citizen Density', 0.7, 0.0, 1, 0.01,
                                                   description='Citizen Density'),
    'cop_density': UserSettableParameter('slider', 'Cop Density', 0.1, 0.0, 1, 0.01,
                                                 description='Cop Density'),
    'citizen_vision': UserSettableParameter('slider', 'Citizen Vision', 7, 0, 20, 1,
                                             description='Citizen vision'),
    'cop_vision': UserSettableParameter('slider', 'Cop Vision', 7, 0, 20, 1,
                                             description='Cop Vision'),
    'legitimacy': UserSettableParameter('slider', 'Legitimacy', 0.8, 0.0, 1.0, 0.01,
                                             description='Legitimacy'),
    'max_jail_term': UserSettableParameter('slider', 'Max Jail Term', 1000, 0, 10000, 1,
                                           description='Max Jail Term')
}

chart = ChartModule([{"Label": "Active",
                      "Color": "Red"}],
                    data_collector_name='datacollector')

canvas_element = CanvasGrid(citizen_cop_portrayal, model_params['height'], model_params['height'], 700, 700)
server = ModularServer(CivilViolenceModel, [canvas_element, chart],
                       "Epstein Civil Violence", model_params)
