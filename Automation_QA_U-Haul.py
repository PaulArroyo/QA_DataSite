from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


driver = webdriver.Chrome()
driver.maximize_window()
actions = ActionChains(driver)

driver.get("https://www.uhaul.com/Storage/")
time.sleep(3)


def TC_UH_007():

    #Location
    location = driver.find_element(By.NAME, "SearchKeyword")
    location.send_keys("Miami, FL")

    time.sleep(1)
    
    #Unit Size
    U_size = driver.find_element(By.ID, "selectboxUnitSizeInput")
    U_size.click()

    time.sleep(1)

    CheckBoxSmall = "/html/body/main/div[1]/div/div/form/fieldset/div/div/div[2]/div/fieldset/div/div[2]/ul/li[1]/label"                            
    Csmall = driver.find_element(By.XPATH, CheckBoxSmall)
    Csmall.click()

    time.sleep(1)

    U_size.click()

    time.sleep(1)

    #Type of Storage
    T_Storage = driver.find_element(By.ID, "selectboxInput")
    T_Storage.click()

    time.sleep(1)

    CheckBoxClimateControl = "/html/body/main/div[1]/div/div/form/fieldset/div/div/div[3]/div/fieldset/div/div[2]/ul/li[1]"                            
    ClimateControl = driver.find_element(By.XPATH, CheckBoxClimateControl)
    ClimateControl.click()
    
    time.sleep(1)
    
    CheckBoxIndoorStorage = "/html/body/main/div[1]/div/div/form/fieldset/div/div/div[3]/div/fieldset/div/div[2]/ul/li[2]"                            
    IndoorStorage = driver.find_element(By.XPATH, CheckBoxIndoorStorage)
    IndoorStorage.click()

    time.sleep(1)

    T_Storage.click()

    time.sleep(1)

    #Clic The button!
    FindStorage_button = driver.find_element(by = By.CLASS_NAME, value = "expanded")
    FindStorage_button.click()

    time.sleep(4)

def Move_Online_Today():
    
    #Let's search the correct cell
    MainHeaderMenuOptions = driver.find_elements(by = By.CLASS_NAME, value = "cell")
    
    #Hover the Storage Tile
    i=0
    while i < len(MainHeaderMenuOptions):
        if(MainHeaderMenuOptions[i].text == "Storage"):
            MainHeaderMenuOptions[i]
            actions.move_to_element(MainHeaderMenuOptions[i]).perform()

        i = i + 1    
    time.sleep(2)

    #Click on Move-In Online Today!
    MoveOnlineStorageXpath = "/html/body/header/nav/div/ul/li[8]/ul/li[4]"                            
    MoveOnlineStorage = driver.find_element(By.XPATH, MoveOnlineStorageXpath)
    MoveOnlineStorage.click()
    
    time.sleep(5)

def TC_UH_008():

    #Invalid Location
    location = driver.find_element(By.NAME, "SearchKeyword")
    location.send_keys("Alajuela")

    time.sleep(1)
    
    #Unit Size
    U_size = driver.find_element(By.ID, "selectboxUnitSizeInput")
    U_size.click()

    time.sleep(1)

    CheckBoxSmall = "/html/body/main/div[1]/div/div/form/fieldset/div/div/div[2]/div/fieldset/div/div[2]/ul/li[1]/label"                            
    Csmall = driver.find_element(By.XPATH, CheckBoxSmall)
    Csmall.click()

    time.sleep(1)

    U_size.click()

    time.sleep(1)

    #Type of Storage
    T_Storage = driver.find_element(By.ID, "selectboxInput")
    T_Storage.click()

    time.sleep(1)
    
    CheckBoxIndoorStorage = "/html/body/main/div[1]/div/div/form/fieldset/div/div/div[3]/div/fieldset/div/div[2]/ul/li[2]"                            
    IndoorStorage = driver.find_element(By.XPATH, CheckBoxIndoorStorage)
    IndoorStorage.click()

    time.sleep(1)

    T_Storage.click()

    time.sleep(1)

    #Clic The button!
    FindStorage_button = driver.find_element(by = By.CLASS_NAME, value = "expanded")
    FindStorage_button.click()

    time.sleep(5)



#RUN!
TC_UH_007()
Move_Online_Today()
TC_UH_008()


