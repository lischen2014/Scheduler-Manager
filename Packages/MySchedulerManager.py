from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
# import json
import easygui
import sys

# Modified 20230516 21:19
# # Modified 20230520 16:25, changed `task` to `job` in bulk add and remove func.

class MySchedulerManager:

    def __init__(self,tz) -> None:
        self.tz = tz
        self.scheduler = BackgroundScheduler(timezone=tz)

    ############################### Scheduler ###############################
    def scheduler_get_state(self):
        if self.scheduler.state == 0:
            result = "Not Running"
        elif self.scheduler.state == 1:
            result = "Running"
        elif self.scheduler.state == 2:
            result = "Paused"
        else:
            result = (f"Unrecognized scheduler state: {self.scheduler.state}")
        return result


    def scheduler_start(self):
        try:
            self.scheduler.start()
        except Exception as e:
            print(f'An error occurred: {e}')

    def scheduler_resume(self):
        try:
            self.scheduler.resume()
        except Exception as e:
            print(f'An error occurred: {e}')

    def scheduler_pause(self):
        try:
            self.scheduler.pause()
        except Exception as e:
            print(f'An error occurred: {e}')

    def scheduler_shutdown(self):
        try:
            self.scheduler.shutdown()
        except Exception as e:
            print(f'An error occurred: {e}')


    ############################### Get Job ###############################
    def get_all_jobs(self):
        jobs = self.scheduler.get_jobs() 
        job_list_status = []
        if jobs:
            for job in jobs:
                # jobs_status += self.get_job(job.id)
                job_status = self.get_job(job.id)
                # print(job_status)
                job_list_status.append(job_status)
                # print(job_list_status)
        else:
            job_list_status = None
        return job_list_status

    def get_job(self,job_id):
        try:
            job_id = str(job_id)
            job = self.scheduler.get_job(job_id)
            job_status = {}
            if job:
                job_status["ID"] = job.id
                job_status["Name"] = job.name
                job_status["Trigger"] = job.trigger
                try:
                    if job.next_run_time:
                        job_status["State"] = "Running"
                        job_status["Next_Run_Time"] = job.next_run_time
                    else:
                        job_status["State"] = "Paused"
                        job_status["Next_Run_Time"] = None
                except:
                    pass
                # job_status["Action"] = job.func
                job_status["Arguments"] = job.args

                return job_status
            else:
                print(f"Message: Job ID: {job_id} does not exist.")
        except ValueError:
            print('Warning: Job ID is not recognized')

    ############################### Add Job ###############################
    def add_job(self,job_dict):
            format_refer = len(job_dict["starttime"])
            if format_refer != 16 and format_refer !=19:
                print("Warning: Unrecognized time format. Please check, it only accept below format:'2023-04-25 21:00' or '2023-04-25 21:00:00' ")
                return
            elif format_refer ==16:
                time_format = '%Y-%m-%d %H:%M'
            elif format_refer == 19:
                time_format = '%Y-%m-%d %H:%M:%S'
            job_starttime = datetime.strptime(job_dict["starttime"],time_format)
            job_id = str(len(self.scheduler.get_jobs()) + 1) # So that id is the index of the whole id list, and id parameter only accept string.
            job_msg = job_dict["task"]
            self.scheduler.add_job(self.test_prompt,trigger='date', run_date = job_starttime, id = job_id, name = job_id, args=[job_msg])
            print(f"Added {job_dict} into job list.")

    def add_job_bulk(self,job_list):
        for single_job in job_list:
            self.add_job(single_job)

    def remove_job(self,job_id):
        try:
            job_id = str(job_id)
            self.scheduler.remove_job(job_id,jobstore=None)
        except ValueError:
            print('Warning: Job ID is not recognized')
        
    # Pause Job
    def pause_job(self,job_id):
        try:
            job_id = str(job_id)
            self.scheduler.pause_job(job_id,jobstore=None)
        except ValueError:
            print('Warning: Job ID is not recognized')
    # Resume Job
    def resume_job(self,job_id): # 即使job resume了，只要scheduler不是running的，依旧不会生效
        try:
            job_id = str(job_id)
            self.scheduler.resume_job(job_id,jobstore=None)
        except ValueError:
            print('Warning: Job ID is not recognized')

    # Clear Job
    def clear_jobs(self):
        self.scheduler.remove_all_jobs(jobstore=None)
        self.get_all_jobs()

    # Prompt
    def test_prompt(self,message):
        easygui.msgbox(f"It's time to do {message}")