#!/usr/bin/python

"""
API Modul pre sluzbu CiteSeerX
Implementuje zakladne vyhladavanie pomocou tejto sluzby
Modul obsahuje 2 vyhladavacie funkcie: basicSearch a extendedSearch
"""




from bs4 import BeautifulSoup
import sys
import urllib2
import re
import codecs
import time

"""
     @param keyword: Vyhladaci retazec pre sluzbu
		CiteSeerX. Moze obsahovat viac klucovych
		slov pre vyhladavanie
     @param Include: Parameter, ktory indikuje zahrnanie
		citacii do vysledku.
     @type Include: True pokial chceme do vysledku
		zahrnut citacie. False pokial do vysledku
		nechcem zahrnut citacie.
     @param Sort: parameter, ktory nadobuda hodnot 0-3
		podla toho akym sposobom maju byt ztriedene 
		vysledky vyhladavania
     @return: Slovnik pricom kazda polozka odpoveda jednemu
		vysledku vyhladavania so vsetkymi informaciami o nej
"""
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
		raise Exception("Connection error")
	#time.sleep(15)
	soup=""
	soup=BeautifulSoup(html_file)
	
	
	
	
	list_authors=[]
	number_of_cycles=0
	pom_link=""
	
	
	
	
	puvenue=""
	pubyear=""
	snippet=""
	citations=""
	pubabstract=""
	results=""
	
	pom_list=[]
	pom_string=""
	name_of_pub=""
	pom_string=unicode(pom_string)
	link_cit=""
	link_lib=""
	base_link=""
	while (True):
		list_authors=[]
		results= soup.findAll('div', attrs={'class' : 'result'})
		
		for i in range(0,len(results)):
			number_of_cycles=number_of_cycles+1
		
		
		for i in range(0,number_of_cycles):
			moje=BeautifulSoup(str(results[i]))
			
			#parsovanie nazvu knihy
			 #a class="remove doc_details"
			name_of_pub= moje.find('a', attrs={'class' : 'doc_details'})
			
			if (not name_of_pub):
				list_authors.append("0")
			else:
				
				
				pom_list.append(name_of_pub.contents)
			
				for p in range(0,len(pom_list)):
					
					pom_string=pom_string + unicode(pom_list[p])
				pom_string=pom_string.replace("<em>","")
				pom_string=pom_string.replace("</em>","")
				pom_string=pom_string.replace("\n","")
				pom_string=pom_string.replace("...","")
				pom_string=pom_string.replace("\t","")
				pom_string=pom_string.strip()
				pom_string=re.sub(r'\s+', ' ', pom_string)
				list_authors.append(unicode(pom_string))
				
				pom_string=""

			#parsovanie autora
			authors= moje.find('span', attrs={'class' : 'authors'})
			if (not authors):
				list_authors.append("0")
			else:
				
				pom_list=[]
				pom_list.append(authors.contents)
			
				for p in range(0,len(pom_list)):
					
					pom_string=pom_string + unicode(pom_list[p])
				pom_string=pom_string.replace("<em>","")
				pom_string=pom_string.replace("</em>","")
				pom_string=pom_string.replace("\n","")
				pom_string=pom_string.replace("...","")
				pom_string=pom_string.replace("\t","")
				pom_string=pom_string.strip()
				pom_string=re.sub(r'\s+', ' ', pom_string)
				list_authors.append(unicode(pom_string))
				
				pom_string=""
			
			#parsovanie nazvu publikacie
			pubvenue=moje.find('span', attrs={'class' : 'pubvenue'})
			if (not pubvenue):
				list_authors.append("0")
			else:
				pom_list=[]
				pom_list.append(pubvenue.contents)
				
				for p in range(0,len(pom_list)):
					
					pom_string=pom_string + unicode(pom_list[p])
	
				pom_string=pom_string.replace("\n","")
				pom_string=pom_string.strip()
				pom_string=pom_string.replace("<em>","")
				pom_string=pom_string.replace("</em>","")
				pom_string=pom_string.replace("\t","")
				pom_string=pom_string.replace("...","")
				pom_string=re.sub(r'\s+', ' ', pom_string)
				list_authors.append(unicode(pom_string))
				
				pom_string=""
			
			#parsovanie roku publikacie
			
			
			pubyear= moje.find('span', attrs={'class' : 'pubyear'})
			if (not pubyear):
				list_authors.append("0")
			else:
				pom_list=[]
				pom_list.append(pubyear.contents)
				
				for p in range(0,len(pom_list)):
					pom_string=pom_string + unicode(pom_list[p])
				pom_string=pom_string.strip()
				
				pom_string=pom_string.replace("<em>","")
				pom_string=pom_string.replace("</em>","")
				pom_string=pom_string.replace("\n","")
				pom_string=pom_string.replace("...","")
				pom_string=pom_string.replace("\t","")
				pom_string=re.sub(r'\s+', ' ', pom_string)
				list_authors.append((unicode(pom_string)))
				
				pom_string=""
			
			#parsovanie snippetu
	
			snippet= moje.find('div', attrs={'class' : 'snippet'})
			
			
			
			if (not snippet):
				list_authors.append("0")
			else:
				pom_list=[]
				pom_list.append(snippet.contents)
				#print pom_list
				
				for p in range(0,len(pom_list)):
					pom_string=pom_string + unicode(pom_list[p])
			#odstranenie nepotrebnych znacike
				pom_string=pom_string.replace("\n","")
				pom_string=pom_string.strip()
				pom_string=pom_string.replace("\t","")
				pom_string=pom_string.replace("<em>","")
				pom_string=pom_string.replace("</em>","")
				pom_string=pom_string.replace("\"","")
				pom_string=pom_string.replace("...","")
				pom_string=re.sub(r'\s+', ' ', pom_string)
				list_authors.append((unicode(pom_string)))
			
				pom_string=""
		
			#parsovanie citacii
			
			citations= moje.find('span', attrs={'class' : 'citations'})
			if (not citations):
				list_authors.append("0")
			else:
				pom_list=[]
				pom_list.append(citations.contents)
				
				for p in range(0,len(pom_list)):
					pom_string=pom_string + unicode(pom_list[p])
				pom_string=pom_string.strip()
				pom_string=pom_string.replace("\n","")
				pom_string=pom_string.replace("...","")
				pom_string=pom_string.replace("\t","")
				pom_string=re.sub(r'\s+', ' ', pom_string)
				list_authors.append((unicode(pom_string)))
			
				pom_string=""
			
			#parsovanie abstraktu
			
			pubabstract= moje.find('span', attrs={'class' : 'pubabstract'})
			if (not pubabstract):
				list_authors.append("0")
			else:
				pom_list=[]
				pom_list.append(pubabstract.contents)
				
				for p in range(0,len(pom_list)):
					pom_string=pom_string + unicode(pom_list[p])
				pom_string=pom_string.strip()
				pom_string=pom_string.replace("\n","")
				pom_string=pom_string.replace("...","")
				pom_string=pom_string.replace("\t","")
				pom_string=re.sub(r'\s+', ' ', pom_string)
				list_authors.append((unicode(pom_string)))
				
				pom_string=""
				
			#parsovanie odkazu do kniznice
			link_lib=moje.find('a', attrs={'class' : 'doc_details'})
			if (not link_lib):
				list_authors.append("0")
			else:
				link_lib=str(link_lib.get('href'))
				base_link="http://citeseerx.ist.psu.edu"
				base_link=base_link+link_lib
				list_authors.append((unicode(base_link)))
			
			
			#parsovanie odkazu na citacie
			link_cit=moje.find('a', attrs={'class' : 'citation'})
			if (not link_cit):
				list_authors.append("0")
			else:
				pom_link=""
				link_cit=str(link_cit.get('href'))
				pom_link="http://citeseerx.ist.psu.edu"
				pom_link=pom_link+link_cit
				list_authors.append(unicode(pom_link))
			
			#parsovanie poctu citacii na dielos
			if (Include == True):
				citations= moje.find('a', attrs={'class' : 'citation'})
				if (not citations):
					list_authors.append("0")
				else:
					pom_list=[]
					pom_list.append(citations.contents)
				
					for p in range(0,len(pom_list)):
						pom_string=pom_string + unicode(pom_list[p])
					pom_string=pom_string.strip()
					pom_string=pom_string.replace("Cited by","")
					pom_string=pom_string.replace("(","")
					pom_string=pom_string.replace(")","")
					pom_string=pom_string.replace("self","")
					
					pom_string=pom_string.replace("\n","")
					pom_string=pom_string.replace("...","")
					pom_string=pom_string.replace("\t","")
					pom_string=re.sub(r'\s+', ' ', pom_string)
					pom_string=pom_string.strip()
					pom_index=0
					pom_index=pom_string.find(" ")
				
					pom_string=pom_string[:pom_index]
					list_authors.append((unicode(pom_string)))
				
				pom_string=""
			
			#vlozenie do slovnika
			result_dic[dic_index]=list_authors
			
			dic_index=dic_index+1
		#koniec prehladavanie hmtl suboru
		#snazim sa najst odkaz na dalsiu stranku
		
		pager=soup.find('div',attrs={'id' : 'pager'})
		#pokial som nenasiel ziadny koncim
		if (len(pager) <2):
			break
		#inak prejdem na dalsiu stranku
		else:
			
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
				raise Exception("Connection error")
			soup=BeautifulSoup(html_file)
	
	#koniec parsovania funkcii
	return result_dic
	


