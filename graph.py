# Minha representação de Marvo Chain
import random


#Definir os gráficos e os termos dos vértices

class Vertex(object):
    def __init__(self, value): #Value é a palavra
        self.value = value
        self.adjacent = {} #nódulos que têm uma borda deste vértice
        self.neighbors = []
        self.neighbors_weights = []

    def __str__(self):
        return self.value + ' '.join([node.value for node in self.adjacent.keys()])

    def add_edge_to(self, vertex, weight=0):
        #Adiciona a borda no vértice colocado junto ao peso
        self.adjacent[vertex] = weight

    def increment_edge(self, vertex):
        #Incrementa o peso sobre a borda
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1

    def get_adjacent_nodes(self):
        return self.adjacent.keys()

    def get_probability_map(self):
        for (vertex, weight) in self.adjacent.items():
            self.neighbors.append(vertex)
            self.neighbors_weights.append(weight)


    def next_word(self):
        #Randomicamente seleciona a próxima palavra BASEADA NO PESO
        return random.choices(self.neighbors, weights=self.neighbors_weights) [0]

#Agora tenho a representação do vértice, colocarei junta a um gráfico

class Graph(object):
    def __init__(self):
        self.vertices = {}

    def get_vertex_values(self):
        return set(self.vertices.keys()) #Qual o valor de todos os vértices nas palavras retornando todas as possíveis palavras

    def add_vertex(self, value):
        self.vertices[value] = Vertex(value)

    def get_vertex(self, value):
        if value not in self.vertices: #E se o valor não estiver no gráfico
            self.add_vertex(value)
        return self.vertices[value] #Pega o objeto do vértice

    def get_next_word(self, current_vertex):
        return self.vertices[current_vertex.value].next_word()

    def generate_probability_mappings(self):
        for vertex in self.vertices.values():
            vertex.get_probability_map()