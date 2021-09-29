import time
import os
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

load_dotenv()


def execute_booking():
    driver = webdriver.Firefox()
    driver.get("https://gestioneorari.didattica.unimib.it/PortaleStudentiUnimib/index.php?view=login&include=login"
               "&from=prenotalezione&from_include=prenotalezione_home&_lang=it")

    # Accept privacy slider
    element = driver.find_element_by_class_name("switch")
    element.click()

    # Open login page
    element = driver.find_element_by_id("oauth_btn")
    element.click()

    time.sleep(2)
    # Fill with login info
    # username
    element = driver.find_element_by_id("username")
    element.clear()
    element.send_keys(os.environ.get("username"))

    # password
    element = driver.find_element_by_id("password")
    element.clear()
    element.send_keys(os.environ.get("password"))
    # Login
    element.send_keys(Keys.RETURN)

    time.sleep(1)
    # Open book a lesson
    element = driver.find_element_by_link_text("Prenota il tuo posto a lezione")
    element.click()

    # Opens "new booking"
    element = driver.find_element_by_partial_link_text("Nuova prenotazione")
    element.click()

    # Execute the booking
    element = driver.find_elements_by_partial_link_text("Verifica e prenota il tuo posto")

    for i in element:
        i.click()
        time.sleep(0.5)
        driver.find_element_by_xpath(".//*[@class='btn normal-button custom-btn-service']").click()

    print("Booking operation finished")


execute_booking()

# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "" not in driver.page_source
# driver.close()
