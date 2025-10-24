from core.pull import DataPuller

dp = DataPuller()
dp.goto_url("https://discord.com/") # tests
elm = dp.find_elm_by_PARTEXT("Download")
print(elm) # debug
dp.click_elm(elm) # debug
dp.download_file(dp.find_elm_by_PARTEXT("Download for")) # debug
dp.wait_for_download() # debug
dp.close() # debug