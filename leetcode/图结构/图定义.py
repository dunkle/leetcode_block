class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected = {}

    def add_neighbor(self, new_id, weight):
        self.connected[new_id] = weight

    def __str__(self):
        return str(self.id) + 'connectedTo:' + str([x.id for x in self.connected])

    def get_connects(self):
        return self.connected.keys()

    def get_id(self):
        return self.id

    def get_weight(self, new_id):
        return self.connected[new_id]


class Graph:
    def __init__(self):
        self.vertex_list = {}
        self.num_vertexes = 0

    def add_vertex(self, key):
        self.num_vertexes += 1
        new_vertex = Vertex(key)
        self.vertex_list[key] = new_vertex

    def get_vertex(self, key):
        if key in self.vertex_list:
            return self.vertex_list[key]
        else:
            return None

    def __contains__(self, key):
        return key in self.vertex_list

    def add_edge(self, f, t, weight):
        if f not in self.vertex_list:
            nv = self.add_vertex(f)
        if t not in self.vertex_list:
            nv = self.add_vertex(t)

        self.vertex_list[f].add_neighbor(self.vertex_list[t], weight)

    def get_vertices(self):
        return self.vertex_list.keys()

    def __iter__(self):
        return iter(self.vertex_list.values())
