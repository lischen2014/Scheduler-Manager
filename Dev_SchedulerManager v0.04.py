import sys
from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import *
from apscheduler.triggers.date import DateTrigger
from apscheduler.schedulers.qt import QtScheduler
from apscheduler.schedulers.base import * 
from apscheduler.events import * # It must combine with `from apscheduler.schedulers.base import * ` So that all events can be imported
from datetime import datetime, timedelta
from win10toast import ToastNotifier
import logging
import easygui
import json
import os
from time import sleep
from Packages.UI_SchedulerManager import Ui_MainWindow
from Packages.MySchedulerManager import MySchedulerManager
from Packages.UI_Config import Ui_Config
from InitVerintSpider import launch_spider

def get_current_dir():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return current_dir

class Init_UI(QMainWindow, Ui_MainWindow): 

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.currentdir = get_current_dir()
        self.setWindowIcon(QtGui.QIcon(os.path.join(get_current_dir(),'./Icon/Coffee.ico')))

        # Resize the window
        # self.resize(800, 600)

        # Modify Table Column Width
        self.tableWidget.setColumnWidth(0,130) # Title
        self.tableWidget.setColumnWidth(1,160) # Run Time
        self.tableWidget.setColumnWidth(2,85) # State
        self.tableWidget.setColumnWidth(3,240) # ID
        
		# Disable editing
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
		# Set selection with whole row not with cell
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
 
		# Resize Columns and Rows with content
        # self.tableWidget.resizeColumnsToContents()
        # self.tableWidget.resizeRowsToContents()


class MyQtSchedulerManager(MySchedulerManager):

    def __init__(self, tz):
        super().__init__(tz)
        # Overwrite MySchedulerManager's scheduler to Qt scheduler
        self.scheduler = QtScheduler()

class ConfigDialog(QtWidgets.QDialog, Ui_Config):
    def __init__(self, parent=None):
        super(ConfigDialog, self).__init__(parent)
        # self.verint_Passwd_LineEdit.setEchoMode(QtWidgets.QLineEdit.Password) # BUG: not work
        self.setupUi(self)

        # Connect the "OK" and "Cancel" buttons to their respective slots
        self.okButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(self.reject)

    def accept(self):
        # This method is called when the "OK" button is clicked
        print("OK button clicked")
        super(ConfigDialog, self).accept()

    def reject(self):
        # This method is called when the "Cancel" button is clicked
        print("Cancel button clicked")
        super(ConfigDialog, self).reject()

    def load_credential(self):
        # Check if the credential file exists
        default_credential_path = os.path.join(os.path.expanduser('~'), "./SchedulerManager/credential.json")
        if os.path.exists(default_credential_path):
            # Load the credential from the file
            with open(default_credential_path, 'r') as f:
                credential = json.load(f)
            # Set the values of the LineEdits
            self.verint_URL_LineEdit.setText(credential.get('URL', ''))
            self.verint_Account_LineEdit.setText(credential.get('account', ''))
            self.verint_Passwd_LineEdit.setText(credential.get('password', ''))

    def save_credential(self):
        # Get the values from the LineEdits
        url = self.verint_URL_LineEdit.text()
        account = self.verint_Account_LineEdit.text()
        password = self.verint_Passwd_LineEdit.text()
        # Create the credential dictionary
        credential = {'URL': url, 'account': account, 'password': password}
        # Save the credential to the file
        default_credential_path = os.path.join(os.path.expanduser('~'), "./SchedulerManager/credential.json")
        with open(default_credential_path, 'w') as f:
            json.dump(credential, f)

