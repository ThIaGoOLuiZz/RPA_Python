import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By

def waitingElement(limitTime, xpath, navegator):
    count = 0

    while count < limitTime:
        try:
            navegator.find_element(By.XPATH, xpath)
            pyautogui.sleep(2)
            print("Conseguiu!")
            break
        except:
            pyautogui.sleep(1)
            print("Não conseguiu!")
            count += 1


xpath = '//input[@id="username"]'
site = "https://practicetestautomation.com/practice-test-login/"

navegador = webdriver.Chrome()
navegador.get(site)

waitingElement(10, xpath, navegador)

username = navegador.find_element(By.XPATH, '//*[@id="login"]/ul/li[2]/b[1]').text
password = navegador.find_element(By.XPATH, '//*[@id="login"]/ul/li[2]/b[2]').text

navegador.find_element(By.ID, 'username').send_keys(username)
navegador.find_element(By.ID, 'password').send_keys(password)
pyautogui.sleep(1)
navegador.find_element(By.ID, 'submit').click()
if "practicetestautomation.com/logged-in-successfully/" in navegador.current_url:
    print('mission acumplished')
else:
    print('mission failed')
pyautogui.sleep(2)
navegador.find_element(By.XPATH, '//*[@id="loop-container"]/div/article/div[2]/div/div/div/a').click()
pyautogui.sleep(2)
navegador.quit()