from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Solution to dismissing modal popups version 1


edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)
edge_options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.geolocation": 1,  # Allow location
    "profile.default_content_setting_values.notifications": 1  # Allow notifications
})

# edge_options.page_load_strategy = 'eager'
medriver_path = "C:\webdrivers\msedgedriver.exe"  # causes browser mismatch
service = Service(medriver_path)
driver = webdriver.Edge(options=edge_options, service=service)
driver.get("https://tinder.com/")
time.sleep(2)
try:
  login = driver.find_element(By.XPATH, value="/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a")
except:
  login = driver.find_element(By.XPATH, value="/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a")
login.click()
time.sleep(2)

original_window = driver.current_window_handle
driver.window_handles

for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

facebook_login = driver.find_element(By.XPATH, value="/html/body/div[2]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button")
facebook_login.click()
# https://www.geeksforgeeks.org/how-to-access-popup-login-window-in-selenium-using-python/
time.sleep(2)


# cookies = driver.find_element(By.XPATH, value="/html/body/div[2]/div[2]/div/div/div/div/div[3]/div[2]/div/div[2]/div[1]")
# cookies.click()

facebook_window = driver.current_window_handle
for window_handle in driver.window_handles:
      if window_handle != original_window and window_handle != facebook_window:
          driver.switch_to.window(window_handle)
          break

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[2]/div/div/div/div/div[3]/div[2]/div/div[2]/div[1]'))).click()


username = driver.find_element(By.XPATH, value="/html/body/div/div[2]/div[1]/form/div/div[1]/div/input")
username.send_keys("szymonbryniakproject@gmail.com")
password = driver.find_element(By.XPATH, value="/html/body/div/div[2]/div[1]/form/div/div[2]/div/input")
password.send_keys("Password_12354!")

facebook_log_in = driver.find_element(By.XPATH, value="/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input")
facebook_log_in.click()

try:
  tinder_continue = driver.find_element(By.XPATH, value="/html/body/div[1]/div/div/div/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div/div/div[3]/div[1]/div/div/div/div[1]/div/div/div/div")
  tinder_continue.click()
except:
  print("elemenet not found: tinder continue 59")

for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

driver.switch_to.window(original_window)
time.sleep(2)
# driver.switch_to.alert().accept()
# print(len(driver.window_handles))
driver.switch_to.active_element.find_element(By.XPATH, value="/html/body/div[2]/div/div[1]/div/div/div[3]/button[1]").click()
# tinder_allow = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div[3]/button[1]"))).click()
# tinder_allow = driver.find_element(by_chained((By.NAME, value=))
# attr = driver.switch_to.active_element.find_element(By.XPATH, value="/html/body/div[2]/div/div[1]/div/div/div[3]/button[1]")
# attr.click()
