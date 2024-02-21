import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions
import requests

navegador = webdriver.Chrome()

navegador.get("https://www.google.com/recaptcha/api2/demo")


dataSite_Key = WebDriverWait(navegador, 10).until(expected_conditions.element_to_be_clickable((By.ID, "recaptcha-demo"))).get_attribute("data-sitekey")
url = navegador.current_url

urlAPI = f'https://2captcha.com/in.php?key=dfb9308670c98785268395a41b3bfb74&method=userrecaptcha&googlekey={dataSite_Key}&pageurl={url}'

payload = {}
headers = {}

response = requests.request("GET", urlAPI, headers=headers, data=payload)
requestID = response.text.replace('OK|','')

urlAPI = f'https://2captcha.com/res.php?key=dfb9308670c98785268395a41b3bfb74&action=get&id={requestID}'

while True:
    response = requests.request("GET", urlAPI, headers=headers, data=payload)
    if 'CAPCHA_NOT_READY' not in response.text:
        tokenCaptcha = response.text.replace('OK|','')
        break
    pyautogui.sleep(5)

navegador.execute_script(f'document.querySelector("#g-recaptcha-response").innerHTML = "{tokenCaptcha}"')
navegador.find_element(By.ID, 'recaptcha-demo-submit').click()

pyautogui.sleep(5)


    
