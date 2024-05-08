import folium
import json
import os

# Function to add points from a JSON file to the map
def add_points_from_json(file_name, map_object):
    try:
        # Construct the full path to the file
        file_path = os.path.join(os.getcwd(), file_name)
        with open(file_path, 'r', encoding='utf-8') as file:  # Ensure using utf-8 encoding
            data = json.load(file)
        
        for item in data:
            try:
                # Extract and parse latitude and longitude
                latitude = float(item["longitude"].strip().strip('"'))
                longitude = float(item["latitude"].strip().strip('"'))
                popup_info = (f"Name: {item['name']}<br>"
                              f"Population: {item['population']}<br>"
                              f"Population Rate: {item['rate_of_population']}<br>"
                              f"Demand: {item['demand']}")
                # Add marker to the map
                folium.Marker([latitude, longitude], popup=folium.Popup(popup_info, max_width=250)).add_to(map_object)
            except ValueError as e:
                print(f"Error converting coordinates for {item['name']}: {e}")
    except FileNotFoundError as e:
        print(f"File not found: {file_name} - {e}")
    except Exception as e:
        print(f"An error occurred while processing {file_name}: {e}")

# Main block to create the map and add markers
def main():
    # Center the map around an average location in Istanbul
    latitude = 41.0082
    longitude = 28.9784
    map_istanbul = folium.Map(location=[latitude, longitude], zoom_start=12)

    # Adding markers for predefined places
    folium.Marker([41.016830, 29.130371], popup='Tepeüstü').add_to(map_istanbul)
    folium.Marker([40.959255, 29.156509], popup='Başibüyük').add_to(map_istanbul)
    folium.Marker([41.079010, 29.257734], popup='Reşadiye').add_to(map_istanbul)

    # Load data from JSON files and add to map
    add_points_from_json('resadiye.json', map_istanbul)
    add_points_from_json('basibuyuk.json', map_istanbul)
    add_points_from_json('tepeustu.json', map_istanbul)

    # Save the map as an HTML file
    map_istanbul.save('combined_istanbul_neighborhoods.html')

# Entry point for the script
if __name__ == "__main__":
    main()
