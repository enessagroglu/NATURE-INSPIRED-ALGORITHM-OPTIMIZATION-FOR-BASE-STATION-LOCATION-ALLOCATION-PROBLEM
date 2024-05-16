import json
import random

# JSON dosyalarını yükle
with open("street.json", "r", encoding="utf-8") as street_file:
    streets = json.load(street_file)["street"]

with open("neighborhood_pop.json", "r", encoding="utf-8") as pop_file:
    neighborhood_populations = json.load(pop_file)["neighborhood_populations"]

# Talep oranları
demand_ratios = [0.5, 0.75, 0.2]

# Her mahalle için talep değerini hesapla ve güncelle
for street in streets:
    neighborhood = street["neighborhood"]
    population = street["population"]
    # Talep oranlarından rastgele birini seç
    demand_ratio = random.choice(demand_ratios)
    # Mahalle nüfusu ile talep oranını çarp ve talep değerini bul
    demand = int(population * demand_ratio)
    # Sokak talebini güncelle
    street["demand"] = demand

# Güncellenmiş sokak verisini street.json dosyasına yaz
with open("street.json", "w", encoding="utf-8") as street_file:
    json.dump({"street": streets}, street_file, indent=4, ensure_ascii=False)

print("Talep değerleri street.json dosyasına eklendi.")