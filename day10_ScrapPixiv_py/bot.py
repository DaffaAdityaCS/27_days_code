from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


PATH = "D:\programing\Project\Scrap_py\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.pixiv.net")

search = driver.find_element_by_class_name("_2tR5RNf")
search.send_keys("paimon")
search.send_keys(Keys.RETURN)

link = driver.find_element_by_link_text("Illustrations")
link.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Illustrations"))
    )
    element.click()

except:
    element.quit()




