from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    # Calculate geographic distance between coordinates (in km)
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of the Earth in km
    return c * r

def fitness_function(chromosome, streets_data, coverage_radius, max_demand_per_station):
    total_demand = sum(street['demand'] for street in streets_data)
    covered_demand = 0
    total_stations = sum(chromosome)
    penalty = 0

    for i, active in enumerate(chromosome):
        if active:
            station_coord = (streets_data[i]['longitude'], streets_data[i]['latitude'])
            local_covered_demand = 0

            for street in streets_data:
                street_coord = (street['longitude'], street['latitude'])
                distance = haversine(float(station_coord[0]), float(station_coord[1]), float(street_coord[0]), float(street_coord[1]))

                if distance <= coverage_radius:
                    local_covered_demand += street['demand']
                    if local_covered_demand > max_demand_per_station:
                        break

            covered_demand += min(local_covered_demand, max_demand_per_station)

    covered_demand_ratio = covered_demand / total_demand
    penalty = (total_demand - covered_demand) * 0.01 
    fitness = covered_demand_ratio - (total_stations / len(streets_data)) - penalty

    return fitness
