from splinter import Browser
import pandas as pd

url = "https://www.google.com"

browser = Browser('chrome')  # open a chrome browser
browser.visit(url)  # goes to the url

search_bar_xpath = '//*[@id="lst-ib"]'
search_bar = browser.find_by_xpath(search_bar_xpath)[0]  # find_by_xpath returns a list, so index 0
search_bar.fill("CodingStartups.com")  # simulate typing


search_button_xpath = '//*[@id="tsf"]/div[2]/div[3]/center/input[1]'
search_button = browser.find_by_xpath(search_button_xpath)[0]
search_button.click()  # simulate clicking


search_results_xpath = '//h3[@class="r"]/a'
search_results = browser.find_by_xpath(search_results_xpath)  # returns list of link elements

# iterate through list of link elements
scraped_data = []
for search_result in search_results:

	title = search_result.text.encode('utf8')  # trust me, clean data
	link = search_result["href"]
	scraped_data.append((title, link))

# put all the data into a pandas dataframe
df = pd.DataFrame(data=scraped_data, columns=["title", "link"])
df.to_csv("links.csv")	# export to csv