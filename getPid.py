# -*- coding: utf-8 -*-
import time #usada no sleep
from selenium import webdriver #usado pra abrir o navegador
from selenium.webdriver.common.keys import Keys #usado para enviar teclas especiais(tab, enter...)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

LINK = "https://web.whatsapp.com/"
WEBDRIVER_CHROME = "chromedriver.exe"
USUARIO_OU_GRUPO = "Stark"

def envia_msg(elemento, msg):
 mensagem = msg.decode('utf-8', 'ignore')
 # print "\n########enviando mensagem '%s' para '%s'\n#############\n" %(mensagem, elemento)
 elemento.send_keys(mensagem)
 elemento.send_keys(Keys.RETURN)
 time.sleep(1)

driver = webdriver.Chrome(WEBDRIVER_CHROME)
driver.get(LINK)

for i in range(1,25):
        print ("%i\n" %(i))
        time.sleep(1)
        input_text = driver.find_element_by_tag_name("input")
        input_text.send_keys(USUARIO_OU_GRUPO)
        time.sleep(1)
        input_text.send_keys(Keys.TAB)
        input_text.send_keys(Keys.TAB)
        input_text.send_keys(Keys.TAB)
        time.sleep(1)
        input_text = driver.find_element_by_class_name("_2S1VP")
        envia_msg(input_text, "Olá, humano! A era das máquinas começa agora!")
        input_text.send_keys(Keys.RETURN)