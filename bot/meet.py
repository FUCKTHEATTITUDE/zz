import logging
from config import Config
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bot import updater, browser, restricted
from telegram.ext import run_async
from telegram import ChatAction
import os
import pickle
import time
from os import execl
from sys import executable
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
userId = Config.USERID
def joinMeet(context, url_meet):

    def students(context):
        try:
            number = WebDriverWait(browser, 2400).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[6]/div[3]/div/div[2]/div[1]/span/span/div/div/span[2]'))).text
        except:
            return
        print(number)
        if(int(number) <10):
            context.bot.send_message(chat_id=userId, text="Your Class has ended!")
            browser.quit()
            execl(executable, executable, "chromium.py")

    try:
        browser.get(url_meet)
        browser.save_screenshot("ss.png")
        context.bot.send_chat_action(chat_id=userId, action=ChatAction.UPLOAD_PHOTO)
        mid  = context.bot.send_photo(chat_id=userId, photo=open('ss.png', 'rb'), timeout = 120).message_id
        os.remove('ss.png')

        if(browser.find_elements_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div')):
            browser.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div').click()
            time.sleep(3)

            context.bot.delete_message(chat_id=userId ,message_id = mid)

            browser.save_screenshot("ss.png")
            context.bot.send_chat_action(chat_id=userId, action=ChatAction.UPLOAD_PHOTO)
            mid = context.bot.send_photo(chat_id=userId, photo=open('ss.png', 'rb'), timeout = 120).message_id
            os.remove('ss.png')
        try:
            WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='NPEfkd RveJvd snByac' and contains(text(), 'Ask to join')]"))).click()
        except:
            WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='NPEfkd RveJvd snByac' and contains(text(), 'Join now')]"))).click()
        context.bot.delete_message(chat_id=userId ,message_id = mid)

        browser.save_screenshot("ss.png")
        context.bot.send_chat_action(chat_id=userId, action=ChatAction.UPLOAD_PHOTO)
        mid = context.bot.send_photo(chat_id=userId, photo=open('ss.png', 'rb'), timeout = 120).message_id
        os.remove('ss.png')
        a = ActionChains(browser)
        time.sleep(5)
        a.key_down(Keys.CONTROL).send_keys('d' + 'e').key_up(Keys.CONTROL).perform()
        context.bot.delete_message(chat_id=userId ,message_id = mid)
        time.sleep(7)
        browser.save_screenshot("ss.png")
        context.bot.send_chat_action(chat_id=userId, action=ChatAction.UPLOAD_PHOTO)
        mid = context.bot.send_photo(chat_id=userId, photo=open('ss.png', 'rb'), timeout = 120).message_id
        os.remove('ss.png')

        context.bot.send_chat_action(chat_id=userId, action=ChatAction.TYPING)
        context.bot.send_message(chat_id=userId, text="Attending your lecture. You can chill :v")
        logging.info("STAAAAPH!!")
    except Exception as e:
        context.bot.send_message(chat_id=userId, text="Error occurred! Fix error and retry!")
        context.bot.send_message(chat_id=userId, text=str(e))

    j = updater.job_queue
    j.run_repeating(students, 20, 1000)




