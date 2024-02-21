

# Neighborhood class will have these attributes: name, population, number of streets, streets list. They should be private.

class Neighborhood:
    def __init__(self, name, population, number_of_streets, streets):
        self.__name = name
        self.__population = population
        self.__number_of_streets = number_of_streets
        self.__streets = streets

    def get_name(self):
        return self.__name

    def get_population(self):
        return self.__population

    def get_number_of_streets(self):
        return self.__number_of_streets

    def get_streets(self):
        return self.__streets

    def set_name(self, name):
        self.__name = name

    def set_population(self, population):
        self.__population = population

    def set_number_of_streets(self, number_of_streets):
        self.__number_of_streets = number_of_streets

    def set_streets(self, streets):
        self.__streets = streets

    def __str__(self):
        return f"Neighborhood: {self.__name}, Population: {self.__population}, Number of streets: {self.__number_of_streets}, Streets: {self.__streets}"
