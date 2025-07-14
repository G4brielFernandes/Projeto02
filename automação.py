import pyautogui as pa 
from time import sleep


def enviar_zap(nome_contrato , vendedor ,on = False):
    v = 'laiz'
    nome = 'Modelo'
    pa.press('win')
    sleep(1)
    pa.write('chrome')
    sleep(1)
    pa.press('enter')
    sleep(1)
    pa.write('whatsapp')
    sleep(1)
    pa.press('enter')
    sleep(10)
    pa.click(x=248, y=231) 
    pa.write(v)
    pa.press('enter')
    sleep(1)
    pa.click(x=765, y=957)
    sleep(1)
    pa.click(x=818, y=635)
    sleep(4)
    pa.click(x=589, y=778)
    pa.write(f'Contrato - {nome}.docx')
    sleep(4)
    pa.press('enter')
    sleep(2)
    pa.click(x=1826, y=918)


# sleep(5)
# print(pa.position())