class Main(Init_UI, QObject, MyQtSchedulerManager):
    
    time_format = '%Y-%m-%d %H:%M:%S'

    # Signal
    signal_update_table = pyqtSignal()
    # signal1 = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.sched_manager = MyQtSchedulerManager(tz='Asia/Shanghai') # Set timezone
        # Redirect stdout to current class, then use `def write()` to redirect the output to the QTextBrowser widget.
        # sys.stdout = self
        self.toaster = ToastNotifier()

        # Update Current Time with a timer
        timer = QTimer(self)
        timer.timeout.connect(self.update_current_time)
        timer.start(1000)

        # Init functions
        self.sched_manager.scheduler.add_listener(self.handle_event, EVENT_ALL)
        self.sched_manager.scheduler.add_listener(self.event_scheduler_started, EVENT_SCHEDULER_STARTED | EVENT_SCHEDULER_RESUMED)
        self.sched_manager.scheduler.add_listener(self.event_scheduler_paused, EVENT_SCHEDULER_PAUSED)
        self.sched_manager.scheduler_start()
        
        # Logging
        log_folder_path = os.path.join(get_current_dir(), "log")
        if not os.path.exists(log_folder_path):
            os.makedirs(log_folder_path)
        log_file_path = os.path.join(log_folder_path, "log.txt")

        logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename = log_file_path,
                    filemode='a')
        self.sched_manager.scheduler._logger = logging

        # Signal & Slots
        ## Menu Actions
        self.actionNew_File.triggered.connect(lambda:print("You clicked New File Button"))
        self.actionSave_File.triggered.connect(lambda:print("You clicked Save File Button")) 
        self.actionCopy.triggered.connect(lambda:print("You clicked Copy Button")) 
        self.actionPaste.triggered.connect(lambda:print("You clicked Paste Button")) 
        self.actionImport_Json.triggered.connect(lambda:(self.import_json()))
        self.actionConfig_Spider.triggered.connect(lambda:(self.verint_config()))
        self.actionrunVerintSpider.triggered.connect(lambda:(self.run_verint_spider()))

        ## Buttons
        self.addJobButton.clicked.connect(lambda:(self.add_job(),print("You clicked Add Job Button")))
        self.editJobButton.clicked.connect(lambda:(self.edit_job(),print("You clicked Edit Job Button")))
        self.removeJobButton.clicked.connect(lambda:(self.remove_job(),print("You clicked Remove Job Button")))
        self.clearJobButton.clicked.connect(lambda:(self.sched_manager.clear_jobs(),print("You clicked add test data Button")))

        ## Scheduler Options
        self.pauseSchedulerButton.clicked.connect(lambda:(self.sched_manager.scheduler_pause()))
        self.resumeSchedulerButton.clicked.connect(lambda:(self.sched_manager.scheduler_resume()))

        ## Job Table
        # self.signal1.connect(self.signalCall1) 
        self.signal_update_table.connect(self.update_table_call) 

        ## Dev Options
        self.action_RefreshSchedulerState.triggered.connect(lambda:print("You clicked action_RefreshSchedulerState Button"))
        self.action_AddTestData2Table.triggered.connect(lambda:(self.add_test_data(),print("You clicked add test data Button")))
        self.action_RemoveTestData.triggered.connect(lambda:print("You clicked Remove Job Button")) 
        self.action_Func1.triggered.connect(lambda:(self.test(),print("You clicked test Button"))) 
        self.action_Func2.triggered.connect(lambda:(self.test2(),print("You clicked test Button_2")))
        self.action_Func3.triggered.connect(lambda:(self.test3(),print("You clicked test Button_3")))


    # Functions
    def write(self, text):  # Overwrite the default write() method to append text to the QTextBrowser.
        self.outputBox.moveCursor(self.outputBox.textCursor().End)
        self.outputBox.insertPlainText(text)

    def get_selection(self):
        selected_rows = win.tableWidget.selectionModel().selectedRows()
        if selected_rows:
            selected_jobs = []
            for row in selected_rows:
                id_value = win.tableWidget.item(row.row(), 3).text()
                job = self.sched_manager.get_job(id_value)
                selected_jobs.append(job)
            return selected_jobs
        else:
            print("No job selected")
            return
    
    def verint_config(self):
        ## GUI part
        # Create a new instance of the ConfigDialog
        config_dialog = ConfigDialog()

        # Show the dialog and wait for it to close
        result = config_dialog.exec_()

        # Check the result of the dialog
        if result == QtWidgets.QDialog.Accepted:
            print("OK button clicked")
        else:
            print("Cancel button clicked")


    def update_table_call(self):
        # print("Refreshing Table")
        all_jobs = self.sched_manager.get_all_jobs()

        if all_jobs:
            try:
                win.tableWidget.setRowCount(len(all_jobs))
            except:
                pass
            i = 0
            for job in all_jobs: # by default it is sorted by next run time
                # update table
                newItem = QTableWidgetItem(job["ID"]) 
                win.tableWidget.setItem(i, 3, newItem)

                newItem = QTableWidgetItem(job["Name"])  
                win.tableWidget.setItem(i, 0, newItem)

                newItem = QTableWidgetItem(job["Next_Run_Time"].strftime(self.time_format))  
                win.tableWidget.setItem(i, 1, newItem)

                newItem = QTableWidgetItem(job["State"])  
                win.tableWidget.setItem(i, 2, newItem)

                i += 1
            # win.tableWidget.sortItems(0, order=Qt.AscendingOrder) # BUG: messed table showing when sort with custom filter???
        else:
            # Clear all cells
            print("No scheduled jobs")
            rowCount = win.tableWidget.rowCount()
            colCount = win.tableWidget.columnCount()
            for row in range(rowCount):
                for col in range(colCount):
                    win.tableWidget.setItem(row, col, QTableWidgetItem(""))
            win.tableWidget.setRowCount(0) # Use this to delete the first empty row with empty cells

    # Update Time
    def get_current_time(self):
        tmp_time = datetime.now()
        current_time = datetime.strftime(tmp_time,self.time_format)
        return current_time
        
    def update_current_time(self):
        update_time = self.get_current_time()
        self.currentTime.setText(update_time)


    # Event Handler
    def handle_event(self,event):
        # self.signal1.emit()

        timestamp = self.get_current_time()
        event_job = False
        msg_job_id = False

        if event.code == 1:
            event_msg = "Scheduler started"
        elif event.code == 2:
            event_msg = "Scheduler shutdown"
        elif event.code == 4:
            event_msg = "Scheduler paused"
        elif event.code == 8:
            event_msg = "Scheduler resumed"
        elif event.code == 16:
            event_msg = "Executor initiated"
        elif event.code == 32:
            event_msg = "Removed all jobs from scheduler"
        elif event.code == 64:
            event_msg = "Jobstore added"
        elif event.code == 128:
            event_msg = "Jobstore removed"
        elif event.code == 256:
            event_msg = "Removed all jobs"
        elif event.code == 512:
            event_msg = "Job added"
            event_job = True
        elif event.code == 1024:
            event_msg = "Job removed"
            event_job = True
        elif event.code == 2048:
            event_msg = "Job modified"
            event_job = True
        elif event.code == 4096 :
            event_msg = 'Job executed successful'
            event_job = True
        elif event.code == 8192:
            event_msg = "Job exucuted failed"
            event_job = True
        elif event.code == 16384:
            event_msg = "Job missed"
            event_job = True
        elif event.code == 32768:
            event_msg = "Job submitted"
            event_job = True
        elif event.code == 65536:
            event_msg = "Job reached max instances"
        else:
            event_msg = 'Unknown Error occured'

        self.signal_update_table.emit()

        # print(event.__dict__)
        if event_job == True:
            try:
                msg_job_id = event.job_id
            except:
                pass
        if msg_job_id:
            print(f"{timestamp} : {msg_job_id} - {event_msg}")
        else:
            print(f"{timestamp} : {event_msg}")
    

    # Executor
    def job_triggered(self, *args):
        self.toaster.show_toast("Scheduler Manager", args[1], duration=5, threaded=True)
        easygui.msgbox(f"It's time:{args[0]} to do {args[1]}")
        

    # Scheduler
    def event_scheduler_paused(self,event):
        state = self.sched_manager.scheduler_get_state()
        self.schedState.setText(state)

    def event_scheduler_started(self,event):
        state = self.sched_manager.scheduler_get_state()
        self.schedState.setText(state)


    # Import Function
    def run_verint_spider(self):
        maincwd = get_current_dir()
        # print("Verint Spider START") # BUG: why this msg print after selenium ran complete not before? tried use \n as end, not work. try use flush, AttributeError: 'Main' object has no attribute 'flush'
        launch_spider(maincwd)
        # print("Verint Spider End")

    def import_json(self):
        default_file_path = os.path.join(get_current_dir(), "./Jobs/JobsNeedImport.json")

        if os.path.exists(default_file_path):
            file_name = default_file_path
        else:
            # Prompt the user to select a file
            file_name, _ = QFileDialog.getOpenFileName(self, 'Import Jobs', '', 'JSON Files (*.json)')
            if not file_name:
                return
            
        # Load the jobs from the file
        with open(file_name, 'r') as f:
            jobs = json.load(f)

        # Add the jobs to the scheduler
        for job in jobs:
            format_refer = len(job["starttime"])
            if format_refer != 16 and format_refer !=19:
                print("Warning: Unrecognized time format. Please check, it only accept below format:'2023-04-25 21:00' or '2023-04-25 21:00:00' ")
                return
            elif format_refer ==16:
                format_string = '%Y-%m-%d %H:%M'
            elif format_refer == 19:
                format_string = self.time_format
            run_date = datetime.strptime(job['starttime'], format_string)
            trigger = DateTrigger(run_date=run_date)
            job_title = job["task"]

            self.sched_manager.scheduler.add_job(self.job_triggered, args=[run_date,job_title], trigger=trigger, name=job_title)


    # Job Function
    def add_job(self):
        # Get the job details from the user
        job_title, ok = QInputDialog.getText(self, 'Add Job', 'Enter the job title:')
        if not ok:
            return

        # Get the start time
        run_date = datetime.strftime((datetime.strptime(self.get_current_time(), self.time_format) + timedelta(seconds=15)),self.time_format) # get_current_time() returned a str, so we need convert it to datetime and then add time delta, finally convert it back to str to display in the dialog box
        run_date, ok = QInputDialog.getText(self, 'Add Job', 'Enter the job start time (YYYY-MM-DD HH:MM:SS):', text=run_date)
        if not ok:
            return

        # Add the job to the scheduler
        trigger = DateTrigger(run_date=run_date)
        self.sched_manager.scheduler.add_job(self.job_triggered, args=[run_date,job_title], trigger=trigger, name=job_title)
        
    def edit_job(self):
        # Get the selected job from the job list
        selected_jobs = self.get_selection()
        if selected_jobs:
            for job in selected_jobs:
                    # Get the new job details from the user
                    job_title, ok = QInputDialog.getText(self, 'Edit Job', 'Enter the new job title:', text=job["Name"])
                    if not ok:
                        return

                    run_date, ok = QInputDialog.getText(self, 'Edit Job', 'Enter the new job start time (YYYY-MM-DD HH:MM:SS):', text = job["Next_Run_Time"].strftime(self.time_format))
                    if not ok:
                        return

                    # Update the job in the scheduler
                    run_date_datetime = datetime.strptime(run_date,self.time_format) # format str back to datetime type
                    trigger = DateTrigger(run_date=run_date_datetime)
                    self.sched_manager.scheduler.reschedule_job(job["ID"], trigger=trigger, args=[run_date,job_title], name=job_title)
                        # BUG:seems reschedule cannot modify param, maybe we need modify first, then reschedule in the second
        else:
            print("Please select 1 job at a time to proceed")

    def remove_job(self):
        selected_jobs = self.get_selection()
        if selected_jobs:
            for job in selected_jobs:
                self.sched_manager.remove_job(job["ID"])

    # def signalCall1( self ):
    #     pass

