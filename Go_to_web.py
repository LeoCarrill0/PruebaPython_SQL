from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#priceProDetalle
def web(ref):
    ref_1 = "https://guatemaladigital.com/Producto/" + str(ref)
    driver = webdriver.Chrome()
    driver.get(ref_1)
    assert "Aegend" in driver.title
    elem = driver.find_element(By.CLASS_NAME, "priceProDetalle")
    print(elem.text)

    
a = input("Ingrese el codigo: ")
web(a)