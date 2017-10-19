from py2neo import Graph, Node
def add_property(node, property_key, property_value):
    print("{}, {}, {}.".format(node, property_key, property_value))
    graph = Graph('http://neo4j:simello@localhost:7474/db/data/')
    graph_node = Node("Person", name="" + node + "")
    graph.merge(graph_node)
    graph_node["{}".format(property_key)] = "{}".format(property_value)
    graph_node.push()
"""" describe simello is a person and his age is 28 and his nationality is italian. """
"""  0        1       2  3 4      5   6   7   8  9  10  11  12          13 14 """
def add_property2(node, *labels, **params):
    node_value = node 
    graph = Graph('http://neo4j:simello@localhost:7474/db/data/')
    graph_node = Node(labels, name="" + node + "")
    graph.merge(graph_node)
    for k,v in params:
        graph_node["{}".format(k)] = "{}".format(v)
        graph_node.push()