##################
    # Simulate normal job
    def job_test1(self,x):
        print(f"For loop job, param: {x}")

    # Simulate failed job
    def job_test2(self,x):
        print(f"For failed loop job, param: {x}")
        a = 1 / 0

    def test(self):
        self.sched_manager.scheduler.add_job(func=self.job_test1, args=('job_test1, Loop Job1',), trigger='interval', seconds=4, name = "Loop Job 1")
        self.sched_manager.scheduler.add_job(func=self.job_test2, args=('job_test2, Loop Job2 Failed',), trigger='interval', seconds=6, name="Loop Job 2 Failed")
        self.sched_manager.scheduler.add_job(func=self.job_test1, args=('job_test3, Loop Job3',), trigger='interval', seconds=3, name = "Loop Job 3")
        self.sched_manager.scheduler.add_job(func=self.job_test1, args=('job_test4, Loop Job4',), trigger='interval', seconds=3, name = "Loop Job 4")
    
    def test2(self):
        print("test 2 triggered")
        self.signal_update_table.emit()

    def test3(self):
        print("test 3 triggered")
        jobs = self.get_selection()
        for job in jobs:
            print("======== START ========")
            print(job["ID"])
            print(job["Name"])
            print(job["Next_Run_Time"])
            print("======== END ========")

##################

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Main()
    win.show()
    sys.exit(app.exec_())
