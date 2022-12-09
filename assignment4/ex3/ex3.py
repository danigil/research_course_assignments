from enum import Enum
import re

import networkx as nx
import matplotlib.pyplot as plt


class AlgoOutputs(Enum):
    All_pigs_can_fly = 1
    Some_pigs_can_fly = 2
    No_pigs_can_fly = 3


pattern = "([A-Z]+)( with (?:[A-Z]+)(?: (?:(?:and (?:[A-Z]+)) )*(?:and (?:[A-Z]+))){0,1}){0,1}\
            ( that can (?:[A-Z]+)(?: (?:(?:and (?:[A-Z]+)) )*(?:and (?:[A-Z]+))){0,1}){0,1} can ([A-Z]+)"


def when_pigs_fly(input: str) -> AlgoOutputs:
    G = nx.DiGraph()

    objects = {}

    traits_are_traits = set()
    objects_have_traits = set()

    relations = {
        "are": ("contained_in", "contains"),
        "have": ("have", "are_had_by"),
        "can": ("can", "can_be_done_by")
    }

    for line in input.splitlines():
        
        if match := re.fullmatch("([A-Z]+) ([a-z]+) ([A-Z]+)", line):
            node1, relation, node2 = match.groups()

            G.add_node(node1)
            G.add_node(node2)

            G.add_edge(node1, node2, attr=relations[relation][0])
            G.add_edge(node2, node1, attr=relations[relation][1])
        elif match := re.fullmatch(pattern, line):
            node1, traits, abilities, node2 = match.groups()
            traits = traits[5:].split("and")
            abilities = abilities[9:].split("and")
            pass
        # if match := re.fullmatch("([A-Z]+) are ([A-Z]+)", line):
        #     first, second = match.groups()
        #
        #     if not (first in traits and second in traits):
        #         # OBJECT_A are OBJECT_B
        #         if first not in G.nodes:
        #             G.add_node(first)
        #
        #         if second not in G.nodes:
        #             G.add_node(second)
        #
        #     G.add_edge(first, second, contained_in=True)
        #     G.add_edge(second, first,  contains=True)
        #
        # if match := re.fullmatch("([A-Z]+) have ([A-Z]+)", line):
        #     # OBJECT have TRAIT
        #     first, second = match.groups()
        #     for node in match.groups():
        #         if node not in G.nodes:
        #             G.add_node(node)
        #
        #     G.add_edge(first, second, have=True)
        #     G.add_edge(second, first, are_had_by=True)
        #
        #
        #
        # if match := re.fullmatch("([A-Z]+) can ([A-Z]+)", line):
        #     first, second = match.groups()
        #     for node in match.groups():
        #         if node not in G.nodes:
        #             G.add_node(node)
        #
        #     G.add_edge(first, second, can=True)
        #     G.add_edge(second, first, are_had_by=True)

    # options = {
    #     "font_size": 10,
    #     "node_size": 300,
    #     "node_color": "white",
    #     "edgecolors": "black",
    #     "linewidths": 1,
    #     "width": 1,
    #     "with_labels": True
    # }
    #
    # nx.draw(G, **options)
    # pos = nx.spring_layout(G)
    #
    # edge_labels = nx.get_edge_attributes(G, 'attr')
    # nx.draw_networkx_edge_labels(G,pos, edge_labels=edge_labels)
    #
    # plt.show()

    return AlgoOutputs.All_pigs_can_fly
