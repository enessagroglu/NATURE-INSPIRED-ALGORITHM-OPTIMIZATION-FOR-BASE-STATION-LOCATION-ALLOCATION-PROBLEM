import csv
import random
import json
import os

class Street:
    def __init__(self, neighbourhood, name, population=0, longitude='', latitude='', rate_of_population=None, demand=0):
        self.neighbourhood = neighbourhood
        self.name = name
        self.population = population
        self.longitude = longitude
        self.latitude = latitude
        self.rate_of_population = rate_of_population if rate_of_population is not None else random.randint(1, 5)
        self.demand = demand

    def get_neighbourhood(self):
        return self.__neighbourhood

    def get_name(self):
        return self.__name

    def get_population(self):
        return self.__population
    
    def get_longitude(self):
        return self.__longitude
    
    def get_latitude(self):
        return self.__latitude

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

    def set_longitude(self, longitude):
        self.__longitude = longitude
    
    def set_latitude(self, latitude):
        self.__latitude = latitude

    def set_rate_of_population(self, rate_of_population):
        self.__rate_of_population = rate_of_population
    
    def set_demand(self, demand):
        self.__demand = demand
    
    def __str__(self):
        return f"neighbourhood: {self.__neighbourhood}, Name: {self.__name}, Population: {self.__population}, Latitude: {self.__latitude} ,Longitude: {self.__longitude}, Rate of population: {self.__rate_of_population}"

    @staticmethod
    def create_street_objects_from_csv(csv_file_path, coordinates_file_path):
        streets_by_neighbourhood = {}
        coordinates_dict = {}

        # Properly handle CSV reading for coordinates
        with open(coordinates_file_path, mode='r', newline='', encoding='utf-8') as coordinates_file:
            reader = csv.reader(coordinates_file)
            next(reader)  # Skip the header
            for row in reader:
                if len(row) == 2:
                    address, coordinate = row
                    try:
                        longitude, latitude = coordinate.replace('"', '').split(',')
                        coordinates_dict[address.strip()] = (longitude.strip(), latitude.strip())
                    except ValueError:
                        print(f"Error parsing coordinates for {address}: {coordinate}")
                else:
                    print(f"Skipping malformed line: {row}")

        # Process streets from the streets.csv file
        with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            for row in reader:
                if len(row) >= 2:
                    neighbourhood, name = row[0], row[1]
                    address = f"{neighbourhood}/{name}"
                    longitude, latitude = coordinates_dict.get(address, ("", ""))

                    population = random.randint(100, 1000)
                    rate_of_population = random.randint(1, 5)
                    demand = random.randint(1, 100)

                    street_object = Street(neighbourhood, name, population, longitude, latitude, rate_of_population, demand)
                    streets_by_neighbourhood.setdefault(neighbourhood, []).append(street_object)
                else:
                    print(f"Skipping malformed line in streets file: {row}")

        # Create JSON files for each neighbourhood
        for neighbourhood, street_objects in streets_by_neighbourhood.items():
            json_data = []
            for street_object in street_objects:
                json_data.append({
                    'name': street_object.name,
                    'longitude': street_object.longitude,
                    'latitude': street_object.latitude,
                    'population': street_object.population,
                    'rate_of_population': street_object.rate_of_population,
                    'demand': street_object.demand
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
