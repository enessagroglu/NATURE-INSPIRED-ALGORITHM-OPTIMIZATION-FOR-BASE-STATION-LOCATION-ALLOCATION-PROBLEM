from fitness_function import fitness_function
from generate_population import generate_new_generation
import json



def genetic_algorithm(streets_data, population, max_generations=100, fitness_threshold=0.95, max_stagnant_generations=10, mutation_rate=0.01, tournament_size=4):
    best_fitness = -float('inf')
    stagnant_generations = 0

    for generation in range(max_generations):
        # Fitness hesapla ve yeni nesli oluştur
        fitness_scores = [fitness_function(chromosome, streets_data) for chromosome in population]
        new_population = generate_new_generation(streets_data, population, mutation_rate, tournament_size)
        
        # En iyi fitness değerini güncelle
        best_generation_fitness = max(fitness_scores)
        if best_generation_fitness > best_fitness:
            best_fitness = best_generation_fitness
            stagnant_generations = 0
        else:
            stagnant_generations += 1

        # Durma koşulları
        if best_fitness >= fitness_threshold:
            print(f"Fitness threshold reached: {best_fitness:.2f} at generation {generation}")
            break

        if stagnant_generations >= max_stagnant_generations:
            print(f"No improvement for {max_stagnant_generations} generations, stopping early at generation {generation}")
            break

        # Popülasyonu yeni nesil ile değiştir
        population = new_population

    return population, best_fitness

def read_street_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        streets_data = json.load(file)
    return streets_data

def save_best_solution_to_json(chromosome, filepath='best_solution.json'):
    """Saves the best solution chromosome to a JSON file."""
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump({'best_chromosome': chromosome}, file, ensure_ascii=False, indent=4)

def read_population_from_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['chromosomes']

def main():
    # paths for street data and initial population JSON files
    streets_filepath = r"D:\Projects\NATURE-INSPIRED-ALGORITHM-OPTIMIZATION-FOR-BASE-STATION-LOCATION-ALLOCATION-PROBLEM\Project\data\basibuyuk.json"
    population_filepath = r"D:\Projects\NATURE-INSPIRED-ALGORITHM-OPTIMIZATION-FOR-BASE-STATION-LOCATION-ALLOCATION-PROBLEM\Project\data\basibuyuk_initial_population.json"

    # Read street data and initial population
    streets_data = read_street_data(streets_filepath)
    population = read_population_from_json(population_filepath)

    # Run the genetic algorithm
    final_population, best_fitness = genetic_algorithm(streets_data, population)

    # Find the best chromosome from the final population
    best_chromosome = max(final_population, key=lambda x: fitness_function(x, streets_data))

    # Save the best chromosome to a JSON file
    save_best_solution_to_json(best_chromosome)

    print("Best Fitness Achieved:", best_fitness)
    

if __name__ == "__main__":
    main()
