from selenium import webdriver
driver = webdriver.Chrome("/Users/busrakoseoglu/PycharmProjects/pythonSelenium/drivers/chromedriver")
driver.get("https://www.enuygun.com")
title = driver.title
print(title)

driver.implicitly_wait(2)
driver.maximize_window()
driver.find_element_by_id("OriginInput").send_keys("İzmir, Türkiye ADB (Adnan Menderes Havalimanı)")
driver.find_element_by_id("DestinationInput").send_keys("Antalya, Türkiye AYT (Antalya Havalimanı)")
driver.find_element_by_name("DepartureDate").click()













