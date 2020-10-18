import networkx as nx
import numpy as np
from cdlib import algorithms


def random_walk(chord_graph, start_chord=None, progression_length=4):
    chord_path = []
    current_chord = start_chord

    if current_chord == None:
        pagerank = list(nx.get_node_attributes(chord_graph, "pagerank").values())
        pagerank = np.array(pagerank) / sum(pagerank)  # normalizing pagerank values to get probability distr.
        current_chord = np.random.choice(a=list(chord_graph.nodes), p=pagerank)
    neighboring_chords = list(chord_graph.neighbors(current_chord))

    for chord_step in range(progression_length):
        chord_path.append(current_chord)
        weights = [chord_graph[current_chord][neighboring_chord]['weight']
                   for neighboring_chord in list(neighboring_chords)]
        weights = np.array(weights) / sum(weights)
        current_chord = np.random.choice(a=neighboring_chords, p=weights)
        neighboring_chords = list(chord_graph.neighbors(current_chord))

    return chord_path


def smart_walk(chord_graph, start_chord=None, progression_length=4, out_threshold=0.85):
    communities = algorithms.louvain(chord_graph.to_undirected())
    chord_path = []
    visited_chords = []
    current_chord = start_chord
    
    if current_chord == None:
        pagerank = np.array(list(nx.get_node_attributes(chord_graph, "pagerank", ).values()))
        pagerank = np.array(pagerank) / sum(pagerank)  # normalizing pagerank values to get probability distr.
        current_chord = np.random.choice(a=list(chord_graph.nodes), p=pagerank)

    for chord_step in range(progression_length):
        chord_path.append(current_chord)
        visited_chords.append(current_chord)
        neighboring_chords = list(chord_graph.neighbors(current_chord))
        probabilities = []
        possible_next_chords = []
        rand = np.random.uniform(0, 1)
        if rand < out_threshold:
            community_index = [True if current_chord in community else False for community in
                               communities.communities].index(True)
            possible_next_chords = [chord for chord in neighboring_chords
                                    if chord in communities.communities[community_index]]
            if len(possible_next_chords) == 0:
                possible_next_chords = neighboring_chords
        else:
            possible_next_chords = neighboring_chords + visited_chords

        for chord in possible_next_chords:
            probabilities.append(int(chord_graph.in_degree(chord, weight='weight')))

        probabilities = np.array(probabilities) / sum(probabilities)
        current_chord = np.random.choice(possible_next_chords, p=probabilities)

    return chord_path