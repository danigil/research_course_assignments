# import networkx as nx
# G= nx.DiGraph()
#
# first, second = ("PIGS", "HAMS")
#
# G.add_nodes_from((first, second))
#
# G.add_edge(first, second, contained_in=True)
# G.add_edge(second, first,  contains=True)
#
# print(G.nodes)
# print(G.edges)
#
# G.add_node("PIGS")
#
# print(G.nodes)
# print(G.edges)
import re
pattern = "([A-Z]+)( with ([A-Z]+)( ((and ([A-Z]+)) )*(and ([A-Z]+))){0,1}){0,1}( that can ([A-Z]+)( ((and ([A-Z]+)) )*(and ([A-Z]+))){0,1}){0,1} can ([A-Z]+)"
pattern2= "([A-Z]+)( with (?:[A-Z]+)(?: (?:(?:and (?:[A-Z]+)) )*(?:and (?:[A-Z]+))){0,1}){0,1}( that can (?:[A-Z]+)(?: (?:(?:and (?:[A-Z]+)) )*(?:and (?:[A-Z]+))){0,1}){0,1} can ([A-Z]+)"
match = re.fullmatch(pattern2,"ANIMALS with WINGS that can RUN and CRAWL can FLY")

print(match.groups())