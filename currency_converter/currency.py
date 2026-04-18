import sys
import urllib2
from bs4 import BeautifulSoup


fromCUR = raw_input("From: ")
to = raw_input("To: ")

amount = raw_input("Amount: ")

#currency_site = "http://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=INR"
currency_site = "http://www.xe.com/currencyconverter/convert/?Amount=1&From=" + fromCUR + "&To=" + to

page = urllib2.urlopen(currency_site)
soup = BeautifulSoup(page, "lxml")

#print soup.find('span', class_ = 'uccResultAmount').string
value = soup.find('span', class_ = 'uccResultAmount').string

print("1 " + fromCUR + " = " + value + " " + to)
print float(value) * float(amount)