from Packages.VerintSpider import VerintSpider
import os

def launch_spider(maincwd):
    verint_account = "user1"
    verint_password = "Password01" 
    verint_url = "https://verinturl.com/"
    output_path = os.path.join(maincwd, "Jobs")
    json_name = "JobsNeedImport.json"
    hide = False
    disable_auto_close = True # False: It will auto close. True: it will not auto close

    spider = VerintSpider(account=verint_account, password=verint_password, URL=verint_url,do_output_screenshot=True, hide = hide, disable_auto_close = disable_auto_close, output_dir=output_path, json_name=json_name)
    spider.runSpider() 

if __name__ == "__main__":
    pass