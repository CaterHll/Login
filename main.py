import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# initialize the webdriver
driver = selenium.webdriver.Chrome()

# go to the login page
driver.get("https://www.betika.com/en-ke/login")

# find the email input field and enter the email
email_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[contains(@type,'text')]")))
email_input.send_keys("254728214630")

# find the password input field and enter the password
password_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[contains(@type,'password')]"))
)
password_input.send_keys("kiplangat")

# find the login button and click it
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Login')]"))
)
login_button.click()

# wait for the login process to finish and verify if the user is logged in
try:
    welcome_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//button[contains(.,'Login')])[1]"))
    )
    print("Login successful!")
except:
    print("Login failed.")

# close the browser
#driver.quit()


#Placing a bet

driver.get('https://www.betika.com/en-ke/s/soccer')


