import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e63dcafb
import time

path = '/Users/kevinheredia/Desktop/Webster/chromedriver'
myName = 'Kevin Heredia'
myEmail = 'Kevin.heredia@icloud.com'
myPhone = '435-730-1813'
currentEmployer = 'Self-employed'
linked = 'https://www.linkedin.com/in/kevin-heredia-11955818b'
portfolio = 'https://kevinherediaportfolio.imfast.io'


driver = webdriver.Chrome(path)
driver.get('https://jobs.lever.co/pillpack/e63dcafb-b658-44dc-865b-0a9083e9c7e1/apply')
# driver.get('https://www.google.com/')

name = driver.find_element(By.NAME, "name")
email = driver.find_element(By.NAME, 'email')
phone = driver.find_element(By.NAME, 'phone')
resume = driver.find_element(By.ID,'resume-upload-input')
linkedIn = driver.find_element(By.NAME,'urls[LinkedIn]')
currentCompany = driver.find_element(By.NAME,'org')
portfolioInput = driver.find_element(By.NAME, 'urls[Portfolio]')

# resume.send_keys(Keys.ENTER)
name.send_keys(myName + Keys.TAB)
email.send_keys(myEmail + Keys.TAB)
phone.send_keys(myPhone + Keys.TAB)
currentCompany.send_keys(currentEmployer + Keys.TAB)
linkedIn.send_keys(linked + Keys.TAB)
portfolioInput.send_keys(portfolio + Keys.TAB)




# try:
#      main = WebDriverWait(driver, 10).until(
#          e63dcafb.presence_of_element_located((By.ID, 'name'))
#      )
#      tag = main.find_elements_by_tag_name('div')
#      main.send_keys(myName + Keys.TAB)

# except:
#         driver.quit()








# web.go_to("google.com")
# web.go_to('google.com')

# # web.go_to('https://jobs.lever.co/pillpack/e63dcafb-b658-44dc-865b-0a9083e9c7e1/apply')
# web.press('Full Name')
# web.type('Kevin Heredia')  # or web.press(web.Key.SHIFT + 'hello its me')
# web.press(web.Key.tab)

# web.go_back()
# web.click('Sign in')
# web.type('mymail@gmail.com', into='Email')
# web.click('NEXT', tag='span')
# web.type('mypassword', into='Password', id='passwordFieldId')
# web.click('NEXT', tag='span')  # you are logged in . woohoooo
