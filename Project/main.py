from fitness_function import fitness_function
from generate_population import generate_new_generation
import json
import os

def genetic_algorithm(streets_data, population, max_generations=100, fitness_threshold=100, max_stagnant_generations=20, mutation_rate=0.35, tournament_size=4):
    best_fitness = -float('inf')
    stagnant_generations = 0

    for generation in range(max_generations):
        # Calculate fitness and create a new generation
        fitness_scores = [fitness_function(chromosome, streets_data) for chromosome in population]
        new_population = generate_new_generation(streets_data, population, mutation_rate, tournament_size)

        # Update the best fitness score
        best_generation_fitness = max(fitness_scores)
        if best_generation_fitness > best_fitness:
            best_fitness = best_generation_fitness
            stagnant_generations = 0
        else:
            stagnant_generations += 1

        # Stop conditions
        if best_fitness >= fitness_threshold:
            print(f"Fitness threshold reached: {best_fitness:.2f} at generation {generation}")
            break

        if stagnant_generations >= max_stagnant_generations:
            print(f"No improvement for {max_stagnant_generations} generations, stopping early at generation {generation}")
            break

        # Replace the population with the new generation
        population = new_population

    return population, best_fitness


def read_street_data(filepath):
    """Reads street data from a JSON file."""
    if not os.path.exists(filepath):
        directory = os.path.dirname(filepath)
        files = os.listdir(directory) if os.path.exists(directory) else []
        raise FileNotFoundError(f"Street data file not found: {filepath}\nFiles in directory: {files}")
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)


def read_population_from_json(filepath):
    """Reads population data from a JSON file."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Population data file not found: {filepath}")
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['chromosomes']

def save_best_solution_to_json(chromosome, filepath='best_solution.json'):
    """Saves the best solution chromosome to a JSON file."""
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump({'best_chromosome': chromosome}, file, ensure_ascii=False, indent=4)


def map_and_save_streets_with_status(streets_data, best_chromosome, output_filepath='streets_with_bs_status.json'):
    """Maps streets to chromosome values indicating whether a base station is placed or not, and saves to a JSON file."""
    # Create a list of dictionaries where each street is mapped to the corresponding chromosome value
    streets_with_status = [
        {
            "street_name": streets_data[i]["name"],
            "has_base_station": bool(value)  # True if 1, False if 0
        }
        for i, value in enumerate(best_chromosome)
    ]

    # Save this data to a JSON file
    with open(output_filepath, 'w', encoding='utf-8') as file:
        json.dump({'streets_with_bs_status': streets_with_status}, file, ensure_ascii=False, indent=4)

    print(f"Street status data has been saved to {output_filepath}")
    
def calculate_cost_from_best_solution(filepath='best_solution.json', base_station_cost=100):
    """
    Calculate the total cost based on the best solution JSON file.
    
    Args:
        filepath (str): Path to the best solution JSON file.
        base_station_cost (int): Cost per base station.
    
    Returns:
        int: Total cost of all placed base stations.
    """
    try:
        # Read the best solution JSON file
        with open(filepath, 'r', encoding='utf-8') as file:
            best_solution = json.load(file)
        
        # Get the chromosome representing the best solution
        chromosome = best_solution['best_chromosome']
        
        # Count the number of 1s in the chromosome
        num_base_stations = sum(chromosome)
        
        # Calculate the total cost
        total_cost = num_base_stations * base_station_cost
        
        return total_cost
    except (FileNotFoundError, KeyError, json.JSONDecodeError) as e:
        print(f"Error reading or parsing best solution file: {e}")
        return None

def main():
    # Paths for street data and initial population JSON files
    streets_filepath = r"D:\GraduationProject\NATURE-INSPIRED-ALGORITHM-OPTIMIZATION-FOR-BASE-STATION-LOCATION-ALLOCATION-PROBLEM\Project\data\basibuyuk.json"
    population_filepath = r"D:\GraduationProject\NATURE-INSPIRED-ALGORITHM-OPTIMIZATION-FOR-BASE-STATION-LOCATION-ALLOCATION-PROBLEM\Project\data\basibuyuk_initial_population.json"

    # Read street data and initial population
    streets_data = read_street_data(streets_filepath)
    population = read_population_from_json(population_filepath)

    # Run the genetic algorithm
    final_population, best_fitness = genetic_algorithm(streets_data, population)

    # Find the best chromosome from the final population
    best_chromosome = max(final_population, key=lambda x: fitness_function(x, streets_data))

    # Save the best chromosome to a JSON file
    save_best_solution_to_json(best_chromosome)

    # Map streets with their base station status (0 or 1) and save to a JSON file
    map_and_save_streets_with_status(streets_data, best_chromosome)

    total_cost = calculate_cost_from_best_solution('best_solution.json', base_station_cost=100)

    # Print the best fitness and total cost achieved
    print("Best Fitness Achieved:", best_fitness)
    print("Total Cost of Best Solution:", total_cost)


if __name__ == "__main__":
    main()
