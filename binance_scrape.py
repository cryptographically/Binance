from BeautifulSoup import BeautifulSoup
from mechanize import Browser
import re
import time
import win32com.client

br=Browser()
response=br.open("https://support.binance.com/hc/en-us/sections/115000106672-New-Listings")

soup = BeautifulSoup(response)
page = soup.find('ul')
listing = page.findAll('a')
comparison_list = []

for i in listing:
	comparison_list.append(i)

while True:
	listings_list = []
	for entry in listing:
		listings_list.append(entry)
	for i in range(1):
		if listings_list[i] != comparison_list[i]:
			olMailItem = 0x0
			obj = win32com.client.Dispatch("Outlook .Application")
			newMail = obj.CreateItem(olMailItem)
			newMail.Subject = "Crypto Riches"
			newMail.Body = str(listings_list[i])
			newMail.To = ##enter recipients here
			newMail.Send()
	time.sleep(60)

