from selenium import webdriver

webpage = r"http://eggnogdb.embl.de/#/app/home/" # edit me
searchterm = 'rspg'# edit me

driver = webdriver.Chrome()
driver.get(webpage)

sbox = driver.find_element_by_class_name("input-group")
sbox.clear()
sbox.send_keys(searchterm)

submit = driver.find_element_by_class_name("input-group")
submit.click()
print submit.click()
