import string
from graph import Graph, Vertex  # Assuming you have the graph module
import random
import os
import re
class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent = {}
        self.neighbors = []
        self.neighbors_weights = []

    def increment_edge(self, vertex):
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1
    
    def get_probability_map(self):
        for (vertex, weight) in self.adjacent.items():
            self.neighbors.append(vertex)
            self.neighbors_weights.append(weight)

    def next_word(self):
        if len(self.neighbors) <= 10:
            """print("Neighbors:", self.neighbors)
            print("Weights:", self.neighbors_weights)"""
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

def get_words_from_text(text_path):
    with open(text_path, 'r') as f:
        text = f.read()
        # remove text in here
        text = re.sub(r'\[(.+)\]',' ', text)
        text = ' '.join(text.split())
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    return words

def make_graph(words):
    g = Graph()
    previous_word = None

    for word in words:
        word_vertex = g.get_vertex(word)
        
        if previous_word:
            previous_word.increment_edge(word_vertex)
        previous_word = word_vertex
    g.generate_probability_mappings()
    return g

def compose(g, words, length=50):
    composition = []
    word = g.get_vertex(random.choice(words))
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)
    return composition

def main():
    # for song lyrics
    
    script_directory = os.path.dirname(os.path.abspath(__file__))
    text_path = os.path.join(script_directory, 'career.txt')

    words = get_words_from_text(text_path)
    g = make_graph(words)
    composition = compose(g, words, 100)
    return ' '.join(composition)

if __name__ == '__main__':
    print(main())
