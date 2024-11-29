class Planet(object):
    def __init__(self, position, vector_start, mass, radius, color, trace_len=20):
        self.position = position
        self.vector = vector_start
        self.mass = mass
        self.radius = radius
        self.color = color
        self.traces = []
        self.trace_len = trace_len

    def update(self, vector):
        self.vector = self.vector[0] + vector[0], self.vector[1] + vector[1]
        self.position = self.position[0] + self.vector[0], self.position[1] + self.vector[1]

    def trace(self):
        if len(self.traces) < self.trace_len:
            self.traces.append(self.position)
        else:
            self.traces.pop(0)
