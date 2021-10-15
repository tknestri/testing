import sys, os
sys.path.append(os.path.abspath("/home/tyler/Documents/openanal/fin/pp/"))
import oi_to_csv

ticker = "aapl"
def get_tbl(ticker):
    print(oi_to_csv.toCsv(ticker))
get_tbl(ticker)