from selenium import webdriver #10 gmails must login...
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

option = webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress","localhost:9222")

driver = webdriver.Chrome(options=option)
time.sleep(4)
driver.get("https://youtube.com/@akafortysevenn?si=JxVu862SEckZ-mRX") #replace with your required url
time.sleep(5)
driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

#2nd Gmail - 2 start(2)
driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item').click() #click on next channel.

time.sleep(4)
driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item').click() #click on next channel.

#3rd Gmail - 3 start(3)
time.sleep(4)
driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item').click() #click on next channel.

#4th Gmail-start(4)
time.sleep(4)
driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item').click() #click on next channel.

#5th gmail - start(5)
time.sleep(4)
driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item').click() #click on next channel.

#6th Gmail - start(6)
time.sleep(4)
driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item').click() #click on next channel.

#7th Gmail - start(7)
time.sleep(4)
driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item').click() #click on next channel.

#8th Gmail - start (8)
time.sleep(4)
driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item').click() #click on next channel.

#9th gmail - 9 start (9)
time.sleep(4)
driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item').click() #click on next channel.

#10th Gmail - 10 start (10)
time.sleep(4)
driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)

driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(3)
driver.find_element_by_id("avatar-btn").click() #click on channel icon.
time.sleep(3)
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click() #click on switch account button.
time.sleep(3) 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item').click() #click on next channel.
time.sleep(4)
driver.find_element_by_xpath("//div[text()='Subscribe']/ancestor::button").click() #click on sub button
time.sleep(30)
#end > 10th acc - each acc contain 10 brand accs


