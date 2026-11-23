
import pyautogui
import time
import os
from datetime import datetime

# ==========================================
# DAILY REPORT AUTOMATION
# GenAI Architect Assignment 1
# Library: PyAutoGUI only
# ==========================================

# STEP 1: SAFETY SETTINGS

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1

print("================================")
print("DAILY REPORT AUTOMATION STARTED")
print("================================")

print("Please do not move the mouse.")
time.sleep(3)

# STEP 2: DATE AND TIME

now = datetime.now()

today = now.strftime("%Y-%m-%d")
current_time = now.strftime("%Y-%m-%d %H:%M:%S")
file_time = now.strftime("%H-%M-%S")

# STEP 3: CREATE OUTPUT FOLDER

project_folder = os.getcwd()

output_folder = os.path.join(
    project_folder,
    "output"
)

os.makedirs(output_folder, exist_ok=True)

excel_file = os.path.join(
    output_folder,
    f"daily_report_{today}_{file_time}.xlsx"
)

screenshot_file = os.path.join(
    output_folder,
    f"daily_report_{today}_{file_time}.png"
)

print("\nDate:", today)
print("Time:", current_time)

# STEP 4: OPEN GOOGLE CHROME

print("\nSTEP 1: Opening Google Chrome...")

pyautogui.hotkey("win", "r")
time.sleep(2)

pyautogui.write("chrome", interval=0.1)
pyautogui.press("enter")

time.sleep(8)

# STEP 5: OPEN WEATHER WEBSITE

print("\nSTEP 2: Opening Chennai weather...")

pyautogui.hotkey("ctrl", "l")

pyautogui.write(
    "https://wttr.in/Chennai?format=3",
    interval=0.05
)

pyautogui.press("enter")

time.sleep(10)

# STEP 6: COPY WEATHER INFORMATION

print("\nSTEP 3: Copying weather information...")

pyautogui.hotkey("ctrl", "a")
pyautogui.hotkey("ctrl", "c")

time.sleep(3)

print("Weather information copied to clipboard.")

# STEP 7: OPEN MICROSOFT EXCEL

print("\nSTEP 4: Opening Microsoft Excel...")

pyautogui.hotkey("win", "r")
time.sleep(2)

pyautogui.write("excel", interval=0.1)
pyautogui.press("enter")

time.sleep(12)

# STEP 8: CREATE NEW WORKBOOK

print("\nSTEP 5: Creating new Excel workbook...")

pyautogui.hotkey("ctrl", "n")
time.sleep(5)

# STEP 9: ENTER EXCEL HEADERS

print("\nSTEP 6: Entering Excel headers...")

pyautogui.write("Date & Time")
pyautogui.press("tab")

pyautogui.write("Fetched Data")
pyautogui.press("tab")

pyautogui.write("Comment")
pyautogui.press("enter")

# STEP 10: ENTER DATE AND TIME

print("\nSTEP 7: Entering date and time...")

pyautogui.write(current_time)
pyautogui.press("tab")

# STEP 11: PASTE WEATHER INFORMATION

print("\nSTEP 8: Pasting weather information...")

pyautogui.hotkey("ctrl", "v")
time.sleep(3)

# STEP 12: ENTER COMMENT

pyautogui.press("tab")

pyautogui.write(
    "Daily Chennai weather update"
)

time.sleep(3)

# STEP 13: FORMAT EXCEL

print("\nSTEP 9: Formatting Excel sheet...")

pyautogui.hotkey("ctrl", "g")
time.sleep(1)

pyautogui.write("A1:C1")
pyautogui.press("enter")

pyautogui.hotkey("ctrl", "b")

# Auto-fit columns
pyautogui.hotkey("ctrl", "a")
pyautogui.hotkey("alt", "h")
pyautogui.press("o")
pyautogui.press("i")

time.sleep(3)

# STEP 14: MAXIMIZE EXCEL

pyautogui.hotkey("win", "up")
time.sleep(2)

# STEP 15: SAVE EXCEL FILE

print("\nSTEP 10: Saving Excel report...")

pyautogui.press("f12")
time.sleep(5)

pyautogui.hotkey("ctrl", "a")

pyautogui.write(
    excel_file,
    interval=0.02
)

pyautogui.press("enter")
time.sleep(6)

# STEP 16: TAKE SCREENSHOT

print("\nSTEP 11: Taking screenshot...")

pyautogui.screenshot().save(
    screenshot_file
)

# STEP 17: FINAL MESSAGE

print("\n================================")
print("DAILY REPORT COMPLETED")
print("================================")

print("\nExcel File:")
print(excel_file)

print("\nScreenshot:")
print(screenshot_file)

print("\nAutomation completed successfully!")
