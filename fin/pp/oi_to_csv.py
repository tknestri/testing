# Importing the required modules
import os
import sys
import pandas as pd
from bs4 import BeautifulSoup
import metric_scraper


ticker = 'AAPL'

# empty list
data = []

# for getting the header from
# the HTML file
dirty_list_header = []
soup = BeautifulSoup(metric_scraper.webpgdl("http://openinsider.com/search?q="+ticker),'html.parser')
header = soup.find_all("table")[11].find("tr")

for items in header:
	try:
		dirty_list_header.append(items.get_text())
	except:
		continue

list_header = []

for item in dirty_list_header:
    if(item == "\n"):
        pass
    else:
        list_header.append(item)



# for getting the data
HTML_data = soup.find_all("table")[-3].find_all("tr")[1:]
# print(HTML_data)
# quit()

for element in HTML_data:
	sub_data = []
	for sub_element in element:
		try:
			sub_data.append(sub_element.get_text())
		except:
			continue
	data.append(sub_data)

# Storing the data into Pandas
# DataFrame
dataFrame = pd.DataFrame(data = data, columns = list_header)

# Converting Pandas DataFrame
# into CSV file
dataFrame.to_csv('Geeks.csv')
