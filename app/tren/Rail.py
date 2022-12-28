from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(executable_path=r"C:\driver_chrome\chromedriver.exe")
driver.get("http://python.org")
driver.quit()