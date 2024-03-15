class Graph():
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacent_list = dict()

    def add_vertex(self, value):
        self.adjacent_list[value] = []
        self.number_of_nodes += 1

    def add_edge(self, value_1, value_2):
        self.adjacent_list[value_1].append(value_2)
        self.adjacent_list[value_2].append(value_1)
    
    def show_connections(self):
        nodes = list(self.adjacent_list.keys())
        for node in nodes:
            node_connections = self.adjacent_list[node]
            connections = ""
            for vertex in node_connections:
                connections += vertex + " "
            print(node + "->" + connections)


graph = Graph()

graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_edge('3', '1')
graph.add_edge('3', '4')
graph.add_edge('4', '2')
graph.add_edge('4', '5')
graph.add_edge('1', '2')
graph.add_edge('1', '0')
graph.add_edge('0', '2')
graph.add_edge('6', '5')

print(graph.adjacent_list)

graph.show_connections()
