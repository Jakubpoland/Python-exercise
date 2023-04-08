import pyautogui
pyautogui.hotkey("win", "r")
pyautogui.typewrite("cmd")
pyautogui.press('enter')
pyautogui.typewrite("ipconfig")
pyautogui.press('enter')
pyautogui.typewrite("ping 8.8.8.8")
pyautogui.press('enter')