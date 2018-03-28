from  selenium import webdriver
from multiprocessing import Pool
import time
from xlrd import open_workbook
from xlutils.copy import copy
import re



def get_from_excel():
    path = r'C:\Users\战神皮皮迪\Documents\GitHub\Spider\from_to_spider\location and distance.xls'
    rb = open_workbook(path)
    sheet_name = rb.sheet_names()[0]
    sheet_1 = rb.sheet_by_name(sheet_name)
    rows = sheet_1.nrows
    fromlist = sheet_1.row_values(0)
    pool = Pool(processes=8)
    for i in range(1, rows):
        tocity = sheet_1.row_values(i)[1]
        for j in fromlist:
            pool.apply_async(get_content, ( j, tocity,))
    pool.close()
    pool.join()
def get_content(from_city,tocity):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs",prefs)
        driver = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
        # driver.set_page_load_timeout(5)
        driver.get('http://www.distancebetweencities.us/result.php?fromplace={}&toplace={}'.format(from_city,tocity))
        time.sleep(10)
        distance=re.findall('id="drvDistance">(.*?)</span>',driver.page_source)
        print(distance)
        driver.quit()








    # driver.quit()
if __name__ == '__main__':

    get_from_excel()
#     pool = Pool(processes=8)
#     for i in range(10):
#         pool.apply_async(get_content, (i,))
#     pool.close()
#     pool.join()
# i=1
# get_content(i)