"""
    @param Text: Vyhladaci retazec pre sluzbu
		CiteSeerX. Moze obsahovat viac klucovych
		slov pre vyhladavanie
    @param Title: Nazov titulu podla ktoreho 
		sa ma vyhladavat
    @param AutorAffi: Prislusnost autora podla, ktorej sa ma 
		vyhladavat
    @param PublicVenue:Zaner diela podla, ktoreho sa ma vyhladavat
    @param Keywords: Klucove slova, ktore musia obsahovat najdene
		vysledky vyhladavania
    @param Abstract: Nazov abstraktu, ktory ma byt zahrnuty 
		do vyhladavania
    @param Year: Obsahuje hodnotu True/False podla toho, ci chceme
		vyhladavat diela podla roku vydania
    @param YearArg: Zoznam ,ktory obsahuje 2 polozky 1. Rok od, ktoreho
		chceme vyhladavat 2.polozka Rok po, ktory chceme vyhladavat
    @param MinCitatons: Minimalny pocet citacii, ktory ma vysledok
		obsahovat
    @param IncludeCitations: Parameter, ktory indikuje zahrnanie
		citacii do vysledku.
    @param SortBy: Sposob akym maju byt jednotlive vysledky triedene
		hodnoty 0-3
		@return: Slovnik pricom kazda polozka odpoveda jednemu
		vysledku vyhladavania so vsetkymi informaciami o nej
"""
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
	try:
		html_file=urllib2.urlopen(page)
	except Exception:
		raise Exception("Connection error")
	#time.sleep(15)
	soup=""
	soup=BeautifulSoup(html_file)
	
	number_of_cycles=0
	
	
	
	
	
	puvenue=""
	pubyear=""
	snippet=""
	citations=""
	pubabstract=""
	results=""
	list_authors=[]
	pom_list=[]
	pom_string=""
	name_of_pub=""
	pom_string=unicode(pom_string)
	while (True):
		list_authors=[]
		results= soup.findAll('div', attrs={'class' : 'result'})
		
		for i in range(0,len(results)):
			number_of_cycles=number_of_cycles+1
		
		
		for i in range(0,number_of_cycles):
			moje=BeautifulSoup(str(results[i]))
			
			#parsovanie nazvu knihy
			 #a class="remove doc_details"
			name_of_pub= moje.find('a', attrs={'class' : 'doc_details'})
			
			if (not name_of_pub):
				list_authors.append("0")
			else:
				
				
				pom_list.append(name_of_pub.contents)
			
				for p in range(0,len(pom_list[i])):
					
					pom_string=pom_string + unicode(pom_list[i][p])
				pom_string=pom_string.replace("<em>","")
				pom_string=pom_string.replace("</em>","")
				pom_string=pom_string.replace("\n","")
				pom_string=pom_string.replace("...","")
				pom_string=pom_string.replace("\t","")
				pom_string=pom_string.strip()
				pom_string=re.sub(r'\s+', ' ', pom_string)
				list_authors.append(unicode(pom_string))
				
				pom_string=""

			#parsovanie autora
			authors= moje.find('span', attrs={'class' : 'authors'})
			if (not authors):
				list_authors.append("0")
			else:
				
				
				pom_list.append(authors.contents)
			
				for p in range(0,len(pom_list[i])):
					
					pom_string=pom_string + unicode(pom_list[i][p])
				pom_string=pom_string.replace("<em>","")
				pom_string=pom_string.replace("</em>","")
				pom_string=pom_string.replace("\n","")
				pom_string=pom_string.replace("...","")
				pom_string=pom_string.replace("\t","")
				pom_string=pom_string.strip()
				pom_string=re.sub(r'\s+', ' ', pom_string)
				list_authors.append(unicode(pom_string))
				
				pom_string=""
			
			#parsovanie nazvu publikacie
			pubvenue=moje.find('span', attrs={'class' : 'pubvenue'})
			if (not pubvenue):
				list_authors.append("0")
			else:
				pom_list.append(pubvenue.contents)
				
				for p in range(0,len(pom_list[i])):
					
					pom_string=pom_string + unicode(pom_list[i][p])
	
				pom_string=pom_string.replace("\n","")
				pom_string=pom_string.strip()
				pom_string=pom_string.replace("<em>","")
				pom_string=pom_string.replace("</em>","")
				pom_string=pom_string.replace("\t","")
				pom_string=pom_string.replace("...","")
				pom_string=re.sub(r'\s+', ' ', pom_string)
				list_authors.append(unicode(pom_string))
				
				pom_string=""
			
			#parsovanie roku publikacie
			
			
			pubyear= moje.find('span', attrs={'class' : 'pubyear'})
			if (not pubyear):
				list_authors.append("0")
			else:
				pom_list.append(pubyear.contents)
				
				for p in range(0,len(pom_list[i])):
					pom_string=pom_string + unicode(pom_list[i][p])
				pom_string=pom_string.strip()
				
				pom_string=pom_string.replace("<em>","")
				pom_string=pom_string.replace("</em>","")
				pom_string=pom_string.replace("\n","")
				pom_string=pom_string.replace("...","")
				pom_string=pom_string.replace("\t","")
				pom_string=re.sub(r'\s+', ' ', pom_string)
				list_authors.append((unicode(pom_string)))
				
				pom_string=""
			
			#parsovanie snippetu
	
			snippet= moje.find('div', attrs={'class' : 'snippet'})
			
			
			
			if (not snippet):
				list_authors.append("0")
			else:
				
				pom_list.append(snippet.contents)
				#print pom_list
				
				for p in range(0,len(pom_list[i])):
					pom_string=pom_string + unicode(pom_list[i][p])
			#odstranenie nepotrebnych znacike
				pom_string=pom_string.replace("\n","")
				pom_string=pom_string.strip()
				pom_string=pom_string.replace("\t","")
				pom_string=pom_string.replace("<em>","")
				pom_string=pom_string.replace("</em>","")
				pom_string=pom_string.replace("\"","")
				pom_string=pom_string.replace("...","")
				pom_string=re.sub(r'\s+', ' ', pom_string)
				list_authors.append((unicode(pom_string)))
			
				pom_string=""
		
			#parsovanie citacii
			
			citations= moje.find('span', attrs={'class' : 'citations'})
			if (not citations):
				list_authors.append("0")
			else:
				pom_list=[]
				pom_list.append(citations.contents)
				
				for p in range(0,len(pom_list[i])):
					pom_string=pom_string + unicode(pom_list[i][p])
				pom_string=pom_string.strip()
				pom_string=pom_string.replace("\n","")
				pom_string=pom_string.replace("...","")
				pom_string=pom_string.replace("\t","")
				pom_string=re.sub(r'\s+', ' ', pom_string)
				list_authors.append((unicode(pom_string)))
			
				pom_string=""
			
			#parsovanie abstraktu
			
			pubabstract= moje.find('span', attrs={'class' : 'pubabstract'})
			if (not pubabstract):
				list_authors.append("0")
			else:
				pom_list=[]
				pom_list.append(pubabstract.contents)
				
				for p in range(0,len(pom_list[i])):
					pom_string=pom_string + unicode(pom_list[i][p])
				pom_string=pom_string.strip()
				pom_string=pom_string.replace("\n","")
				pom_string=pom_string.replace("...","")
				pom_string=pom_string.replace("\t","")
				pom_string=re.sub(r'\s+', ' ', pom_string)
				list_authors.append((unicode(pom_string)))
				
				pom_string=""
				
			#parsovanie odkazu do kniznice
			link_lib=moje.find('a', attrs={'class' : 'doc_details'})
			if (not link_lib):
				list_authors.append("0")
			else:
				link_lib=str(link_lib.get('href'))
				base_link="http://citeseerx.ist.psu.edu"
				base_link=base_link+link_lib
				list_authors.append((unicode(base_link)))
			
			
			#parsovanie odkazu na citacie
			link_cit=moje.find('a', attrs={'class' : 'citation'})
			if (not link_cit):
				list_authors.append("0")
			else:
				pom_link=""
				link_cit=str(link_cit.get('href'))
				pom_link="http://citeseerx.ist.psu.edu"
				pom_link=pom_link+link_cit
				list_authors.append(unicode(pom_link))	
				
			#parsovanie poctu citacii na dielos
			if (Include == True):
				citations= moje.find('a', attrs={'class' : 'citation'})
				if (not citations):
					list_authors.append("0")
				else:
					
					pom_list.append(citations.contents)
				
					for p in range(0,len(pom_list[i])):
						pom_string=pom_string + unicode(pom_list[i][p])
					pom_string=pom_string.strip()
					pom_string=pom_string.replace("Cited by","")
					pom_string=pom_string.replace("(","")
					pom_string=pom_string.replace(")","")
					pom_string=pom_string.replace("self","")
					
					pom_string=pom_string.replace("\n","")
					pom_string=pom_string.replace("...","")
					pom_string=pom_string.replace("\t","")
					pom_string=re.sub(r'\s+', ' ', pom_string)
					pom_string=pom_string.strip()
					pom_index=0
					pom_index=pom_string.find(" ")
				
					pom_string=pom_string[:pom_index]
					list_authors.append((unicode(pom_string)))
				
				pom_string=""
			
			#vlozenie do slovnika
			result_dic[dic_index]=list_authors
			
			dic_index=dic_index+1
		#koniec prehladavanie hmtl suboru
		#snazim sa najst odkaz na dalsiu stranku
		
		pager=soup.find('div',attrs={'id' : 'pager'})
		#pokial som nenasiel ziadny koncim
		if (len(pager) <2):
			break
		#inak prejdem na dalsiu stranku
		else:
			
			next_url= soup.find('div', attrs={'id' : 'pager'})
			pom_list=[]
			author_list=[]
			spom_string=""
			
			base_url="http://citeseerx.ist.psu.edu"
			try:
				html_file=urllib2.urlopen(base_url)
			except Exception:
				raise Exception("Connection error")
	
			pom_string= next_url.contents[1].get('href')
	
			base_url=base_url+pom_string
			try:
				html_file=urllib2.urlopen(base_url)
			except Exception:
				raise RuntimeError("Connection error")
			soup=BeautifulSoup(html_file)
	
	#koniec parsovania funkcii
	return result_dic
	
	
