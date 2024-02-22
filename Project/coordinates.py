from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time


street_names = []
coordinates = []
neigbourhood_and_street = {}

point_path = ''
coordinat_path = '/html/body/div[1]/div[2]/div[10]/div[1]/div[1]/div[1]/div/div[1]/div/div/div[3]/div[2]/span[2]/div/div/div/div[1]'


def get_coordinates(url, street_names):
    # Set up the Selenium driver
    driver = webdriver.Chrome()
    # Open the URL
    driver.get(url)
    time.sleep(3)

    for street in street_names:
    # Arama kutusunu bul ve sokak adını gir
        arama_kutusu = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[3]/header/div/div/div/form/div[1]/div/span/span/input')
        
        arama_kutusu.send_keys(street)
        driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[3]/header/div/div/div/form/div[2]/button').click()
        
        # Sonuçları bekleyin
        time.sleep(5)  # Uygun bir bekleme süresi ayarlayabilirsiniz
    
        # Adres kutusundaki lat-long değerini al
        try:
            
            coordinat_data = driver.find_element(by= By.XPATH, value= coordinat_path)
            coordinates.append(coordinat_data.text)
            driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[3]/header/div/div/div/form/div[4]/button').click()
            

            print(coordinates)
        except:
            print(street, " için sonuç bulunamadı.")
    
    # Sayfayı temizle ve bir sonraki sokak için geri dön
    driver.get("https://yandex.com.tr/maps")
    # Close the driver
    driver.quit()

def get_streets_csv():
    df = pd.read_csv("./data/streets.csv")
    # columns names are neighbourhood and street. neighbourhood should be key and street should be value with list
    for index, row in df.iterrows():
        if row[0] in neigbourhood_and_street:
            neigbourhood_and_street[row[0]].append(row[1])
        else:
            neigbourhood_and_street[row[0]] = [row[1]]
    
    print(neigbourhood_and_street)


def get_coordinates_to_csv():
    df = pd.DataFrame(coordinates, columns=["coordinates"])
    df.to_csv("./data/coordinates.csv", index=False)

get_streets_csv()
# get_coordinates("https://yandex.com.tr/maps", street_names_test)

