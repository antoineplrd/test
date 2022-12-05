class Node:

    def __init__(self, label, position, connected_nodes):
        self._label = label
        self._position = tuple(position)
        self._connected_nodes = connected_nodes
        self.successive = dict()

    @property
    def label(self):
        return self._label

    @property
    def position(self):
        return self._position

    @property
    def connected_nodes(self):
        return self._connected_nodes

    @property
    def successive(self):
        return self._successive

    @label.setter
    def label(self, value):
        self._label = value

    @position.setter
    def position(self, value):
        self._position = value

    @connected_nodes.setter
    def connected_nodes(self, value):
        self._connected_nodes = value

    @successive.setter
    def successive(self, value):
        self._successive = value

    def propagate(self, signal_information):
        path = signal_information.path
        if len(signal_information.path) > 1:
            nextline = path[0] + path[1]
            nextline_instance = self.successive[nextline]
            signal_information.UpdatePath_CrossedNode()
            nextline_instance.propagate(signal_information)
