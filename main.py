import csv
import matplotlib.pyplot as plt
import os
from core import pull, logic, menu

dp = pull.DataPuller(browser_name="FireFox", driver_path="~/stathat", headless=True)
logic = logic.logic()
ChoiceMenu = menu.CoreMenu

#Main Program
url = input("[?] What is the download URL?: ")
try:
    dp.goto_url(url)
    page_source = dp.grab_source()
    print('[+] attempting to find element via data format tag...')
    element = dp.find_elm_by_XPATH("//a[@data-format='csv']")
    if element:
        print(f'[+] found element: {element}')
        download_button = element
    else:
        print('[-] could not find element via data format tag, trying partial link text "CSV"...')
        try:
            element = dp.find_elm_by_PARTEXT("CSV")
        except TimeoutError as e:
            print("[-] Error TimeOut: could not finding element via partial text.", e)
            element = None
            quit("[-] QUITTING... Could not find download link.")
        print(f'found element: {element}')
        download_button = element

    print("[+] Downloading file...")
    file_path = dp.download_file(download_button, wait_time=60)

    print("[+] Download complete:", file_path)

finally:
    os.system('clear' if os.name == 'posix' or 'unix' else 'cls')
    print("[!] finishing up...")
    dp.close()

data = logic.load_csv(file_path)
# https://catalog.data.gov/dataset/electric-vehicle-population-data
print("\nFirst 5 rows:")
for row in data[:5]:
    print(row)

menu_instance = ChoiceMenu(data)
menu_instance.display_menu()
