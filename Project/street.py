import random
# Street class will have the following properties: neighborhood, name, population, coordinate, rate of population. They should be private.

class Street:
    def __init__(self, neighborhood, name, population, coordinate, rate_of_population, demand):
        self.__neighborhood = neighborhood
        self.__name = name
        self.__population = population
        self.__coordinate = coordinate
        self.__rate_of_population = rate_of_population
        self.__demand = demand

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
    

    def create_street_objects_from_csv(csv_file_path):
        street_objects = []
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            next(file)  
            for line in file:
                parts = line.strip().split('/')
                neighborhood = parts[0]
                name_and_coordinate = parts[1].split(',')
                name = name_and_coordinate[0]
                coordinate = name_and_coordinate[1]
                demand = 0
                population =  0
                rate_of_population = random.randint(1, 5)
                street_object = Street(neighborhood, name, population, coordinate, rate_of_population, demand)
                street_objects.append(street_object)
        return street_objects

    # CSV dosyası yolu
    csv_file_path = 'yolunuz.csv'
    streets = create_street_objects_from_csv(csv_file_path)

    # İlk birkaç objeyi görmek için
    for street in streets[:5]:  # İlk 5 objeyi yazdır
        print(street)

    def __str__(self):
        return f"Neighborhood: {self.__neighborhood}, Name: {self.__name}, Population: {self.__population}, Coordinate: {self.__coordinate}, Rate of population: {self.__rate_of_population}"
