import pyautogui
import webbrowser as wb
import time
import pywhatkit


def send_multiple_messages(message, count):
    for _ in range(count):
        pyautogui.write(message)
        pyautogui.press('enter')
        time.sleep(0.5)  

wb.open('https://web.whatsapp.com')


time.sleep(30)


send_multiple_messages('hai', 200)

pywhatkit.sendwhatmsg("+918946003016", "hello world", 10, 47)
