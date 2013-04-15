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
@param:keyword - vyhladavacia fraza
@return: asociativne_pole
'''
def basicSearch(keyword,Include):
	html_file=""
	html_file = sendUrlCiteSeerX_BASIC(keyword,Include)
	
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
	req = urllib2.Request(http_request)
	response = urllib2.urlopen(req)
	the_page = response.read()	
	
	return the_page


		

html_doc = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


soup = BeautifulSoup(html_doc)

print(soup.prettify())


	
