# coding:"utf-8"

import argparse
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


parser = argparse.ArgumentParser(description='input plz.')
parser.add_argument('--p', required=True, help='input plz.')
args = parser.parse_args()

# information
email = "example@outlook.com"
telephone = "177777777"
src = "https://003-iz.impfterminservice.de/impftermine/service?plz="+str(args.p)
# src = "https://097-iz.impfterminservice.de/impftermine/service?plz=04910"
age = "25"
driver_path = "PATH/OF/chromedriver"

# xpath
button_no = "/html/body/app-root/div/app-page-its-login/div/div/div[" \
            "2]/app-its-login-user/div/div/app-corona-vaccination/div[2]/div/div/label[2]/span "
button_yes = "/html/body/app-root/div/app-page-its-login/div/div/div[" \
             "2]/app-its-login-user/div/div/app-corona-vaccination/div[3]/div/div/div/div[" \
             "2]/div/app-corona-vaccination-no/form/div[1]/div/div/label[1]/span "
button_confirm = "/html/body/app-root/div/app-page-its-login/div/div/div[" \
                 "2]/app-its-login-user/div/div/app-corona-vaccination/div[3]/div/div/div/div[" \
                 "2]/div/app-corona-vaccination-no/form/div[4]/button "
box_email = "/html/body/app-root/div/app-page-its-check-result/div/div/div[" \
            "2]/div/div/div/div/app-its-check-success/div/form/div[1]/label/input "
box_tel = "/html/body/app-root/div/app-page-its-check-result/div/div/div[" \
          "2]/div/div/div/div/app-its-check-success/div/form/div[2]/label/div/input "
get_code = "/html/body/app-root/div/app-page-its-check-result/div/div/div[" \
           "2]/div/div/div/div/app-its-check-success/div/form/div[3]/button "
box_sms = "/html/body/app-root/div/app-page-its-check-result/div/div/div[" \
          "2]/div/div/div/div/app-its-check-success/div/form/div[1]/label/input "
box_birth = '/html/body/app-root/div/app-page-its-login/div/div/div[2]/app-its-login-user/div/div/app-corona-vaccination/div[3]/div/div/div/div[2]/div/app-corona-vaccination-no/form/div[3]/div/div/input'

web = webdriver.Chrome(driver_path)
web.get(src)

time.sleep(3)

# cookie 确认
button_cookie = "/html/body/app-root/div/div/div/div[3]/div[2]/div/div[1]/a"
button_cookie2 = "/html/body/app-root/div/div/div/div[3]/div[2]/div/div[2]/a"

try:
    web.find_element_by_xpath(button_cookie).click()
except NoSuchElementException:
    print("cookie1 button not found")

time.sleep(1)

#try:
#    web.find_element_by_xpath(button_cookie2).click()
#except NoSuchElementException:
#    print("cookie2 button not found")
    
count = 1
print("\a")

while True:
    try:
        web.find_element_by_xpath(button_no).click()
    except NoSuchElementException:
        print("waiting room......")
        time.sleep(10)
        # 如果从waiting room进入预约界面，可能出现cookie
        try:
            web.find_element_by_xpath(button_cookie).click()
        except NoSuchElementException:
            pass
        continue
    else:  # 网页加载正常，尝试进行预约
        print(str(args.p)+": 正在进行第"+str(count)+"次尝试")
        count += 1
        time.sleep(4)
        if count > 1 and (count - 1) % 100 == 0:
            print("______正在刷新网页______")
            web.refresh()
            time.sleep(3)
        try:
            web.find_element_by_xpath(button_yes).click()
        except NoSuchElementException:
            print("  暂无code，正在重试...")
            continue
        else:
            print("  有可用code")
            web.find_element_by_xpath(button_yes).click()
            time.sleep(1)
            web.find_element_by_xpath(box_birth).send_keys("20001111")
            time.sleep(0.5)
            web.find_element_by_xpath(button_confirm).click()
            time.sleep(1)
            try:
                web.find_element_by_xpath(box_email).send_keys(email)
            except NoSuchElementException:
                print("    code已被抢完，正在重试...")
                continue
            else:
                time.sleep(0.5)
                web.find_element_by_xpath(box_tel).send_keys(telephone)
                time.sleep(0.5)
                web.find_element_by_xpath(get_code).click()
                try:
                    web.find_element_by_xpath(box_sms)
                except NoSuchElementException:
                    print("      验证码未成功发送...")

                    continue
                else:
                    print("已成功获取code，请尽快查看手机，填写验证码！")
                    for i in range(100):
                        print("\a")
                        time.sleep(0.8)
                    time.sleep(600)
                    break
