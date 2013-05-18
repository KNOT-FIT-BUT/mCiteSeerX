#!/usr/bin/python

'''
API Modul pre sluzbu CiteSeerX
Implementuje zakladne vyhladavanie pomocou tejto sluzby
Modul obsahuje 2 vyhladavacie funkcie: basicSearch a extendedSearch
'''

from bs4 import BeautifulSoup
import sys
import urllib2

'''
Funkcia, ktora splna zakladne vyhladavanie pomocou sluzby CiteSeerX
@param:keyword - vyhladavacia fraz(retazec),Include - Bool. hodnota
@return: asociativne_pole
'''
def basicSearch(keyword,Include):
	result_dic=dict()
	author_parse=""
	title_parse=""
	date_parse=""
	vol_parse=""
	issn_parse=""
	abstract_url_parse=""
	pdf_url_parse=""
	language_parse=""
	keywords_parse=""
	isbn_parse=""
	insert_key=0
	html_file=""
	html_file = sendUrlCiteSeerX_BASIC(keyword,Include)
	soup = BeautifulSoup(html_file.read())
	

	




# Copy all of the content from the provided web page
webpage = urlopen('http://feeds.huffingtonpost.com/huffingtonpost/LatestNews').read()
 
# Grab everything that lies between the title tags using a REGEX
patFinderTitle = re.compile('')
 
# Grab the link to the original article using a REGEX
patFinderLink = re.compile('<link rel.*href="(.*)">')
 
# Store all of the titles and links found in 2 lists
findPatTitle = re.findall(patFinderTitle,webpage)
findPatLink = re.findall(patFinderLink,webpage)
 
# Create an iterator that will cycle through the first 16 articles and skip a few
listIterator = []
listIterator[:] = range(2,16)
 
soup2 = BeautifulSoup(webpage)
#print soup2.findAll("title")
titleSoup = soup2.findAll("title")
linkSoup = soup2.findAll("link")
for i in listIterator:
    print titleSoup[i]
    print linkSoup[i]
    print "\n"
    # Copy all of the content from the provided web page
webpage = urlopen('http://feeds.huffingtonpost.com/huffingtonpost/LatestNews').read()
 
# Grab everything that lies between the title tags using a REGEX
patFinderTitle = re.compile('')
 
# Grab the link to the original article using a REGEX
patFinderLink = re.compile('<link rel.*href="(.*)">')
 
# Store all of the titles and links found in 2 lists
findPatTitle = re.findall(patFinderTitle,webpage)
findPatLink = re.findall(patFinderLink,webpage)
 
# Create an iterator that will cycle through the first 16 articles and skip a few
listIterator = []
listIterator[:] = range(2,16)
 
soup2 = BeautifulSoup(webpage)
#print soup2.findAll("title")
titleSoup = soup2.findAll("title")
linkSoup = soup2.findAll("link")
for i in listIterator:
    print titleSoup[i]
    print linkSoup[i]
    print "\n"
    # Copy all of the content from the provided web page
webpage = urlopen('http://feeds.huffingtonpost.com/huffingtonpost/LatestNews').read()
 
# Grab everything that lies between the title tags using a REGEX
patFinderTitle = re.compile('')
 
# Grab the link to the original article using a REGEX
patFinderLink = re.compile('<link rel.*href="(.*)">')
 
# Store all of the titles and links found in 2 lists
findPatTitle = re.findall(patFinderTitle,webpage)
findPatLink = re.findall(patFinderLink,webpage)
 
# Create an iterator that will cycle through the first 16 articles and skip a few
listIterator = []
listIterator[:] = range(2,16)
 
soup2 = BeautifulSoup(webpage)
#print soup2.findAll("title")
titleSoup = soup2.findAll("title")
linkSoup = soup2.findAll("link")
for i in listIterator:
    print titleSoup[i]
    print linkSoup[i]
    print "\n"
    # Copy all of the content from the provided web page
webpage = urlopen('http://feeds.huffingtonpost.com/huffingtonpost/LatestNews').read()
 
# Grab everything that lies between the title tags using a REGEX
patFinderTitle = re.compile('')
 
