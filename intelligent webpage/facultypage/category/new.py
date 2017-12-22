# import libraries
import requests
from bs4 import BeautifulSoup
def fetch(x,y):
	# specify the url
	# quote_page = "http://www.iitg.ernet.in/cse/csejournalpublications"
	# page = urllib2.urlopen(quote_page)
	page = requests.get("http://www.iitg.ernet.in/cse/csejournalpublications")
	# parse the html using beautiful soap and store in variable `soup`
	#soup = BeautifulSoup(page, 'html.parser')
	soup = BeautifulSoup(page.content, 'html.parser')
	# Take out the <div> of name and get its value
	name_box = soup.find_all('td', attrs={'class': 'column-2'})
	lis=list()
	for name in name_box:
		nae = name.get_text() # strip() is used to remove starting and trailing
		if x not in nae and y not in nae :
			continue
		else :
			lis.extend([nae])
	return lis


def name1(x):
	if " " not in x:
		return x
	y=x.split(" ",1)
	k=y[0][0:1]
	z=k+" "+y[1]
	return z

