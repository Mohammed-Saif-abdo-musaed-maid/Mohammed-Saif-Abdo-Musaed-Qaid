import requests
from bs4 import BeautifulSoup
import csv
date = input("please enter the date in the fallowing format MM/DD/YYYY:")
page  = requests.get(f"https://www.yallakora.com/match-center/?data={date}")
def main(page):
    src=page.content 
    print(src)
    main(page)