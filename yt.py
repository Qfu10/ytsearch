import os
import sys
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

if sys.argv[1] == "-h":
    print("\nWelcome to Yotube search crawler\nValid commands are-\n") 
    print("1)<yt.py xyz> or <yt xyz> opens the first result when searching \"xyz\" on Youtube\n")
    print("2)<yt.py -n t xyz> or <yt -n t xyz> opens the t-th result when searching \"xyz\" on Youtube\n")
    print("3)<yt.py -h> or <yt -h> for the help page")
else:
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    counter = 1
    search = sys.argv[-1]
    if sys.argv[1] == "-n":
        counter = sys.argv[2]


    def scrape(query, num):
        url = "https://www.youtube.com/results?search_query=" + query
        driver.get(url)
        xpath="/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[" + str(num) + "]/div[1]/div/div[1]/div/h3/a"
        return driver.find_element_by_id("meta").find_element_by_xpath(xpath).get_attribute('href')

    os.system("start \"\" " + scrape(search, counter))