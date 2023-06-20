# pip install webdriver-manager
import chromedriver_autoinstaller
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from time import sleep
from datetime import datetime
import json
import os

class VerintSpider:
    # BUG: chromedriver_autoinstaller will override logging and cause when job missed, it will print to terminal.
    # to do:
    # 1. from cmpany PC, try run this script later after PC fully initiated.
    # 2. try specify a path for ChromeDrivermanager using below code.
    # possible soulution: try chromedriver_autoinstaller


    def __init__(self, URL, account, password, driver_path=chromedriver_autoinstaller.install(), 
                 output_dir = 'Jobs', json_name = "Verint.json",
                 do_output_json = True, do_output_screenshot = False, 
                 hide = False, disable_auto_close = False):
        self.URL = URL
        self.account = account
        self.password = password
        self.driver_path = driver_path
        self.output_dir = output_dir
        self.json_name = json_name
        self.do_output_json = do_output_json
        self.do_output_screenshot = do_output_screenshot
        self.hide = hide
        self.disable_auto_close = disable_auto_close
        
        # configure options
        driver_options = webdriver.ChromeOptions()
        driver_options.add_argument('log-level=3')
        driver_options.add_argument('--start-maximized') # maximum resolution
        driver_options.add_argument('--disable-gpu') # improve stability and performance in some cases.
        driver_options.add_argument('--disable-blink-feature=AutomationControlled') # help to prevent detection and blocking by websites that try to detect and block automated testing.
        if hide:
            self.disable_auto_close = False # If it run in backend, auto close msut be enabled to avoid Selenium unable to quit.
            driver_options.add_argument('--headless')
        driver_options.add_experimental_option('detach', disable_auto_close)  # True: not close automatically， False：close automatically

        self.driver_options = driver_options
        driver = webdriver.Chrome(executable_path=driver_path, options=self.driver_options)
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def runSpider(self):
        try:
            self.driver.get(url=self.URL)
            self.driver.find_element(By.ID, "username").send_keys(self.account, Keys.ENTER)
            self.driver.find_element(By.ID, "password").send_keys(self.password, Keys.ENTER) 
            sleep(7)

            personal_page = self.driver.current_url
            if "MYSCHEDULE_PERSONAL" not in personal_page:
                # Redirect to My Schedule
                self.wait.until(lambda driver: driver.find_element(By.XPATH, '//*[@id="1_MY_HOME->1_FS_MYSCHEDULE-btnInnerEl"]'))
                self.driver.find_element(By.XPATH, '//*[@id="1_MY_HOME->1_FS_MYSCHEDULE-btnInnerEl"]').click()

                sleep(3)
                # Redirect to Personal
                self.wait.until(lambda driver: driver.find_element(By.XPATH, '//*[@id="1_MY_HOME->1_FS_MYSCHEDULE->2_FS_MYSCHEDULE_PERSONAL-btnInnerEl"]'))
                self.driver.find_element(By.XPATH, '//*[@id="1_MY_HOME->1_FS_MYSCHEDULE->2_FS_MYSCHEDULE_PERSONAL-btnInnerEl"]').click()

            # Switch to iframe
            iframe = self.driver.find_element(By.ID, "mctnt")
            self.driver.switch_to.frame(iframe)

            # Switch to Graphic View
            viewButton = self.driver.find_element(By.ID, "viewType_0")

            # Find the "Graphical" option and click on it
            viewButton.click()
            viewButton.send_keys(Keys.DOWN)

            # Wait for the page to load after the selection is made
            WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element_value((By.ID, "viewType_0"), "Graphical"))

            # Get my schedule
            myShiftTable  = self.driver.find_element(By.ID, "dualList_rListWrapper")
            myShiftBody = myShiftTable.find_element(By.TAG_NAME, "tbody")
            myShiftBodyDays = myShiftBody.find_elements(By.CSS_SELECTOR, "[id^='dualList_rListr']:not([id$='c0'])")

            all_tasks_tmp = []
            for i,myShiftBodyDay in enumerate(myShiftBodyDays):
                # Expand all tasks in individual day from sub_elements
                dailyTasks = myShiftBodyDay.find_elements(By.CSS_SELECTOR, "[fancytitle]")

                # Extract information from each sub-element
                for task_tmp in dailyTasks:
                    starttime_unix = int(int(task_tmp.get_attribute('startdate'))/1000)
                    # endtime_unix = int(int(task_tmp.get_attribute('enddate'))/1000)

                    starttime_unix = datetime.fromtimestamp(starttime_unix)

                    # date = datetime(starttime_unix.year, starttime_unix.month, starttime_unix.day)
                    # startdate_f = (startdate).strftime('%Y-%m-%d')

                    starttime = starttime_unix
                    starttime_f = (starttime).strftime('%Y-%m-%d %H:%M')
                    
                    # endtime = datetime.fromtimestamp(endtime_unix)
                    # endtime_f = (endtime).strftime('%Y-%m-%d %H:%M')

                    task_title = (task_tmp.get_attribute('fancytitle')).split("\r")[0] # Drop the time text which no longer needed.

                    task = {}
                    # task["date"] = date
                    task["starttime"] = starttime_f
                    # task["endtime"] = endtime_f
                    task["task"] = task_title
                    
                    all_tasks_tmp.append(task)

            # Use for loop to remove duplicate tasks
            all_tasks = []
            for d in all_tasks_tmp:
                if d not in all_tasks:
                    all_tasks.append(d)
            
            if self.do_output_screenshot:
                self.takeScreenshot()
            if self.do_output_json:
                self.outputJson(all_tasks)
            if self.disable_auto_close:
                print("Spider ran completely, json updated. You can close the Verint window now.")
            else:
                print("Spider ran completely, json updated. ")
            return all_tasks
        except Exception as e:
            print("Spider ran failed with Error:", e)

    def takeScreenshot(self):
        current_time = time.strftime("%Y-%m-%d %H-%M-%S") # file name canont contains `:`
        filename = f"{current_time}.png"
        path = os.path.join(self.output_dir,filename)
        self.driver.save_screenshot(path)
        print(f"Screenshot {filename} saved in {path}")

    def outputJson(self, all_tasks):
        filename = self.json_name
        path = os.path.join(self.output_dir,filename)
        # Write the list to a JSON file
        with open(path, 'w') as f:
            json.dump(all_tasks, f)
        print(f"Json file: {filename} is saved under below path\n {path}")

