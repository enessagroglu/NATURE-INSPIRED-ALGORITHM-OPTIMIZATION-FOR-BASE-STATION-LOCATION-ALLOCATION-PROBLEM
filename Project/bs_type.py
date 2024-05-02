class bs_type:
    def __init__(self, cost, type, capacity, range):
        self._cost = cost
        self._type = type
        self._capacity = capacity
        self._range = range

    # Getter methods
    def get_cost(self):
        return self._cost

    def get_type(self):
        return self._type

    def get_capacity(self):
        return self._capacity

    def get_range(self):
        return self._range

    # Setter methods
    def set_cost(self, cost):
        self._cost = cost

    def set_type(self, type):
        self._type = type

    def set_capacity(self, capacity):
        self._capacity = capacity

    def set_range(self, range):
        self._range = range