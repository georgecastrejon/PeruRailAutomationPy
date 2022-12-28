from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\driver_chrome\chromedriver.exe")
driver.get("http://python.org")
driver.close()