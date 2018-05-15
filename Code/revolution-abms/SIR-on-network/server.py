import math

from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule
from mesa.visualization.modules import TextElement
from mesa.visualization.UserParam import UserSettableParameter
from mesa.visualization.modules import NetworkModule

from model import VirusModel, State, number_infected


def network_portrayal(G):
    # The model ensures there is always 1 agent per node

    def node_color(agent):
        if agent.state is State.INFECTED:
            return 'RED'
        elif agent.state is State.SUSCEPTIBLE:
            return 'GREEN'
        else:
            return 'GREY'

    # if disease can be transmitted down it, draw the line solid, else grey
    def edge_color(agent1, agent2):
        if (agent1.state is State.SUSCEPTIBLE and agent2.state is not State.REMOVED) \
        or (agent2.state is State.SUSCEPTIBLE and agent1.state is not State.REMOVED):
            return '#000000'
        return '#e8e8e8'

    def edge_width(agent1, agent2):
        if (agent1.state is State.SUSCEPTIBLE and agent2.state is not State.REMOVED) \
        or (agent2.state is State.SUSCEPTIBLE and agent1.state is not State.REMOVED):
            return 2
        return 3


    portrayal = dict()
    portrayal['nodes'] = [{'id': n_id,
                           'agent_id': n['agent'][0].unique_id,
                           'size': 5,
                           'color': node_color(n['agent'][0]),
                           }
                          for n_id, n in G.nodes(data=True)]

    portrayal['edges'] = [{'id': i,
                           'source': source,
                           'target': target,
                           'color': edge_color(G.node[source]['agent'][0], G.node[target]['agent'][0]),
                           'width': edge_width(G.node[source]['agent'][0], G.node[target]['agent'][0]),
                           }
                          for i, (source, target, _) in enumerate(G.edges(data=True))]

    return portrayal


network = NetworkModule(network_portrayal, 500, 500, library='d3')
chart = ChartModule([{'Label': 'Susceptible', 'Color': '#ADD694'},
                     {'Label': 'Infected', 'Color': '#F2728C'},
                     {'Label': 'Removed', 'Color': ' #67B8C7'}])


class RatioElement(TextElement):
    def render(self, model):
        ratio = model.removed_susceptible_ratio()
        ratio_text = '&infin;' if ratio is math.inf else '{0:.2f}'.format(ratio)
        return 'Removed/Susceptible Ratio: ' + ratio_text

class InfectedRemainingElement(TextElement):
    def render(self, model):
        infected = number_infected(model)
        return 'Infected Remaining: ' + str(infected)

class BasicReproductionNumber(TextElement):
    def render(self, model):
        R_0 = ((model.num_nodes-model.initial_outbreak_size)/model.num_nodes)*(model.beta/model.alpha)
        return 'Basic Reproduction Number, R₀: ' + str(R_0)[0:4]

text = BasicReproductionNumber(), RatioElement(), InfectedRemainingElement()

model_params = {
    'num_nodes': UserSettableParameter('slider', 'Number of agents', 70, 10, 100, 1,
                                       description='Choose how many agents to include in the model'),
    'avg_node_degree': UserSettableParameter('slider', 'Avg Node Degree', 3, 3, 8, 1,
                                             description='Avg Node Degree'),
    'initial_outbreak_size': UserSettableParameter('slider', 'Initial Outbreak Size', 1, 1, 10, 1,
                                                   description='Initial Outbreak Size'),
    'beta': UserSettableParameter('slider', 'Virus Spread Chance', 0.06, 0.0, 1.0, 0.01,
                                                 description='Probability that susceptible neighbor will be infected'),
    'alpha': UserSettableParameter('slider', 'Recovery Chance', 0.04, 0.0, 1.0, 0.01,
                                             description='Probability that the virus will be removed'),
}

server = ModularServer(VirusModel, [network, chart, *text], 'SIR Model', model_params)
server.port = 8521