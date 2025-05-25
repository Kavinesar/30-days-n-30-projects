import pyautogui
import pyperclip
import subprocess
import time
contact = "7200906819" 
message = "This is an automated message from your PC "

subprocess.Popen("start whatsapp:", shell=True)

time.sleep(6)  

pyautogui.hotkey("ctrl", "f")
time.sleep(1)
pyperclip.copy(contact)
pyautogui.hotkey("ctrl", "v")
time.sleep(1)

pyautogui.press("down")  
time.sleep(0.5)
pyautogui.press("enter") 
time.sleep(1)
pyperclip.copy(message)
pyautogui.hotkey("ctrl", "v")
time.sleep(0.3)
pyautogui.press("enter")

