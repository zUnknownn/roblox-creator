import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Function to generate a random date of birth
def generate_random_date():
    month = random.randint(1, 12)
    day = random.randint(1, 28)  # Assuming all months have up to 28 days
    year = random.randint(1980, 2010)
    return month, day, year

# Read account names from a file
def read_account_names(file_path):
    with open(file_path, 'r') as file:
        names = file.read().splitlines()
    return names

# Setup Chrome WebDriver using webdriver_manager
driver = webdriver.Chrome(ChromeDriverManager().install())

# Roblox registration URL
url = 'https://www.roblox.com/account/signupredir'

# Get random name from file
account_names = read_account_names('account.txt')
random_name = random.choice(account_names)

# Generate random date of birth
birth_month, birth_day, birth_year = generate_random_date()

# Default password
default_password = '10101010'

try:
    # Open Roblox registration page
    driver.get(url)
    driver.maximize_window()  # Maximize the browser window for better visibility

    # Fill out registration form with explicit waits
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'MonthDropdown'))).send_keys(str(birth_month))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'DayDropdown'))).send_keys(str(birth_day))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'YearDropdown'))).send_keys(str(birth_year))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'signup-username'))).send_keys(random_name)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'signup-password'))).send_keys(default_password)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'signup-password-confirm'))).send_keys(default_password)

    # Select gender (example, adjust based on your HTML)
    gender_element_id = 'gender-male' if random.choice(['Male', 'Female']) == 'Male' else 'gender-female'
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, gender_element_id))).click()

    # Submit registration form
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'SignupButton'))).click()

    # Wait for registration to complete and check for successful redirection
    WebDriverWait(driver, 10).until(EC.url_contains('roblox.com/home'))

    # Print success message
    print(f"Account created successfully with username: {random_name}")

    # Save valid account to file
    with open('valid.txt', 'a') as file:
        file.write(f"{random_name}\n")

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close the browser
    driver.quit()
