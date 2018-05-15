# SIR on a network

## Summary

An Agent-based model that adapts the compartmental SIR model to a network.

This uses [mesa](https://github.com/projectmesa/mesa) for the ABM, [networkx](https://networkx.github.io/) for the complex network aspect and [d3.js](https://d3js.org/) as the JavaScript library used to render the network.

## Installation

To install the dependencies use pip and the requirements.txt in this directory. e.g.

```
    $ pip install -r requirements.txt
```

## How to Run

To run the model interactively, run ``run.py`` in this directory. e.g.

```
    $ python run.py
```

Then open your browser to [http://127.0.0.1:8521/](http://127.0.0.1:8521/) and press Reset, then Run.

## Files

* ``run.py``: Launches a model visualization server.
* ``model.py``: Contains the agent class, and the overall model class.
* ``server.py``: Defines classes for visualizing the model (network layout) in the browser via Mesa's modular server, and instantiates a visualization server.

## Further Reading

An intro tutorial to using mesa can be found at:
http://mesa.readthedocs.io/en/master/tutorials/intro_tutorial.html

This model was based on:
https://github.com/projectmesa/mesa/tree/master/examples/virus_on_network

Which references:
[Stonedahl, F. and Wilensky, U. (2008). NetLogo Virus on a Network model](http://ccl.northwestern.edu/netlogo/models/VirusonaNetwork). 
Center for Connected Learning and Computer-Based Modeling, Northwestern University, Evanston, IL.
and
[Wilensky, U. (1999). NetLogo](http://ccl.northwestern.edu/netlogo/)
Center for Connected Learning and Computer-Based Modeling, Northwestern University, Evanston, IL.

For a good intro to mathematical epidemiology, see:
[Brauer, Fred, and Carlos Castillo-Chavez. (2013). Mathematical Models for Communicable Diseases. Society for Industrial and Applied Mathematics.

