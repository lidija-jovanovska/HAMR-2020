# Chord progression generation using complex networks

## Motivation

The idea for this project was conceived for the HAMR hackathon, that was part of the ISMIR 2020 conference. Research crossing the fields of network science and MIR & musicology is relatively scarce. By representing specific entities (i.e. chords, notes, keys...) and relationships between them with the help of networks we can utilize the plethora of research methods that have been developed in that field. With our project all we did is scratch the surface, but we are hoping that this endeavour will inspire musicologists and network scientists alike to investigate even further. 

## Description

### The graph

The repo includes the [graph](https://github.com/lidija-jovanovska/HAMR-2020/blob/main/chord_progressions_network.gexf) generated using data from [Ultimate Guitar](https://www.ultimate-guitar.com). The data consists of __~15,000 songs__, which were preprocessed in order to obtain only the chord progressions. In the generated network all of the unique chords in the corpus are represented with nodes which are connected if there exists a transition from one chord to another. The link weights represent the statistical probability for a transition (calculated based on the data). As such, the network is formally defined as a __directed, weighted graph__. 

### The code

After doing an analysis of the graph, we wanted to experiment with different models for generating chord progressions. Both models are implemented in this [script](https://github.com/lidija-jovanovska/HAMR-2020/blob/main/generate_progressions.py). The first model is a simple __random walk__ using the link weights (transition probabilities) to traverse the graph. If the starting chord is not provided, the model selects the first chord based on its pagerank value. The second model, called __"smart" walk__, is somewhat more complex as it also takes into account the community structure of the network. Additionaly, we define a threshold based on which we decide whether we stay or leave the current community.

## How to use?

You can try generating chord progressions yourself using our [demo](https://colab.research.google.com/drive/1zr-yTdOp2xdnS_XYG4hQ1bh6QBEflASU)

## Feedback

We are open for potential tweaks and improvements. You are welcome to send your feedback to : lidija.jovanovska@outlook.com or bojanevkoski@outlook.com
