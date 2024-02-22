from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


street_names_test = ["RESUL SK. tepeustu","LIDER SK. tepeustu"]
coordinates = []

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
        arama_kutusu = driver.find_element(By.XPATH, '//*[@id="b9663a41-358f-43b5-a560-69e61e93afdc"]')
        arama_kutusu.clear()
        arama_kutusu.send_keys(street)
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/header/div/div/div/form/div[2]/button').click()
        
        # Sonuçları bekleyin
        time.sleep(5)  # Uygun bir bekleme süresi ayarlayabilirsiniz
    
        # Adres kutusundaki lat-long değerini al
        try:
            
            coordinat_data = driver.find_element(by= By.XPATH, value= coordinat_path)
            coordinates.append(coordinat_data.text)
            
           
            print(coordinates)
        except:
            print(street, " için sonuç bulunamadı.")
    
    # Sayfayı temizle ve bir sonraki sokak için geri dön
    driver.get("https://yandex.com.tr/maps")
    # Close the driver
    driver.quit()

get_coordinates("https://yandex.com.tr/maps", street_names_test)

    
 