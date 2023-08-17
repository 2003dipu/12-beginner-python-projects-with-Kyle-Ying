import random

class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent = {}  # nodes that have an edge from this vertex
        self.neighbors = []
        self.neighbors_weights = []  # Corrected attribute name

    def increment_edge(self, vertex):
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1
    
    def get_probability_map(self):
        for (vertex, weight) in self.adjacent.items():
            self.neighbors.append(vertex)
            self.neighbors_weights.append(weight)  # Corrected attribute name

   
    def next_word(self):
        if len(self.neighbors) <= 10:  # Adjust the limit as needed
            print("Neighbors:", self.neighbors)
            print("Weights:", self.neighbors_weights)
        return random.choices(self.neighbors, weights=self.neighbors_weights)[0]

class Graph:
    def __init__(self):
        self.vertices = {}

    def get_vertex_values(self):
        return set(self.vertices.keys())
    
    def add_vertex(self, value):
        self.vertices[value] = Vertex(value)
    
    def get_vertex(self, value):
        if value not in self.vertices:
            self.add_vertex(value)
        return self.vertices[value]
    
    def get_next_word(self, current_vertex):
        return self.vertices[current_vertex.value].next_word()
    
    def generate_probability_mappings(self):
        for vertex in self.vertices.values():
            vertex.get_probability_map()
