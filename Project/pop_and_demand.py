import json

with open("street.json", "r", encoding="utf-8") as street_file:
    streets = json.load(street_file)["street"]

with open("neighborhood_pop.json", "r", encoding="utf-8") as pop_file:
    neighborhood_populations = json.load(pop_file)["neighborhood_populations"]


# Her mahallenin toplam rate değerini ve sokakların nüfusunu hesaplama
total_rates = {}
for street in streets:
    neighborhood = street["neighborhood"]
    rate = street["rate_of_population"]
    if neighborhood in total_rates:
        total_rates[neighborhood] += rate
    else:
        total_rates[neighborhood] = rate

# Her mahalle için rate başına düşen nüfusu hesaplama ve sokaklara nüfus dağıtma
for street in streets:
    neighborhood = street["neighborhood"]
    rate = street["rate_of_population"]
    # Mahallenin rate başına düşen nüfusunu hesapla
    population_per_rate = neighborhood_populations[neighborhood] / total_rates[neighborhood]
    # Sokak nüfusunu hesapla ve güncelle
    street["population"] = int(population_per_rate * rate)

# Sokakların güncellenmiş nüfuslarını yazdır
with open("street.json", "w", encoding="utf-8") as street_file:
    json.dump({"street": streets}, street_file, indent=4, ensure_ascii=False)

print("Güncellenmiş sokak verisi street.json dosyasına yazıldı.")
