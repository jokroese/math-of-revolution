from .agent import Citizen, Cop

COP_COLOR = "Black"
AGENT_QUIET_COLOR = "Blue"
AGENT_REBEL_COLOR = "Green"
JAIL_COLOR = "Purple"


def citizen_cop_portrayal(agent):
    if agent is None:
        return

    portrayal = {"Shape": "circle",
                 "x": agent.pos[0], "y": agent.pos[1],
                 "Filled": "true"}

    if isinstance(agent, Citizen):
        color = AGENT_QUIET_COLOR if agent.condition == "Quiescent" else \
            AGENT_REBEL_COLOR
        color = JAIL_COLOR if agent.jail_sentence else color
        portrayal["Color"] = color
        portrayal["r"] = 0.8
        portrayal["Layer"] = 0

    elif isinstance(agent, Cop):
        portrayal["Color"] = COP_COLOR
        portrayal["r"] = 0.5
        portrayal["Layer"] = 1
    return portrayal
