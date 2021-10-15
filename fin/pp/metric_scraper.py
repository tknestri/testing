from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver
from time import sleep

requests_headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36' }



# FUCK YOU!!!!
# DRIVER = r'C:\Users\483286\Documents\chromedriver_win32\chromedriver.exe'
#
# options = webdriver.ChromeOptions()
# options.add_argument(r'user-data-dir=C:\Users\483286\Documents\'')
# options.add_argument('--no-proxy-server')
# driver = webdriver.Chrome(DRIVER,options =options)
#
# sleep(7)
# driver.get('http://www.python.org')
# sleep(1)
#
# driver.get_screenshot_as_file("screenshot.png")
# driver.quit()
# print("end...")


tick3r = "AAPL"

def strrange(string, b, c):
  out = ""
  while b<c:
    out += string[b]
    b+=1
  return out

def webpgdl(url):
  response = requests.get(url, headers=requests_headers, timeout = 5)
  return response.text

def aaa_yield():
  page = webpgdl("https://fred.stlouisfed.org/series/AAA")
  # print("got page from requests...")
  soup = BeautifulSoup(page, features="lxml")
  # print(soup.text)
  aaa = re.findall("\n\d+.+\d\d+", soup.text)
  return float(aaa[0])

def eps(ticker):
  try:
      page = webpgdl("https://finance.yahoo.com/quote/" + ticker)
  except ConnectionError:
      print("eps:: could not retrive page")
      return

  # print("got page from requests...")
  soup = BeautifulSoup(page, features="lxml")
  value = re.search(r"(?<=EPS\s)(?<=\s).*(?=Ear)", soup.text)
  try:
    return float(strrange(value[0], 5, 9))
  except IndexError:
    print("eps:: failed to parse")
    return

def bvps(ticker):
  try:
    page = webpgdl("https://finance.yahoo.com/quote/" + ticker + "/key-statistics?p=" + ticker)
  except ConnectionError:
    print("eps:: could not retrive page")
    return

  # print("got page from requests...")
  soup = BeautifulSoup(page, features="lxml")
  value = re.search(r"(?<=Book Value Per Share \(mrq\)).*(?=Cash Flow Statement)", soup.text)
  try:
    return float(value[0])
  except IndexError:
    print("eps:: failed to parse")
    return

def expected_growth():
  return

def pe_ratio(ticker):
  try:
    page = webpgdl("https://finance.yahoo.com/quote/" + ticker)
  except ConnectionError:
    print("eps:: could not retrive page")
    return

  print("got page from requests...")
  soup = BeautifulSoup(page, features="lxml")
  value = re.search(r"(?<=EPS\s)(?<=\s).*(?=Ear)", soup.text)
  try:
    return float(strrange(value[0], 5, 9))
  except IndexError:
    print("eps:: failed to parse")
    return


def employees(ticker):
  try:
    page = webpgdl("https://finance.yahoo.com/quote/" + ticker + "/profile?p=" + ticker)
  except ConnectionError:
    print("employees:: could not retrive page")
    return

  # print("got page from requests...")
  soup = BeautifulSoup(page, features="lxml")

  # print(soup.text)

  value = re.search(r"(?<=Full Time Employees:).*(?=Key)", soup.text)
  value = re.sub('\D', '', value[0])
  print(value[0])

  return value

def sector(ticker):
  try:
    page = webpgdl("https://finance.yahoo.com/quote/" + ticker + "/profile?p=" + ticker)
  except ConnectionError:
    print("employees:: could not retrive page")
    return

  # print("got page from requests...")
  soup = BeautifulSoup(page, features="lxml")

  # print(soup.text)

  value = re.search(r"(?<=Sector\(s\):\s).*(?=Indus)", soup.text)
  value1 = re.sub('\D', '', value[0])
  # print(value)
  return value[0]

def industry(ticker):
  try:
    page = webpgdl("https://finance.yahoo.com/quote/" + ticker + "/profile?p=" + ticker)
  except ConnectionError:
    print("employees:: could not retrive page")
    return

  # print("got page from requests...")
  soup = BeautifulSoup(page, features="lxml")

  # print(soup.text)

  value = re.search(r"(?<=Industry\:\s).*(?=Full Time Employees)", soup.text)
  value1 = re.sub('\D', '', value[0])
  # print(value)
  return value[0]

def total_revenue(ticker):
  return
