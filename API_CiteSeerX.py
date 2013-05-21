#!/usr/bin/python

'''
API Modul pre sluzbu CiteSeerX
Implementuje zakladne vyhladavanie pomocou tejto sluzby
Modul obsahuje 2 vyhladavacie funkcie: basicSearch a extendedSearch
'''

from bs4 import BeautifulSoup
import sys
import urllib2
import re

import time
'''
Funkcia, ktora splna zakladne vyhladavanie pomocou sluzby CiteSeerX
@param:keyword - vyhladavacia fraz(retazec),Include - Bool. hodnota
@return: asociativne_pole
'''
def basicSearch(keyword,Include,Sort):
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
	keyword=keyword.strip()
	keyword = re.sub(' +',' ',keyword)
	keyword=keyword.replace(" ","+")
	pocet=0
	page= sendUrlCiteSeerX_BASIC(keyword,Include,Sort)
	zoznam=[]
	try:
		html_file=urllib2.urlopen(page)
	except Exception:
		raise RuntimeError("Connection error")
	#time.sleep(15)
	soup=""
	soup=BeautifulSoup(html_file)
	
	

	while (True):
		
		list_authors=[]
		pom_list=[]
		pom_string=""
		pocet=0
		authors= soup.findAll('span', attrs={'class' : 'authors'})
		for o in range(0,len(authors)):
			pocet=pocet+1
		
		if (not authors):
			for i in range(0,pocet):
				list_authors[i].append("0")
		
		
		for i in range(0,len(authors)):
			pom_list.append(authors[i].contents)
			
			for p in range(0,len(pom_list[i])):
				pom_string=pom_string + pom_list[i][p]
		
			pom_string=pom_string.replace("\n","")
			
			pom_string=pom_string.replace("\t","")
	
			
			list_authors.append(pom_string)
			
			pom_string=""
		
		dic_index=0
		
		
		
		pom_string=""
		pubvenue_list=[]
		authors= soup.findAll('span', attrs={'class' : 'pubvenue'})
		
		if (not authors):
			for i in range(0,pocet):
			
				pubvenue_list.append("0")
		for i in range(0,len(authors)):
			pom_list.append(authors[i].contents)
		
			for p in range(0,len(pom_list[i])):
				pom_string=pom_string + pom_list[i][p]
		
			pom_string=pom_string.replace("\n","")
		
			pom_string=pom_string.replace("\t","")
			zoznam.append(pom_string)
			print zoznam	
			result_dic[dic_index].append(zoznam[p])
		
			pom_string=""
		
	
		pom_list=[]
		
		pom_string=""
		
		
		pubyear_list=[]
		authors= soup.findAll('span', attrs={'class' : 'pubyear'})
		if (not authors):
			for i in range(0,pocet):
				pubyear_list.append("0")
		for i in range(0,len(authors)):
			pom_list.append(authors[i].contents)
			
			for p in range(0,len(pom_list[i])):
				pom_string=pom_string + pom_list[i][p]
		
			pom_string=pom_string.replace("\n","")
		
			pom_string=pom_string.replace("\t","")
			pubyear_list.append(pom_string)
			pom_string=""
		
		
		pom_list=[]
		snippet_list=[]
		pom_string=""
		pom_string=unicode(pom_string)
		authors= soup.findAll('div', attrs={'class' : 'snippet'})
		
		if (not authors):
			for i in range(0,pocet):
				snippet_list.append("0")
		for i in range(0,len(authors)):
			pom_list.append(authors[i].contents)
			
			for p in range(0,len(pom_list[i])):
				
				pom_string=pom_string + unicode(pom_list[i][p])
		
			pom_string=pom_string.replace("\n","")
			
			pom_string=pom_string.replace("\t","")
			pom_string=pom_string.replace("<em>","")
			pom_string=pom_string.replace("</em>","")
			pom_string=pom_string.replace("\"","")
			pom_string=pom_string.replace("...","")
			snippet_list.append(pom_string)
			pom_string=""
		
		print snippet_list[0]
		sys.exit(0)
		pom_list=[]
		
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
			try:
				html_file=urllib2.urlopen(base_url)
			except Exception:
				raise RuntimeError("Connection error")
			soup=BeautifulSoup(html_file)
	print result_dic
	#koniec whilte
	#print soup
	
	return result_dic
	

