# The Copter with NEAT

![](https://img.shields.io/badge/Python-3-green.svg?style=for-the-badge&logo=python)

Copter is a simple game. Rules are simple, you only have to dodge the ghosts and don't crash to upper and lower screens but trick is in movement of copter. It only moves down by default, so to move it upwards, you have to hold space bar for it.

So, in the title, "The Copter" part is clear. But what is "NEAT?"
## What is NEAT?

NEAT stands for NeuroEvolution of Augmenting Topologies , it is a genetic algorithm (GA) for the generation of evolving artificial neural networks (a neuroevolution technique) developed by Ken Stanley in 2002.

It alters both the weighting parameters and structures of networks, attempting to find a balance between the fitness of evolved solutions and their diversity. It is based on applying three key techniques:

- tracking genes with history markers to allow crossover among topologies.
- applying speciation (the evolution of species) to preserve innovations.
- developing topologies incrementally from simple initial structures.

## Performance

On simple control tasks, the NEAT algorithm often arrives at effective networks more quickly than other contemporary neuro-evolutionary techniques and reinforcement learning methods.

## Algorithm

Traditionally a neural network topology is chosen by a human experimenter, and effective connection weight values are learned through a training procedure. This yields a situation whereby a trial and error process may be necessary in order to determine an appropriate topology. NEAT is an example of a topology and weight evolving artificial neural network (TWEANN) which attempts to simultaneously learn weight values and an appropriate topology for a neural network.

In order to encode the network into a phenotype for the GA, NEAT uses a direct encoding scheme which means every connection and neuron is explicitly represented. This is in contrast to indirect encoding schemes which define rules that allow the network to be constructed without explicitly representing every connection and neuron allowing for more compact representation.

The NEAT approach begins with a perceptron-like feed-forward network of only input neurons and output neurons. As evolution progresses through discrete steps, the complexity of the network's topology may grow, either by inserting a new neuron into a connection path, or by creating a new connection between (formerly unconnected) neurons.


So, what is the use of that in this game? So basically, with the help of this algorithm, your computer by itself will play this game.

**For, more information about the algorithm, you can read the [official research paper](http://nn.cs.utexas.edu/downloads/papers/stanley.ec02.pdf)**


## References

- [NEAT: An Awesome Approach to NeuroEvolution](https://towardsdatascience.com/neat-an-awesome-approach-to-neuroevolution-3eca5cc7930f)

- [neat-python](https://github.com/CodeReclaimers/neat-python)

## Implementation
![Demo](demo.gif)

**Want to play the original game?**:smiley:[Check this out](https://github.com/iamAbhishekkumar/The-Copter)

## TODO

- Make a graph, for easy visualization, what is happeing inside the neural netwok.

**If you like it, :star:this repo :upside_down_face:**

**If you find any issues, feel free to raise issues. Enjoy!:smile:**
