#!/usr/bin/python

'''
API Modul pre sluzbu CiteSeerX
Implementuje zakladne vyhladavanie pomocou tejto sluzby
Modul obsahuje 2 vyhladavacie funkcie: basicSearch a extendedSearch
'''

from bs4 import BeautifulSoup
import sys
import urllib2

import time
'''
Funkcia, ktora splna zakladne vyhladavanie pomocou sluzby CiteSeerX
@param:keyword - vyhladavacia fraz(retazec),Include - Bool. hodnota
@return: asociativne_pole
'''
def basicSearch(keyword,Include):
	result_dic=dict()
	dic_index=0
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
	base_url=""
	html_file=""
	pager=""
	authors=""
	page=""
	page= sendUrlCiteSeerX_BASIC(keyword,Include,0)
	zoznam=[]
	html_file=urllib2.urlopen(page)
	#time.sleep(15)
	soup=""
	soup=BeautifulSoup(html_file)
	
	

	while (True):
		pom_list=[]
		author_list=[]
		pom_string=""
		authors= soup.findAll('span', attrs={'class' : 'authors'})
		for i in range(0,len(authors)):
			pom_list.append(authors[i].contents)
		
			for p in range(0,len(pom_list[i])):
				pom_string=pom_string + pom_list[i][p]
		
			pom_string=pom_string.replace("\n","")
		
			pom_string=pom_string.replace("\t","")
			
			zoznam.append(pom_string)
			pom_string=""
		result_dic[dic_index].append(zoznam)
	
		pom_list=[]
		author_list=[]
		pom_string=""
		authors= soup.findAll('span', attrs={'class' : 'pubvenue'})
		for i in range(0,len(authors)):
			pom_list.append(authors[i].contents)
		
			for p in range(0,len(pom_list[i])):
				pom_string=pom_string + pom_list[i][p]
		
			pom_string=pom_string.replace("\n","")
		
			pom_string=pom_string.replace("\t","")
			zoznam.append(pom_string)
			pom_string=""
		result_dic[dic_index].append(zoznam)
		
		pom_list=[]
		author_list=[]
		pom_string=""
		authors= soup.findAll('span', attrs={'class' : 'pubyear'})
		for i in range(0,len(authors)):
			pom_list.append(authors[i].contents)
		
			for p in range(0,len(pom_list[i])):
				pom_string=pom_string + pom_list[i][p]
		
			pom_string=pom_string.replace("\n","")
		
			pom_string=pom_string.replace("\t","")
			zoznam.append(pom_string)
			pom_string=""
		result_dic[dic_index].append(zoznam)
			
	
		pom_list=[]
		author_list=[]
		pom_string=""
		authors= soup.findAll('span', attrs={'class' : 'snippet'})
		for i in range(0,len(authors)):
			pom_list.append(authors[i].contents)
		
			for p in range(0,len(pom_list[i])):
				pom_string=pom_string + pom_list[i][p]
		
			pom_string=pom_string.replace("\n","")
		
			pom_string=pom_string.replace("\t","")
			zoznam.append(pom_string)
			pom_string=""
		result_dic[dic_index].append(zoznam)
	
		pom_list=[]
		author_list=[]
		pom_string=""
		
		zoznam=[]
		authors= soup.findAll('span', attrs={'class' : 'citations'})
		for i in range(0,len(authors)):
			pom_list.append(authors[i].contents)
		
			for p in range(0,len(pom_list[i])):
				pom_string=pom_string + pom_list[i][p]
		
			pom_string=pom_string.replace("\n","")
		
			pom_string=pom_string.replace("\t","")
			zoznam.append(pom_string)
			pom_string=""
		result_dic[dic_index].append(zoznam)
		
		
		pom_list=[]
		author_list=[]
		pom_string=""
		authors= soup.findAll('span', attrs={'class' : 'pubabstract'})
		for i in range(0,len(authors)):
			pom_list.append(authors[i].contents)
		
			for p in range(0,len(pom_list[i])):
				pom_string=pom_string + pom_list[i][p]
		
			pom_string=pom_string.replace("\n","")
		
			pom_string=pom_string.replace("\t","")
			zoznam.append(pom_string)
			pom_string=""
		result_dic[dic_index].append(zoznam)
		
	
		pager=soup.find('div',attrs={'id' : 'pager'})
		if (len(pager) <2):
			break
		else:
			insert_key=insert_key+1
			next_url= soup.find('div', attrs={'id' : 'pager'})
			pom_list=[]
			author_list=[]
			spom_string=""
			
			base_url="http://citeseerx.ist.psu.edu"
			html_file=urllib2.urlopen(base_url)
	
	
			pom_string= next_url.contents[1].get('href')
	
			base_url=base_url+pom_string
	
			html_file=urllib2.urlopen(base_url)
			soup=BeautifulSoup(html_file)
	print result_dic
	#koniec whilte
	#print soup
	
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
	html_file=""
	html_file = sendUrlCiteSeerX_EXTENDED(keyword,Include,0,title_arg,autoraffi_arg,publicvenue,keywords_arg,abstract_arg,year_arg,mincitations_arg)
	soup = BeautifulSoup(html_file.read())
	
	
	
def sendUrlCiteSeerX_EXTENDED(keywordsPhrase,Citation,Sort,title_arg,autoraffi,publicvenue,keywords,abstract,year_arg,min_cit):
	http_req=""
	sort_list_no_cit=['&t=doc','&t=doc&sort=cite','&t=doc&sort=dates','&t=doc&sort=ascdate','&t=doc&sort=recent']
	sort_list_cit=['&ic=1&sort=rlv&t=doc','&ic=1&sort=cite&t=doc','&ic=1&t=doc&sort=date','&t=doc&sort=ascdate','&ic=1&t=doc&sort=recent']
	if (Citation == 0):
		http_req= "http://citeseerx.ist.psu.edu/search?q="+keywordsPhrase+"&submit=Search"+sort_list_no_cit[Sort]
	else:
		http_req= "http://citeseerx.ist.psu.edu/search?q="+keywordsPhrase+"&submit=Search"+sort_list_cit[Sort]	
	
	return http_req

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
	
	return http_req

vysledok=dict()
vysledok = basicSearch("windows",False)

		

        