'''
Funkcia, ktora splna rozsirene vyhladavanie pomocou sluzby CiteSeerX
@rparam:text - vyhladavaci retazec
@param:Title - nazov titulu
@param:AutorAffi - prislusnost autora
@param:PublicVenue - zaner diela
@oaram: Keywords - klucove slova 
@return: asociativne_pole
'''	
def extendedSearch(Text,Title,AutorAffi,PublicVenue,Keywords,Abstract,Year,
YearArg,MinCitations,IncludeCitation,SortBy):
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
	
	
	if (Text != False):
		text_arg=1
	elif(Title!=0):
		title_arg=1
	elif (AutorAffi !=False):
		autoraffi_arg=1
	elif (PublicVenue != False):
		publicvenue_arg=1
	elif (keywords!=False):
		keywords_arg=1
	elif (Abstract !=False):
		abstract_arg=1
	elif (Year!=False):
		year_arg=1
	elif (MinCitations != False):
		mincitations_arg=1
	
	elif (IncludeCitation != False):
			citations_arg=1
	html_file=""
	html_file = sendUrlCiteSeerX_EXTENDED(keyword,Include,0,title_arg,autoraffi_arg,publicvenue,keywords_arg,abstract_arg,year_arg,mincitations_arg)
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
	keyword=keyword.strip()
	keyword = re.sub(' +',' ',keyword)
	keyword=keyword.replace(" ","+")

	page= sendUrlCiteSeerX_BASIC(keyword,Include,Sort)
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
Funkcia, ktora formuje zakladny URL dokaz na zaklade udajov ktore dostane od uzivatela
'''	
def sendUrlCiteSeerX_EXTENDED(keywordsPhrase,Citation,Sort,title_arg,author_name,autoraffi,publicvenue,keywords,abstract,year_arg,min_cit):
	
	http_req="http://citeseerx.ist.psu.edu/search?q="
	couter=0
	try:
		if (keywordsPhrase != False):
			http_req = http_req + "text%3A" + keywordsPhrase 
			counter=counter+1
		elif (title_arg != False):
			if (counter !=0):
				http_req = http_req + "+AND+" + "title%3A" + title_arg
				counter=counter+1
			else:
				http_re = http_req + "title%3A" + title_arg
				counter=counter+1
		elif (author_name != False):
			if (counter !=0):
				http_req = http_req + "+AND+" + "author%3A" + author_name
				counter=counter+1
			else:
				http_re = http_req + "author%3A" + author_name
				counter=counter+1
		elif (autoraffi != False):
			if (counter !=0):
				http_req = http_req + "+AND+" + "affil%3A" + autoraffi
				counter=counter+1
			else:
				http_re = http_req + "affil%3A" + autoraffi
				counter=counter+1
		elif (publicvenue != False):
			if (counter !=0):
				http_req = http_req + "+AND+" + "venue%3A" + publicvenue
				counter=counter+1
			else:
				http_re = http_req + "venue%3A" + publicvenue
				counter=counter+1
		elif (keywords != False):
			if (counter !=0):
				http_req = http_req + "+AND+" + "keyword%3A" + keywords
				counter=counter+1
			else:
				http_re = http_req + "keyword%3A" + keywords
				counter=counter+1
		elif (abstract!= False):
			if (counter !=0):
				http_req = http_req + "+AND+" + "abstract%3A" + abstract
				counter=counter+1
			else:
				http_re = http_req + "abstract%3A" + abstract
				counter=counter+1
			
			
		elif (yearArg != False):
			if (counter !=0):
			
				if (yearArg[0] >=1900 and yearArg[1] == 0):
					http_req = http_req + "+AND+" + "year%3A%5B" + yearArg[0] + "+TO+" + "2014"+ "%5D"
					counter=counter+1
				else:
					http_req = http_req + "+AND+" + "year%3A%5B" + yearArg[0] + "+TO+" + yearArg[1]+ "%5D"
					counter=counter+1
			else:
				if (yearArg[0] >=1900 and yearArg[1] == 0):
					http_req = http_req + "+AND+" + "year%3A%5B" + yearArg[0] + "+TO+" + "2014"+ "%5D"
					counter=counter+1
				else:
					http_req = http_req + "+AND+" + "year%3A%5B" + yearArg[0] + "+TO+" + yearArg[1]+ "%5D"
					counter=counter+1
		elif (min_cit != False):
			if (counter !=0):
				http_req = http_req + "+AND+" + "ncites%3A%5B" + min_cit
				counter=counter+1
			else:
				http_re = http_req + "ncites%3A%5B" + min_cit
				counter=counter+1
	except Exception:
		raise Exception("Bad value")
			
			
			
			
			
	sort_list_no_cit=['&t=doc','&t=doc&sort=cite','&t=doc&sort=dates','&t=doc&sort=ascdate','&t=doc&sort=recent']
	sort_list_cit=['&ic=1&sort=rlv&t=doc','&ic=1&sort=cite&t=doc','&ic=1&t=doc&sort=date','&t=doc&sort=ascdate','&ic=1&t=doc&sort=recent']
	
	if (Citation == 0):
		http_req= http_req + keywordsPhrase+"&submit=Search"+sort_list_no_cit[Sort]
	else:
		http_req= http_req + keywordsPhrase+"&submit=Search"+sort_list_cit[Sort]	
		
	
	return http_req

'''
Funkcia, ktora mi vymaze prebytocne medzery
'''
def strip_one_space(s):
    if s.endswith(" "): s = s[:-1]
    if s.startswith(" "): s = s[1:]
    return s

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
	
	
	return http_req

vysledok=dict()
vysledok = basicSearch("nieco",False,0)


		

        

