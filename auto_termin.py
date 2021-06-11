# coding:"utf-8"

import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import datetime
import time


# infomation
src = "https://003-iz.impfterminservice.de/impftermine/suche/CH12-P128-R112/71111"  # address of ur code
driver_path = "/PATH/OF/chromedriver"

# personal data
sex = "male"
name = "A"
last_name = "B"
post = "11111"
ort = "Berlin"
street = "Straße"
number = "1"
tel = "1234567"
email = "e@outlook.com"

# xpath
button_cookie = "/html/body/app-root/div/div/div/div[2]/div[2]/div/div[1]/a"
button_find_termin = "/html/body/app-root/div/app-page-its-search/div/div/div[2]/div/div/div[5]/div/div[1]/div[" \
                     "2]/div[2]/button "
button_confirm_termin = '//*[@id="itsSearchAppointmentsModal"]/div/div/div[2]/div/div/form/div[2]/button[1]'

# information_xpath
button_data = "/html/body/app-root/div/app-page-its-search/div/div/div[2]/div/div/div[5]/div/div[2]/div[2]/div[2]/button"
male = '//*[@id="itsSearchContactModal"]/div/div/div[2]/div/form/div[1]/app-booking-contact-form/div[1]/div/div/div[1]/label[1]/span'
female = '//*[@id="itsSearchContactModal"]/div/div/div[2]/div/form/div[1]/app-booking-contact-form/div[1]/div/div/div[1]/label[2]/span'
box_name = '//*[@id="itsSearchContactModal"]/div/div/div[2]/div/form/div[1]/app-booking-contact-form/div[2]/div[1]/div/label/input'
box_last_name = '//*[@id="itsSearchContactModal"]/div/div/div[2]/div/form/div[1]/app-booking-contact-form/div[2]/div[2]/div/label/input'
box_post = '//*[@id="itsSearchContactModal"]/div/div/div[2]/div/form/div[1]/app-booking-contact-form/div[3]/div[1]/div/label/input'
box_ort = '//*[@id="itsSearchContactModal"]/div/div/div[2]/div/form/div[1]/app-booking-contact-form/div[3]/div[2]/div/label/input'
box_street = '//*[@id="itsSearchContactModal"]/div/div/div[2]/div/form/div[1]/app-booking-contact-form/div[4]/div[1]/div/label/input'
box_number = '//*[@id="itsSearchContactModal"]/div/div/div[2]/div/form/div[1]/app-booking-contact-form/div[4]/div[2]/div/label/input'
box_tel = '//*[@id="itsSearchContactModal"]/div/div/div[2]/div/form/div[1]/app-booking-contact-form/div[4]/div[3]/div/label/div/input'
box_email = '//*[@id="itsSearchContactModal"]/div/div/div[2]/div/form/div[1]/app-booking-contact-form/div[5]/div/div/label/input'
button_confirm = '//*[@id="itsSearchContactModal"]/div/div/div[2]/div/form/div[2]/button[1]'
button_book = '/html/body/app-root/div/app-page-its-search/div/div/div[2]/div/div/div[5]/div/div[3]/div[2]/div[2]'
button_cancel = '//*[@id="itsSearchAppointmentsModal"]/div/div/div[2]/div/div/form/div[2]/button[2]'

web = webdriver.Chrome(driver_path)
web.get(src)

time.sleep(3)
web.get(src)
time.sleep(1)
try:
    web.find_element_by_xpath(button_cookie).click()
except NoSuchElementException:
    pass
time.sleep(3)

count = 98
while True:
    try:
        web.find_element_by_xpath(button_find_termin).click()
    except NoSuchElementException:
        print("waiting room...")
        time.sleep(5)
        continue
    time.sleep(0.5)
    try:
        web.find_element_by_id("itsSearchAppointmentsModal").click()
        time.sleep(0.5)
        web.find_element_by_xpath(button_confirm_termin).click()
        time.sleep(0.5)
        web.find_element_by_xpath(button_data).click()

    except ElementClickInterceptedException:
        count += 1
        if count % 100:
            web.find_element_by_xpath(button_cancel).click()
            print("Kein Termin..." + str(count))
            time.sleep(3)
            continue
        else:
            print("Kein Termin..." + str(count))
            print("Refreshing......")
            web.quit()
            time.sleep(1)
            web = webdriver.Chrome(driver_path)
            web.get(src)
            time.sleep(1)
            web.get(src)
            time.sleep(1)
            continue

    else:
        break


if sex == "male":
    web.find_element_by_xpath(male).click()
else:
    web.find_element_by_xpath(female).click()
time.sleep(0.2)
web.find_element_by_xpath(box_name).send_keys(name)
web.find_element_by_xpath(box_last_name).send_keys(last_name)
web.find_element_by_xpath(box_post).send_keys(post)
web.find_element_by_xpath(box_ort).send_keys(ort)
web.find_element_by_xpath(box_street).send_keys(street)
web.find_element_by_xpath(box_number).send_keys(number)
web.find_element_by_xpath(box_tel).send_keys(tel)
web.find_element_by_xpath(box_email).send_keys(email)

time.sleep(0.5)
web.find_element_by_xpath(button_confirm).click()

time.sleep(0.5)
web.find_element_by_xpath(button_book).click()

print("预约成功")
time.sleep(1000)
