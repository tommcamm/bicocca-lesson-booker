import sys
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


def execute_booking(username, password):
    # Starts the driver in headless mode
    options = Options()
    options.headless = False
    driver = webdriver.Firefox(options=options)
    driver.get("https://gestioneorari.didattica.unimib.it/PortaleStudentiUnimib/index.php?view=login&include=login"
               "&from=prenotalezione&from_include=prenotalezione_home&_lang=it")

    driver.implicitly_wait(5)

    # Accept privacy slider
    element = driver.find_element_by_class_name("switch")
    element.click()

    # Open login page
    element = driver.find_element_by_id("oauth_btn")
    element.click()

    # Fill with login info
    # username
    element = driver.find_element_by_id("username")
    element.clear()
    element.send_keys(username)

    # password
    element = driver.find_element_by_id("password")
    element.clear()
    element.send_keys(password)
    # Login
    element.send_keys(Keys.RETURN)

    # Open book a lesson
    element = driver.find_element_by_link_text("Prenota il tuo posto a lezione")
    element.click()

    # Opens "new booking"
    element = driver.find_element_by_partial_link_text("Nuova prenotazione")
    element.click()

    # Execute the booking
    element = driver.find_elements_by_partial_link_text("Verifica e prenota il tuo posto")

    if len(element) == 0:
        print("No bookable lessons found...")
        print("Booking operation finished")
        driver.quit()
        sys.exit(2)
    else:
        book_count = 0
        for i in element:
            i.click()
            print(
                "Lesson booked: " + driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[2]/span/p[2]/b")
                .get_attribute("innerHTML"))
            driver.find_element_by_xpath(".//*[@class='btn normal-button custom-btn-service']").click()
            book_count = book_count + 1

        print("booked " + str(book_count) + " lesson(s)")
        driver.quit()

    print("Booking operation finished")
