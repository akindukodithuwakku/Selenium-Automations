from time import sleep
from selenium import webdriver
from selenium.common import ElementClickInterceptedException , NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




def read_secrets(file_path):
    secrets = {}
    with open(file_path) as data:
        for line in data:
            key, value = line.strip().split('=')
            secrets[key] = value
    return secrets

# Read secrets from the file
secrets = read_secrets("secrets.txt")


# Extract the values
GMAIL_ID = secrets.get("GMAIL_ID")
GOOGLE_PWD = secrets.get("GOOGLE_PWD")


# Set up Chrome options to keep the browser open after the script completes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initialize the Chrome driver
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
# Open Tinder website
driver.get("http://www.tinder.com")

# Wait for the page to load
sleep(2)

# Accept cookies
accept_cookies = driver.find_element(By.XPATH, '//*[@id="c1323653706"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
accept_cookies.click()

# Wait for the cookies acceptance to be processed
sleep(1)

# Click the "Log in" button
tinder_login = driver.find_element(By.XPATH, '//*[text()="Log in"]')
tinder_login.click()

# Wait for the login options to appear
sleep(5)

sleep(2)
fb_login = driver.find_element(By.XPATH, value='//*[@id="c-404727370"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
fb_login.click()

# Wait for the new window to appear
sleep(2)

# Switch to the new window
driver.switch_to.window(driver.window_handles[-1])

# Now perform the login using Gmail credentials
email_field = driver.find_element(By.XPATH, '//*[@id="email"]')
email_field.send_keys(GMAIL_ID)


# Wait for the next page to load
sleep(5)

password_field = driver.find_element(By.XPATH, '//*[@id="pass"]')
password_field.send_keys(GOOGLE_PWD)

sleep(5)

password_field.send_keys(Keys.ENTER)


sleep(10)
#Allow location
allow_location_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, 'button[data-testid="allow"]'))
)
allow_location_button.click()
sleep(3)


notifications_button = driver.find_element(By.XPATH, value='//*[@id="c-404727370"]/div/div/div/div/div[3]/button[1]')
notifications_button.click()

cookies = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()
sleep(3)
for n in range(100):

    # Add a 2-second delay between likes.
    sleep(2)

    try:
        print("Clicking the Like button...")
        heart_icon = driver.find_element(By.XPATH, value="//*[@id='t2067052097']/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button")
        heart_icon.click()

    # For "It's a match" pop-up!
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()
        # For "Tinder Gold" pop-up
        except NoSuchElementException:
            close_tinder_gold = driver.find_element(By.XPATH, value="//*[@id='t338671021']/div/div[2]/div[2]/button")
            close_tinder_gold.click()

    # If the Like button changes XPath after the first Like
    except NoSuchElementException:
        try:
            heart_icon = driver.find_element(By.XPATH, value="//*[@id='t2067052097']/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button")
            heart_icon.click()
        # For "Add Tinder to your Home Screen" pop-up
        except ElementClickInterceptedException:
            not_interested_button = driver.find_element(By.XPATH, value="//*[@id='t338671021']/div/div/div[2]/button[2]/div[2]/div[2]/div")
            not_interested_button.click()

driver.quit()