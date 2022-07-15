from rdflib import Graph

g = Graph()

g.parse("../Wikipedia Info/nif-context_lang=de.ttl/nif-context_lang=de.ttl")


print(len(g))