# Grab the link to the original article using a REGEX
patFinderLink = re.compile('<link rel.*href="(.*)">')
 
# Store all of the titles and links found in 2 lists
findPatTitle = re.findall(patFinderTitle,webpage)
findPatLink = re.findall(patFinderLink,webpage)
 
# Create an iterator that will cycle through the first 16 articles and skip a few
listIterator = []
listIterator[:] = range(2,16)
 
soup2 = BeautifulSoup(webpage)
#print soup2.findAll("title")
titleSoup = soup2.findAll("title")
linkSoup = soup2.findAll("link")
for i in listIterator:
    print titleSoup[i]
    print linkSoup[i]
    print "\n"
    # Copy all of the content from the provided web page
webpage = urlopen('http://feeds.huffingtonpost.com/huffingtonpost/LatestNews').read()
 
# Grab everything that lies between the title tags using a REGEX
patFinderTitle = re.compile('')
 
# Grab the link to the original article using a REGEX
patFinderLink = re.compile('<link rel.*href="(.*)">')
 
# Store all of the titles and links found in 2 lists
findPatTitle = re.findall(patFinderTitle,webpage)
findPatLink = re.findall(patFinderLink,webpage)
 
# Create an iterator that will cycle through the first 16 articles and skip a few
listIterator = []
listIterator[:] = range(2,16)
 
soup2 = BeautifulSoup(webpage)
#print soup2.findAll("title")
titleSoup = soup2.findAll("title")
linkSoup = soup2.findAll("link")
for i in listIterator:
    print titleSoup[i]
    print linkSoup[i]
    print "\n"



authordiv = soup.find('meta',attrs={'name':'citation_title'})




authordiv = soup.find('meta',attrs={'name':'citation_title'})
	
	return result_dic
	

'''
Funkcia, ktora splna zakladne vyhladavanie pomocou sluzby CiteSeerX
@return:asociativne_pole
@return: asociativne_pole
'''	
def extendedSearch(Text,Title,AutorAffi,PublicVenue,Keywords,Abstract,Year,
YearArg,MinCitations,Citations,SortBy):
	text_arg=0
	title_arg=0
	autorAffi_arg=0
	publicvenue_arg=0
	keywords_arg=0
	abstract_arg=0
	year_arg=0
	mincitations_arg=0
	citations_arg=0
	sortbyt_arg=0
	if (Text !=0):
		text_arg=1
	elif(Title!=0):
		title_arg=1
	elif (AutorAffi !=0):
		autoraffi_arg=1
	elif (PublicVenue != 0):
		publicvenue_arg=1
	elif (keywords!=0):
		keywords_arg=1
	elif (Abstract !=0):
		abstract_arg=1
	elif (Year!=0):
		year_arg=1
	elif (MinCitations != 0):
		mincitations_arg=1
	elif (SortBy !=0):
		sortby_arg=1
	
def sendUrlCiteSeerX_EXTENDED(keywordsPhrase,Citation,Sort):
	http_req=""


'''
Funkcia pre poslanie ziadosti o URL
Tato funkcia je pouzivana zakladnou funkciou pre vyhladavanie
'''
def sendUrlCiteSeerX_BASIC(keywordsPhrase,Citation,Sort):
	http_req=""
	response=""
	sort_list_no_cit=['&t=doc','&t=doc&sort=cite','&t=doc&sort=dates','&t=doc&sort=ascdate','&t=doc&sort=recent']
	sort_list_cit=['&ic=1&sort=rlv&t=doc','&ic=1&sort=cite&t=doc','&ic=1&t=doc&sort=date','&t=doc&sort=ascdate','&ic=1&t=doc&sort=recent']
	if (Citation == 0):
		http_req= "http://citeseerx.ist.psu.edu/search?q="+keywordsPhrase+"&submit=Search"+sort_list_no_cit[Sort]
	else:
		http_req= "http://citeseerx.ist.psu.edu/search?q="+keywordsPhrase+"&submit=Search"+sort_list_cit[Sort]	
	req=""
	the_page=""
		page=urllib2.urlopen(http_request)

	
	
	
	return page


		

        

