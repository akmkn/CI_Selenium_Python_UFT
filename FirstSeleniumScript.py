from selenium import webdriver
driver = webdriver.Chrome("C:\\Python27\\selenium\\webdriver\\chromedriver_win32\\chromedriver.exe")
#driver = webdriver.Chrome()
driver.get("http://ch3lxcrmwsut401/ecommunications_open_db/start.swe?SWECmd=AutoOn")
driver.implicitly_wait(20)
driver.find_element_by_name("SWEUserName").send_keys("crm_tester42")
driver.find_element_by_name("SWEPassword").send_keys("equinix")
driver.find_element_by_link_text("Login").click()
