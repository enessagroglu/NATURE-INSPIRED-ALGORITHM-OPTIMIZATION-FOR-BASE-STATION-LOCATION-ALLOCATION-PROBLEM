import numpy as np
import random

def tournament_selection(population, fitness_scores, tournament_size=4):
    """Selects two parents from the population using tournament selection."""
    # Turnuva için rastgele bireyler seç
    participants = random.sample(list(enumerate(population)), tournament_size)
    
    # Participants listesinden (index, chromosome) çiftleri olarak alınır
    # Fitness skorlarına göre sıralayarak en iyi iki bireyi bul
    sorted_participants = sorted(participants, key=lambda x: fitness_scores[x[0]], reverse=True)
    
    # En iyi iki bireyi dön
    return [population[idx] for idx, _ in sorted_participants[:2]]

# Örnek kullanım
population = [np.random.randint(0, 2, 10) for _ in range(100)]  # Rastgele bir populasyon yarat (örneğin, 100 birey ve her biri 10 gene sahip)
fitness_scores = [np.random.rand() for _ in range(100)]  # Her birey için rastgele fitness skorları yarat

# Turnuva seçimi yaparak iki ebeveyni seç
parents = tournament_selection(population, fitness_scores)
print("Seçilen Ebeveynler:", parents)