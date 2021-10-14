# import metric_scraper

import sys
import metric_scraper

# ticker = input("ticker: ")
# menu = """
# OPTIONS:
#     1 Show eps
#     2 Show p/e ratio
#     3 Show mumber of employees
#     4 show all"""
# print(menu)
# selection = input('enter a number: ')
#
# if int(selection) == 1:
#     # print("eps: " + metric_scraper.eps(ticker))
#     x = 2

ticker = "AAPL"
selection = 4
if int(selection) == 4:
    print("eps: ", metric_scraper.eps(ticker))
    print("employees: ", metric_scraper.employees(ticker))
    print("sector: ", metric_scraper.sector(ticker))
    print("industry: ", metric_scraper.industry(ticker))
    print("book value per share: ", metric_scraper.bvps(ticker))
    print("AAA Yield: ", metric_scraper.aaa_yield())