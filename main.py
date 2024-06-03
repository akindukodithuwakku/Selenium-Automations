
#creating a new driver
# stay_alive = webdriver.ChromeOptions()
# stay_alive.add_experimental_option("detach", True)

# drive = webdriver.Chrome(options=stay_alive)

# drive.get("https://survey.stackoverflow.co/2023/#most-popular-technologies-office-stack-async")
# popular_DB = drive.find_element((By.XPATH, '//*[@id="office-stack-async7gn0x"]/tbody/tr[1]/td[1]'))
#
# print(f"the most popular: {popular_DB}")


#locators in selenium

# drive.get("https://www.python.org/")
# times = drive.find_element(By.CSS_SELECTOR,"say-no-more")
# names = drive.find_element((By.CLASS_NAME, "event-widget li a"))
#
# events = {}
#
# for n in range(len(times)):
#     events[n] = {
#         "time" : times[n].text,
#         "name" : names[n].text,
#     }
# print(events)

# drive.get("https://en.wikipedia.org/wiki/Main_Page")
#
# # article_count = drive.find_element(By.CSS_SELECTOR, "#articlecount a")
# # print(article_count.text)
#
# click_links = drive.find_element(By.LINK_TEXT, "Content portals")
#
# search = drive.find_element(By.NAME, "search")
# time.sleep(1)
# search.send_keys("Machine Learning", Keys.ENTER)


#------------------------------------------------------------------------------------------------

#tinder auto swapping bot

from time import sleep
from selenium import webdriver
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

# Locate the iframe
iframe = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//iframe[@title="Google බොත්තම සමගින් පුරන්න"]'))
)

# Switch to the iframe
driver.switch_to.frame(iframe)

# Wait for the Google login button to be present and clickable
google_login = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//div[@role="button" and @aria-labelledby="button-label"]'))
)
google_login.click()

# Wait for the new window to appear
sleep(5)

# Switch to the new window
driver.switch_to.window(driver.window_handles[-1])


# Now perform the login using Gmail credentials
email_field = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
email_field.send_keys(GMAIL_ID)
email_field.send_keys(Keys.ENTER)

# Wait for the next page to load
sleep(10)

password_field = driver.find_element(By.XPATH, '//*[@name="password"]')
password_field.send_keys(GOOGLE_PWD)
password_field.send_keys(Keys.ENTER)

# Add any additional steps if required after login

driver.quit()