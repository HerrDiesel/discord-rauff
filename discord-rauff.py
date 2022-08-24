#!/usr/bin/env python3
### DEPENDENCIES

## Selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys

## Other dependencies
import time
import os
import json
import sys
import csv
from pathlib import Path

## Is Windows? Otherwise, assume Linux.
is_windows = sys.platform.startswith('win')

### MAIN
def main():
    ### OPTIONS
    sys.argv.append('')

    ## default options
    verbose = False
    if is_windows:
        data_file = os.getcwd() + "\\data.tsv"
    else:
        data_file = os.getcwd() + '/data.tsv'

    ## check through args
    next_is_path = False
    for arg in sys.argv:
        arg = str(arg)

        if next_is_path:
            if  arg.startswith(("/", "\\", "~")):
                data_file = arg
            else:
                if is_windows:
                    data_file = os.getcwd() + "\\" + arg
                else:
                    data_file = os.getcwd() + "/" + arg
        next_is_path = False

        ## --help, -h, /help, /h
        if arg in {"--help", "-h", "/help", "/h"}:
            if str(sys.argv[0]) == "/usr/bin/discord-rauff":
                sys.argv[0] = "discord-rauff"
            print("Usage: " + str(sys.argv[0]) + " [OPTIONS] [ARGUMENTS]")
            print('    -i, --input, --from [PATH-TO-FILE]        uses the specified file as source instead of default $PWD/data.tsv')
            print("    -v, --verbose                             verbose")
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)
        
        ## --input, -i, /input, /i, --from
        elif arg in {"--input", "-i", "/input", "/i", "--from"}:
            next_is_path = True
        
        ## --verbose, -v, /verbose, /v
        elif arg in {"--verbose", "-v", "/verbose", "/v"}:
            verbose = True

        else:
            if arg != sys.argv[0]:
                break

    ### CONFIG.JSON

    ## Try to open "config.json" file
    try:
        if is_windows:
            with open('config.json', 'r', encoding="utf8") as jsonFile:
                config = json.load(jsonFile)
        else:
            with open(str(Path.home()) + "/.config/discord-rauff/config.json", 'r', encoding="utf8") as jsonFile:
                config = json.load(jsonFile)
    ## If there's no "config.json" file, generate one
    except:
        config = {}
        config["email"] = input("YOUR E-MAIL ADDRESS:: ")
        config["country"] = input("REPORTED USERS' COUNTRY (optional):: ") or ""
        config["age"] = "13"
        if config["country"]:
            config["age"] = input("LOCAL AGE RESTRICTION (defaults to 14+):: ").replace("+","") or "14"
        config["chrome_path"] = input("CHROMIUM-BASED BROWSER PATH (e.g., Chrome, Brave, Vivaldi, Opera):: ").replace('\\', '/') if is_windows else input("CHROMIUM-BASED BROWSER PATH (e.g., Chrome, Brave, Vivaldi, Opera):: ")
        config["driver_path"] = input("CHROME DRIVER PATH:: ").replace('\\', '/') if is_windows else input("CHROME DRIVER PATH:: ")

        if is_windows:
            with open('config.json', 'x', encoding="utf8") as jsonFile:
                json.dump(config, jsonFile)
        else:
            Path(str(Path.home()) + "/.config/discord-rauff").mkdir(parents=True, exist_ok=True)
            with open(str(Path.home()) + "/.config/discord-rauff/config.json", 'x', encoding="utf8") as jsonFile:
                json.dump(config, jsonFile)

    ## Get paths from config.json
    driver_path = Service(config["driver_path"])
    chrome_path = config["chrome_path"]

    ## Get e-mail address from config.json
    userEmail = config["email"]

    ## Get country from config.json
    country = config["country"]+"'s"

    ## Get age restriction from config.json
    ageRestriction = config["age"]

    ### CHROME SETUP

    ## Set Chrome options
    option = Options()
    option.binary_location = chrome_path
    option.add_argument("--incognito")
    option.add_argument("--disable-crash-reporter")
    option.add_argument("--disable-extensions")
    option.add_argument("--disable-in-process-stack-traces")
    option.add_argument("--disable-logging")
    option.add_argument("--disable-dev-shm-usage")
    option.add_argument("--log-level=3")
    option.add_argument("--output=/dev/null")
    option.add_argument("start-maximized")
    option.add_argument('--no-sandbox')
    option.add_argument("--disable-blink-features=AutomationControlled")
    option.add_experimental_option("excludeSwitches", ["enable-automation"])
    option.add_experimental_option('useAutomationExtension', False)
    option.add_argument("--disable-gpu")
    option.add_argument("--headless")

    ## Setup Chrome instance
    browser = webdriver.Chrome(service=driver_path, options=option)
    browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    browser.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})

    ### CLEAR TERMINAL
    os.system('cls' if is_windows else 'clear')

    ### ASCII ART
    print('................................................................................')
    print('................................................................................')
    print('................................................................................')
    print('.........................................%......................................')
    print('........................................(@......................................')
    print('........................................@@@.....................................')
    print('.......................................@@@@@....................................')
    print('..............................*@@@@@@.@@@@@@.@@@@(...........................@@@')
    print('..........................@@@@@@@@@@.@@@@@@,.@@@@@@@@@...................@@@@@@@')
    print('......................,@@@@@@@@@....&@@@@@@@....@@@@@@@@@@..........@@@@@@@@@@@@')
    print('....................@@@@@@@%........@@@@@@@@@.......*@@@@@@@....@@@@@@@@@@@@@@@@')
    print('..................@@@@@@@..........@@@@@@@@@@@.........@@@@(..@@@@@@@@@@@@@@@@@@')
    print('.................@@@@@%...........@@@@@#.@@@@@@........@@......@@@@@@@@@@@@@@@@@')
    print('...............@@@@@@............@@@@@@...@@@@@@..*@@@@@@@@......@@@@@@@@@@@@@@@')
    print('...............@@@@@............@@@@@@.....@@@..@@@@@@@@@@@@.....@@@@@@@@@@@@@@@')
    print('..............@@@@@.......................@.....@@@@@@@@@@@@@.....@@@@@@@@@@@@@@')
    print('.......................@@@@@@@@@@@@@@............................@@@@@@..&@@@@@@')
    print('.....@@@@@@@@@@@@@@@@@@@@@@@@@@@@.........................&#/*...........@@@@@@@')
    print('......@@@@@@@@@@@@@@.....@@@.......,.....@@@@@......@@@@@@@@@.@@.,@,............')
    print('......@@@@@@....,@@........@,.....@@......@@@@@.....&@@@@@@@&.....@@@@@@@@@@@@@@')
    print('...............@@@@*@@@...(/.....@@@@.......@@@@.....@@@@@@@.....@@@@@@@@@@@@@@@')
    print('...............@.....@@@@@@.....@@@@@@@.......@@%.....@@@@&.....@@@@@@@@@@@@@@@@')
    print('........../@@@@@@......@@@.....@@@@@@@@@@....@@@@......@@......@@@@@@@@@@@@@@@@@')
    print('......@@@@@@@@@@@@,............@@@@@@@@@@@@@@@@@@@......@@...@@@@@@@@@@@@@@@@@@@')
    print('..@@@@@@@@@@@@@@@@@@,.........@@@@@@@@@@@@@@@@@@@@@...../@&&@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@..........(@@@@@@@@@@@@....@@.....@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@........................@@...@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*..............*@@@@@..@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('................................................................................')
    print('discord-rauff v1.0.0 by Herr Diesel // Report underage users from file!')
    print('................................................................................')

    ### DISCORD WEBSITE
    try:
        ## Try to open the file
        with open(data_file, 'r', encoding="utf8") as f:
            reader = csv.reader(f,delimiter='\t')
            array = list(reader)
            f.seek(0)
            print("ROWS IMPORTED:: " + str(len(array)))
            print('................................................................................')

            ## Main loop
            submitted_reports = 0
            failed_reports = 0
            for col in array:
                try:
                    col.append('')
                    ## Go to Discord Support Page
                    browser.get('https://support.discord.com/hc/pl/requests/new?ticket_form_id=360000029731')
                    time.sleep(2)

                    repUserID = col[0]
                    if verbose: print("\nReported User ID:: " + str(repUserID))

                    repUserTag = col[1]
                    if verbose: print("Reported User Tag:: " + str(repUserTag))

                    repUserMsg = col[2]
                    if verbose: print("Reported User Message Link:: " + str(repUserMsg))

                    additionalInfo = col[3]
                    if verbose: print("Additional information regarding the report:: " + str(additionalInfo))

                    ## Insert e-mail address
                    emailField = browser.find_element("xpath",'//*[@id="request_anonymous_requester_email"]')
                    emailField.send_keys(userEmail)
                    if verbose: print("INSERTED THE E-MAIL ADDRESS")
                    time.sleep(0.125)

                    ## Navigate through "How can we help you" field
                    outerHowField = browser.find_element("xpath",'//*[@id="new_request"]/div[3]/a')
                    outerHowField.click()
                    innerHowField = browser.find_element("xpath",'//*[@id="__dc.ticket_form-tnsv1_report_other_issue__"]')
                    innerHowField.click()
                    if verbose: print('NAVIGATED THROUGH "How can we help you" FIELD')
                    time.sleep(0.251)

                    ## Navigate through "What do you want to report" field
                    outerWhatField = browser.find_element("xpath",'//*[@id="new_request"]/div[5]/a')
                    outerWhatField.click()
                    innerWhatField = browser.find_element("xpath",'//*[@id="__dc.ticket_form-tnsv1_cat_-_underage_user__"]')
                    innerWhatField.click()
                    if verbose: print('NAVIGATED THROUGH "What do you want to report" FIELD')
                    time.sleep(0.521)

                    ## Insert message link
                    msgLinkField = browser.find_element("xpath",'//*[@id="request_custom_fields_360008125792"]')
                    msgLinkField.send_keys(repUserMsg)
                    if verbose: print("INSERTED THE MESSAGE LINK")
                    time.sleep(0.251)

                    ## Insert report's topic
                    topicField = browser.find_element("xpath",'//*[@id="request_subject"]')
                    topicField.send_keys('Underage user')
                    if verbose: print("INSERTED REPORT'S TOPIC")
                    time.sleep(0.521)

                    ## Insert report's description
                    descField = browser.find_element("xpath",'//*[@id="request_description"]')
                    descField.send_keys("The following Discord user is under " + ageRestriction + " years of age and therefore under the " + country + " minimum age.")
                    descField.send_keys("The information has been provided to take appropriate action if needed.")
                    descField.send_keys(Keys.RETURN)
                    descField.send_keys(Keys.RETURN)
                    descField.send_keys("USER ID: ")
                    descField.send_keys(repUserID)
                    descField.send_keys(Keys.RETURN)
                    descField.send_keys("USER TAG: ")
                    descField.send_keys(repUserTag)
                    descField.send_keys(Keys.RETURN)
                    descField.send_keys(Keys.RETURN)
                    descField.send_keys(repUserMsg)
                    descField.send_keys(Keys.RETURN)
                    descField.send_keys(Keys.RETURN)
                    descField.send_keys(additionalInfo)
                    if verbose: print("INSERTED THE REPORT'S DESCRIPTION")
                    time.sleep(2)

                    ## Submit the report
                    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    submitButton = browser.find_element("xpath",'//*[@id="new_request"]/footer/input')
                    submitButton.click()
                    if verbose: print("SUBMITTED THE REPORT")
                    time.sleep(3)
                    submitted_reports += 1
                except Exception as e:
                    if verbose: print("ERROR:: " + str(e))
                    failed_reports += 1
                    continue
        print('................................................................................')
        print("SUBMITTED REPORTS:: " + str(submitted_reports) + "\nFAILED REPORTS:: " + str(failed_reports))
        print('................................................................................')
        browser.quit()

        if is_windows:
            os.system("pause")

    except Exception as e:
        if str(e).startswith("[Errno 2]"):
            print('ERROR:: Please provide "data.tsv" file or provide a custom file using "--from"\n')
        else:
            print(e)
        print('Stuck? Please consult with the manual or try running the program with "--help"')

### RUN

if __name__ == '__main__':
    try:
        main()
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

    except KeyboardInterrupt:
        print('\nInterrupted')

        if is_windows: exit_code = 3221225786
        else: exit_code = 130

        try:
            sys.exit(exit_code)
        except SystemExit:
            os._exit(exit_code)
