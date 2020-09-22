#-*- coding=utf8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep

############################################
username = "skyutech"
password = "sky4275"
############################################


driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')


driver.get("https://login.taobao.com/member/login.jhtml")

#element = driver.find_element_by_link_text("密码登录")
#element.click()
#driver.find_element_by_id("TPL_username_1").clear()
driver.find_element_by_id("TPL_password_1").clear()
driver.find_element_by_id("TPL_username_1").send_keys(username)
sleep(1);
driver.find_element_by_id("TPL_password_1").send_keys(password)
sleep(1);


#슬라이더를 가져옵니다size
span_background = driver.find_element_by_css_selector("#nc_1__scale_text > span")
span_background_size = span_background.size
print(span_background_size)

# 슬라이더의 위치를 ​​얻는다
button = driver.find_element_by_css_selector("#nc_1_n1z")
button_location = button.location
print(button_location)

# 드래그 조작：drag_and_drop_by_offset
# 슬라이더의 위치를 ​​슬라이더 길이만큼 초기 위치에서 오른쪽으로 이동합니다 (즉, x 좌표는 슬라이더 위치에 슬라이더 길이를 더한 값이고 y 좌표는 슬라이더의 좌표 위치를 유지합니다)
x_location = button_location["x"] + span_background_size["width"]
y_location = button_location["y"]
ActionChains(driver).drag_and_drop_by_offset(button, x_location, y_location).perform()
#driver.get_cookies()입수cookie


sleep(1)
driver.find_element_by_id("J_SubmitStatic").click()
cookie = "; ".join([item["name"] + "=" + item["value"] +"\n" for item in driver.get_cookies()])
print(cookie)