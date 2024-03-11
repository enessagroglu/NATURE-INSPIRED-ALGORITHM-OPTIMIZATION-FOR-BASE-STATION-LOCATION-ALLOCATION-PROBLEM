import random
import json
import os

class Street:
    def __init__(self, neighbourhood, name, population, coordinate, rate_of_population, demand):
        self.__neighbourhood = neighbourhood
        self.__name = name
        self.__population = population
        self.__coordinate = coordinate
        self.__rate_of_population = rate_of_population
        self.__demand = demand

    def get_neighbourhood(self):
        return self.__neighbourhood

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


    def set_neighbourhood(self, neighbourhood):
        self.__neighbourhood = neighbourhood

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
    
    def __str__(self):
        return f"neighbourhood: {self.__neighbourhood}, Name: {self.__name}, Population: {self.__population}, Coordinate: {self.__coordinate}, Rate of population: {self.__rate_of_population}"

    @staticmethod
    def create_street_objects_from_csv(csv_file_path, coordinates_file_path):
        streets_by_neighbourhood = {}
        coordinates_dict = {}  # Store coordinates information

        # Read coordinates from the coordinates.csv file
        with open(coordinates_file_path, 'r', encoding='utf-8') as coordinates_file:
            next(coordinates_file)  # Skip the header
            for line in coordinates_file:
                parts = line.strip().split(',')
                if len(parts) >= 2:
                    address = parts[0]
                    coordinate = parts[1].lstrip('"\"')
                    coordinates_dict[address] = coordinate

        # Process streets from the streets.csv file
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            next(file)  # Skip the header
            for line in file:
                parts = line.strip().split(',')
                if len(parts) >= 2:
                    neighbourhood = parts[0]
                    name = parts[1]
                    address = f"{neighbourhood}/{name}"
                    
                    # Check if coordinates are available for the address
                    if address in coordinates_dict:
                        coordinate = coordinates_dict[address]
                    else:
                        print(f"Coordinates not found for address: {address}")
                        coordinate = ""

                    demand = 0
                    population = 0
                    rate_of_population = random.randint(1, 5)
                    street_object = Street(neighbourhood, name, population, coordinate, rate_of_population, demand)

                    if neighbourhood not in streets_by_neighbourhood:
                        streets_by_neighbourhood[neighbourhood] = []

                    streets_by_neighbourhood[neighbourhood].append(street_object)
                else:
                    print(f"Skipping line: {line}")

        # Write JSON files for each neighbourhood
        for neighbourhood, street_objects in streets_by_neighbourhood.items():
            json_data = []
            for street_object in street_objects:
                json_data.append({
                    'name': street_object.get_name(),
                    'coordinate': street_object.get_coordinate(),
                    'population': street_object.get_population(),
                    'rate_of_population': street_object.get_rate_of_population(),
                    'demand': street_object.get_demand()
                })

            json_file_path = os.path.join(script_directory, 'data', f'{neighbourhood}.json')
            with open(json_file_path, 'w', encoding='utf-8') as json_file:
                json.dump(json_data, json_file, ensure_ascii=False, indent=2)

        return streets_by_neighbourhood

# CSV and coordinates file paths
script_directory = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(script_directory, 'data', 'streets.csv')
coordinates_file_path = os.path.join(script_directory, 'data', 'coordinates.csv')

streets_by_neighbourhood = Street.create_street_objects_from_csv(csv_file_path, coordinates_file_path)

# Print the created JSON files
for neighbourhood, street_objects in streets_by_neighbourhood.items():
    print(f'Created JSON file for {neighbourhood}: {neighbourhood}_streets.json')

 #İlk birkaç objeyi görmek için
for neighbourhood, street_objects in streets_by_neighbourhood.items():
    print(f"Street objects in neighbourhood {neighbourhood}:")
    for street in street_objects[:5]:  # İlk 5 objeyi yazdır
        print(street)
