import folium
import json

def create_map(all_streets_filepath, bs_status_filepath, output_html='map.html'):
    # Load all streets data
    with open(all_streets_filepath, 'r', encoding='utf-8') as file:
        all_streets = json.load(file)

    # Load base station status data
    with open(bs_status_filepath, 'r', encoding='utf-8') as file:
        bs_status = json.load(file)['streets_with_bs_status']

    # Create a map centered around the first entry (correct coordinates usage)
    if all_streets:
        initial_coords = [float(all_streets[0]["latitude"]), float(all_streets[0]["longitude"])]
    else:
        initial_coords = [40.9600, 29.1500]  # Default coordinates if data is empty

    map_istanbul = folium.Map(location=initial_coords, zoom_start=13)

    # Adding markers for all streets in red
    for street in all_streets:
        folium.Marker(
            [float(street["latitude"]), float(street["longitude"])],  # Correct order of latitude and longitude
            popup=street["name"],
            icon=folium.Icon(color='red')
        ).add_to(map_istanbul)

    # Update markers to green for streets with base stations
    bs_streets = {item['street_name']: item for item in bs_status if item['has_base_station']}
    for street in bs_streets.values():
        folium.Marker(
            [float(street["latitude"]), float(street["longitude"])],  # Correct order of latitude and longitude
            popup=street["street_name"] + " - Base Station",
            icon=folium.Icon(color='green')
        ).add_to(map_istanbul)

    # Save the map as an HTML file
    map_istanbul.save(output_html)
    print(f"Map has been saved to {output_html}")

# Example usage:
create_map('basibuyuk.json', 'streets_with_bs_status.json')
