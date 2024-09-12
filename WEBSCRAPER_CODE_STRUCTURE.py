# -- Import the neccessary libraries --
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium. webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service

import traceback
import time
from datetime import datetime

# from pymongo import MongoClient

#### ! pip install pymongo

# # Connect to MongoDB
# client = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB URI if different
# db = client['mydatabase']  # Replace 'mydatabase' with your database name
# collection = db['mycollection']  # Replace 'mycollection' with your collection name


# -- Constant variables --
service = Service('chromedriver.exe')

# -- Get the driver --
def get_driver(link: str):
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")  # to prevent the infobars popups to interfere with the script
    options.add_argument("start-maximized")  # some webpages may change the content depending on the size of the window so we access the maximized version of the browser
    options.add_argument("disable-dev-shm-usage")  # to avoid issues while interacting with the browser on a linux computer and replit is a linux computer
    options.add_argument("no-sandbox")  # to disable sandbox in the browser
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get(link)
    return driver

# -- Logic to scrape the data --
def navigate_down_and_data_generation(Driver):
    
    # -- Check if the home page is loaded or not --
    try:
        wait(Driver, 90).until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text() ,'Top 20' )]")))
        print("Home page is loaded")
    except:
        print("Unable to load home page")
        return True
    
    try:
        # -- Scraping Logic --
        for Search in range(1, 1000):
            print(f"\n=========== Running Dog : {Search} ===============\n")
            try:
                dog_name = wait(Driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//dog-name-fetching-xpath)[" + str(Search) + "]"))).text
                print("Dog Name : '" + str(dog_name) + "'\n")

                dog_desc = wait(Driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//dog-desc-fetching-xpath)[" + str(Search) + "]"))).text
                print("Dog Description : '" + str(dog_desc) + "'\n")


                # # -- Store the data --
                # data = {
                #     "dog_name": str(dog_name),
                #     "dog_desc": str(dog_desc)
                # }
                # result = collection.insert_one(data)

            except:
                wait(Driver, 30).until(EC.visibility_of_element_located((By.XPATH, "(//dog-name-fetching-xpath)[" + str(Search - 1) + "]"))).text
                print("\n============= Dog Name Scraping ended ==================\n")
                break
    except:
        print("!!! Issue in fetching data")
        print(traceback.format_exc())
        return True

# -- Start the BOT process --
def runbot():
    global link
    start_time = datetime.now()
    print("+++++++++++++++++++++++++ Automation process started +++++++++++++++++++")
    
    driver = get_driver(link=link)
    navigate_down_and_data_generation(driver)
    
    print("+++++++++++++++++++++++++ Automation process ended +++++++++++++++++++++")

    end_time = datetime.now()
    time_taken = end_time - start_time
    time_taken = datetime.strptime(time_taken, "%H:%M:%S")
    print(f"************* Time Taken: {time_taken} ******************")


# --------------- Changeable variables ------------------------
link = "https://supertails.com/blogs/posts/hot-picks-top-dog-breeds-suited-for-indian-climate?srsltid=AfmBOor1d6c2cYMIw97E3111C8lwXz_zWUAnScRWkVpPlxwrq8QhU4Y0"  # the link to the webpage you want to
# -------------------------------------------------------------

if __name__ == '__main__':
    runbot()