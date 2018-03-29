import requests
import urllib2
import xlsxwriter

from bs4 import BeautifulSoup

# Get the values after parsing from webpage
quote_page = "http://www.bloomberg.com/quote/SPX:IND"

page= urllib2.urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')

name = soup.find('h1', attrs={'class': 'name'})
name = name.text.strip()

price = soup.find('div', attrs={'class': 'price'})
price = price.text.strip()

# Write the values to Excel File
workbook = xlsxwriter.Workbook('stock_index.xlsx')
worksheet = workbook.add_worksheet()

# Set width of Name Column
worksheet.set_column('A:A', 50)

# Define bold format
bold = workbook.add_format({'bold': True})

worksheet.write(0, 0, 'Index Name', bold)
worksheet.write(0, 1, 'Value', bold)

worksheet.write(1, 0, name)
worksheet.write(1, 1, price)

workbook.close()
