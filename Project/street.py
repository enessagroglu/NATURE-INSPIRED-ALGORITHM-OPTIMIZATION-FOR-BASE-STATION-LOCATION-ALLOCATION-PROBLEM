
# Street class will have the following properties: neighborhood, name, population, coordinate, rate of population. They should be private.

class Street:
    def __init__(self, neighborhood, name, population, coordinate, rate_of_population, demand, base_station_types):
        self.__neighborhood = neighborhood
        self.__name = name
        self.__population = population
        self.__coordinate = coordinate
        self.__rate_of_population = rate_of_population
        self.__demand = demand
        self.__base_station_types = base_station_types

    def get_neighborhood(self):
        return self.__neighborhood

    def get_name(self):
        return self.__name

    def get_population(self):
        return self.__population

    def get_coordinate(self):
        return self.__coordinate

    def get_rate_of_population(self):
        return self.__rate_of_population
    
    def get_demand(self):
        return self.__demand

    def get_base_station_types(self):
        return self.__base_station_types

    def set_neighborhood(self, neighborhood):
        self.__neighborhood = neighborhood

    def set_name(self, name):
        self.__name = name

    def set_population(self, population):
        self.__population = population

    def set_coordinate(self, coordinate):
        self.__coordinate = coordinate

    def set_rate_of_population(self, rate_of_population):
        self.__rate_of_population = rate_of_population
    
    def set_demand(self, demand):
        self.__demand = demand
    
    def set_base_station_types(self, base_station_types):
        self.__base_station_types = base_station_types

    def __str__(self):
        return f"Neighborhood: {self.__neighborhood}, Name: {self.__name}, Population: {self.__population}, Coordinate: {self.__coordinate}, Rate of population: {self.__rate_of_population}"
