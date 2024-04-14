import webbrowser
import time
import pyautogui

# Open a new tab in your default browser and navigate to Google
webbrowser.open_new_tab('http://www.google.com')
# Wait a few seconds to let the page load
time.sleep(5)  # Adjust this depending on the speed of your internet connection

# Use pyautogui to type 'current temperature' into Google search bar with slow key input
pyautogui.write('current temperature', interval=0.25)
# Press the 'Enter' key to execute the search
pyautogui.press('enter')