"""
    @param keywordsPhrase: Vyhladaci retazec pre sluzbu
		CiteSeerX. Moze obsahovat viac klucovych
		slov pre vyhladavanie
	@param Citation: Zahrnutie citacii do vysledkov vyhladavania
	@param Sort: Sposob akym maju byt jednotlive vysledky triedene
		hodnoty 0-3
    @param title_arg: Zahrnutie nazvu titulu do vyhladavania
    @param author_name: Nazov autora
    @param autoraffi: Prislusnost autora podla, ktorej sa ma 
		vyhladavat
    @param publicvenue:Zaner diela podla, ktoreho sa ma vyhladavat
    @param keywords: Klucove slova, ktore musia obsahovat najdene
		vysledky vyhladavania
    @param abstract: Nazov abstraktu, ktory ma byt zahrnuty 
		do vyhladavania
    @param year_arg: Zoznam ,ktory obsahuje 2 polozky 1. Rok od, ktoreho
		chceme vyhladavat 2.polozka Rok po, ktory chceme vyhladavat
    @param MinCitatons: Minimalny pocet citacii, ktory ma vysledok
		obsahovat
    @param IncludeCitations: Parameter, ktory indikuje zahrnanie
    @return: Slovnik pricom kazda polozka odpoveda jednemu
		vysledku vyhladavania so vsetkymi informaciami o nej
"""
def __sendUrlCiteSeerX_EXTENDED(keywordsPhrase,Citation,Sort,title_arg,author_name,autoraffi,publicvenue,keywords,abstract,year_arg,min_cit):
	
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
		raise ValueError("Bad values")
			
			
			
			
			
	sort_list_no_cit=['&t=doc','&t=doc&sort=cite','&t=doc&sort=dates','&t=doc&sort=ascdate','&t=doc&sort=recent']
	sort_list_cit=['&ic=1&sort=rlv&t=doc','&ic=1&sort=cite&t=doc','&ic=1&t=doc&sort=date','&t=doc&sort=ascdate','&ic=1&t=doc&sort=recent']
	
	if (Citation == 0):
		http_req= http_req + keywordsPhrase+"&submit=Search"+sort_list_no_cit[Sort]
	else:
		http_req= http_req + keywordsPhrase+"&submit=Search"+sort_list_cit[Sort]	
		
	
	return http_req

"""
     @param s: Retazec v ktorom sa orezu medzery
	 @return: Orezany vstupny retazec
"""
def __strip_one_space(s):
    if s.endswith(" "): s = s[:-1]
    if s.startswith(" "): s = s[1:]
    return s

"""
     @param keywordPhrase: Vyhladaci retazec pre sluzbu
		CiteSeerX. Moze obsahovat viac klucovych
		slov pre vyhladavanie
     @param Citation: Zahrnuti citacii do vyhladavania
     @param Sort: parameter, ktory nadobuda hodnot 0-3
		podla toho akym sposobom maju byt ztriedene 
		vysledky vyhladavania
     @return: Slovnik pricom kazda polozka odpoveda jednemu
		vysledku vyhladavania so vsetkymi informaciami o nej
"""
def __sendUrlCiteSeerX_BASIC(keywordsPhrase,Citation,Sort):
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
vysledok = basicSearch("windows",True,0)

print vysledok
		

        

