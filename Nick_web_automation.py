
# this is code that shows how python can do web automation dont know how it works as yet but hoping to figure it out!

conf = yaml.full_load(open('loginDetails.yml'))
myUserName = conf['test_site_user']['email']
myPassword = conf['test_site_user']['password']
 
driver = webdriver.Chrome()
 
# driver.get('https://practicetestautomation.com/practice-test-login/')
# driver.find_element(By.NAME, "username").send_keys('just work')
 
 
 
def login (url, usernameId, username, passwordId, password, submit_buttonId):
    driver.get(url)
    time.sleep(5)
    driver.find_element(By.NAME,'username').send_keys(username)
    driver.find_element (By.NAME, "password").send_keys(password)
    driver.find_element (By.ID, "submit").click()
    time.sleep(10)
 
def close_button (close_buttonId):
    close_buttonId = driver.find_element (By.XPATH, "/html/body/div[1]/div/section/div/div/article/div[2]/div/div/div/a").click()
    time.sleep(3)
   
login('https://practicetestautomation.com/practice-test-login/', "username", myUserName, "password", myPassword, "submit" )
close_button (close_button)

