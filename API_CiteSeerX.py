#!/usr/bin/python

'''
API Modul pre sluzbu CiteSeerX
Implementuje zakladne vyhladavanie pomocou tejto sluzby
Modul obsahuje 2 vyhladavacie funkcie: basicSearch a extendedSearch
'''

from bs4 import BeautifulSoup
import sys
import urllib2

















html_doc = """





<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
























  	
  
  
  
 



  





<html xmlns:og="http://ogp.me/ns#" xmlns:fb="https://www.facebook.com/2008/fbml" xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-US" lang="en-US">

  <head>

	
  
	<title>IEEE Xplore - 
		On the use of windows for harmonic analysis with the discrete Fourier transform
	</title>
	



<link rel="stylesheet" href="/assets/css/print.css" type="text/css" media="print" />


<!-- includes mete name description and title tags -->





	
	
			 
		
		 		 	
				
			
			
		
		
		 		 	
				
			
			
		
	
	
	
	
	
	
	
	
	
	
	

	

	

	
	
	

	

	

	
	
	
	
	
	

	

	
	
	
	
	
	
	
	
	
	
	
		
	

	

	

	
		
	
		
	


<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
	
	<meta name="Description" content="This paper makes available a concise review of data windows and their affect on the detection of harmonic signals in the presence of broad-band noise, and in the presence of nearby strong harmonic interference. We also call attention to a number of common errors in the application of windows when used with the fast Fourier transform. This paper includes a comprehensive catalog of data windows along with their significant performance parameters from which the different windows can be compared. Finally, an example demonstrates the use and value of windows to resolve closely spaced harmonic signals characterized by large differences in amplitude."> 

	
	<meta name="Title" CONTENT="IEEE Xplore - On the use of windows for harmonic analysis with the discrete Fourier transform"> 





<script type="text/javascript">
//<![CDATA[
    IS_INDIVIDUAL_USER=false;
    
	ASSETS_RELATIVE_PATH = '/assets';
	IBP_WS_ASSETS='https://www.ieee.org';
	var IBP_WS_ENABLED_FLAG = 'true';
	//var WEBSERVICES_INCLUDE_MINICART_MASHUP_FLAG;
	if (IBP_WS_ENABLED_FLAG.toUpperCase() == "FALSE" )	
	{
		IBP_WS_ENABLED_FLAG = false;
	}
	else
	{
		IBP_WS_ENABLED_FLAG=true;	
	}
	//]]>
</script>

<style type="text/css" media="screen, print">
	@import url(/assets/css/jquery.qtip.min.css);
	@import url(/assets/css/master.css);
	@import url(/assets/css/endeca.min.css);
	@import url(/assets/js/colorbox/colorbox.min.css);
	@import url(/assets/css/simplePassMeter.min.css);	
</style>
<link rel="stylesheet" href="/assets/css/jquery-ui-1.8.19.custom.css"/>



<script type="text/javascript">
	var NTPT_IMAGE_LOCATION = 'http://tagxplore.ieee.org/';
	var XPLORE_SSL_HOST = 'https://ieeexplore.ieee.org';
    var XPLORE_SSL_YES_NO = true;
	var SSL_YES_NO = 'yes';
	if (SSL_YES_NO.toUpperCase() == "NO"){
		XPLORE_SSL_YES_NO = false;
	}
	var WEBSERVICES_SSL_YES_NO = 'yes';
	var XPLORE_WEBSERV_YES_NO = true;
	if (WEBSERVICES_SSL_YES_NO.toUpperCase() == "NO"){
		XPLORE_WEBSERV_YES_NO = false;
	}
	var IBP_MEMBEER_SIGNIN_TIME_WAIT_IN_MILLIES = '800';
	var ASSETS_RELATIVE_PATH = '/assets';
	var SPECIAL_CHARACTER_MAPS = '&:.AND.,=:.EQ.,+:.PLS.,#:.HSH.,(:.LB.,):.RB.,":.QT.';
	var SPECIAL_CHARACTERS = new Array();
	var SPECIAL_CHARACTER_REPLACEMENTS = new Array();
	var characterMaps = SPECIAL_CHARACTER_MAPS.split(",");
	for (var i = 0; i < characterMaps.length; i++) {
		parts = characterMaps[i].split(":");
		SPECIAL_CHARACTERS[i] = parts[0];
		SPECIAL_CHARACTER_REPLACEMENTS[i] = parts[1];
	}

	var ALL_SEARCH_FIELDS = 'Search_Index_Terms:Index Terms,Search_All_Text:Full Text & Metadata,Search_All:Metadata Only,Search_Publication_Title:Search Publication Title,Search_Related_Terms:Search Related Terms,Search_Authors:Author Name,p_Id:Article Number,p_Endeca_Id:Endeca Id,p_Module_Number:Module Number,p_Part_Num:Part Num,p_ISSN:ISSN,p_ISBN:ISBN,p_EISBN:EISBN,p_IS_Number:IS Number,p_Accession_Number:Accession Number,p_Article_Number:Article Number,p_Copyright_Holder:Copyright Holder,p_Copyright_Year:Copyright Year,p_Title:Document Title,p_Abstract:Abstract,p_Publication_Number:Publication Number,p_Parent_Publication_Number:Parent Publication Number,p_Publication_Title:Publication Title,p_Volume:Volume,p_Issue:Issue,p_Padded_Issue_Number:Padded Issue Number,p_Part:Part,p_Start_Page:Start Page,p_End_Page:End Page,p_File_Path:File Path,p_Publication_Date:Publication Date,p_Publication_Year:Publication Year,p_Online_Date:Online Date,p_Month:Month,p_Author_Pref_Names:Author Pref Names,p_Authors:Authors,p_Author_Affiliations:Author Affiliations,p_Reference_Count:Reference Count,p_Citation_Count:Citation Count,p_Multimedia_Flag:Multimedia Flag,p_Biomedical_Eng_Flag:Biomedical Eng Flag,p_Non_IEEE:Non IEEE,p_STDS_Product_Number:STDS Product Number,p_Status:Status,p_DOI:DOI,p_Pdf_Path:Pdf Path,p_Pdf_Size:Pdf Size,p_Content_Type:Content Type,p_Publisher:Publisher,p_Controlled_Terms:INSPEC Controlled Terms,p_Free_Terms:INSPEC Non-Controlled Terms,p_IEEE_Terms:IEEE Terms,p_Author_Terms:Author Keywords,p_Mesh_Terms:MeSH Terms,p_PACS_Terms:PACS Terms,p_DOE_Terms:DOE Terms,p_Insert_Date:Insert Date,Conference_Location:nference Location,p_Index_Content:Index Content,p_CODEN:CODEN,p_Document_Text:Document Text,p_Standard_Number:Standard Number,p_Preprint_Flag:Preprint Flag,p_Rapid_Post_Flag:Rapid Post Flag,p_Last_Update:Last Update,p_New_Flag:New Flag,p_Open_Access_Flag:Open Access Flag,p_Pubmed_Id:Pubmed Id,p_Duration:Duration,p_Society:Society,p_Conference:Conference,p_Society_URL:Society URL,p_Id_Subject:Id Subject,p_Book_Number:Book Number,p_Pages:Pages,p_Edition_Number:Edition Number,p_Sequence:Sequence,p_Related_Info_Type:Related Info Type,p_Related_Info:Related Info,p_Format_ISBN:Format ISBN,p_Meeting_Date:Meeting Date,p_Course_level:Course level,p_Course_ID:Course ID,p_About_Url:About Url,p_Additional_Url:Additional Url,p_Authors_Url:Authors Url,p_Open_Access_Url:Open Access Url,p_Partnum_VendorURL_MediaType:Partnum VendorURL MediaType,p_Branding_Image_File:Branding Image File,p_Cover_Image_File:Cover Image File,p_Frequency:Frequency,p_Field_Of_Interest:Field Of Interest,p_G_Parent_Publication_Number:G Parent Publication Number,p_Ms_Url:Ms Url,p_Relationship:Relationship,p_Society_Image:Society Image,p_Visit_Url:Visit Url,p_Visit_Website:Visit Website,p_Start_Year:Start Year,p_End_Year:End Year,p_Record_Type:Record Type,p_Rollup_Key:Rollup Key,p_Epub:Epub,p_Pic_Code_Description:Pic Code Description,p_Pic_Code:Pic Code,p_Sponsors:Sponsors,p_Notes:Notes,p_Conference_Date:Conference Date,p_Publication_Contact:Publication Contact,p_isBuyable:isBuyable,p_Publication_Files:Publication Files,p_Map_Pricing_Key:Map Pricing Key,p_Unavailable_for_Sale:Unavailable for Sale,p_Publication_Sort:Publication Sort,p_Standard_Family:Standard Family,p_Standard_Group:Standard Group,p_Product_Url:Product Url,p_ISBN_MediaType:ISBN MediaType,p_Html_Flag:Html Flag,p_Rightslink_Flag:Rightslink Flag,p_Page_Count:Page Count,p_Name:Name,p_Table_of_Contents:Table of Contents,p_Time_Stamp:Time Stamp,p_Insert_Date:Insert Date,p_Sub_Title:Sub Title,p_Related_Item:Related Item,p_Reference_Material:Reference Material,p_Latest_Issue_Time:Latest Issue Time,p_Search_Latest_Date:Search Latest Date,p_Pbd_Flag:Pbd Flag,p_Lms_Url:Lms Url,p_Current_Volume:Current Volume,p_Author_Ids:Author Ids,p_First_Names:First Name,p_Middle_Names:Middle Name,p_Last_Names:Last Name,Type_Ahead_Terms:Type Ahead Terms,IEEE_Term:IEEE Term,Content_Type:Content Type,Author:Author,Affiliation:Affiliation,Topic:Topic,Publication_Title:Publication Title,Publication_Year:Publication Year,Publisher:Publisher,Conference_Country:Conference Country,Conference_Location:Conference Location,Standard_Status:Standard Status,Conference_Year:Conference Year,Publication_Package:Subscribed Content,Standard_Package:Standard Package,Standard_Title:Standard Title,Standard_Term:Standards Dictionary Terms,Publication_Range:Publication Range,Standard_Range:Standard Range,Record_Type:Record Type,Media_Type:Media Type,Book_Type:Book Type,Course_Type:Course Type,Publication_Standard_Range:Publication Standard Range,Perpetual_Year:Perpetual Year,Opac_Title_Range:Opac Title Range';
	var SEARCH_FIELD_REFERENCES = new Array();
	var SEARCH_FIELD_DISPLAYS = new Array();
	var searchFields = ALL_SEARCH_FIELDS.split(",");
	for (var j = 0; j < searchFields.length; j++) {
		parts = searchFields[j].split(":");
		SEARCH_FIELD_REFERENCES[j] = parts[0];
		SEARCH_FIELD_DISPLAYS[j] = parts[1];
	}
	
	var PAGE_TAGGING = 'ON';
	var wt_domain = 'statse.webtrendslive.com';
	var wt_dcsid = 'dcs7nlnxvuz5bdjhyiihzogfg_6x8o';
	if(PAGE_TAGGING && PAGE_TAGGING == 'ON') {
		PAGE_TAGGING = true;
	} else {
		PAGE_TAGGING = false;
	}
	// This adds trim support in IE, without this any use of trim will break in IE
	if(typeof String.prototype.trim !== 'function') {
		  String.prototype.trim = function() {
		    return this.replace(/^\s+|\s+$/g, ''); 
		  }
		}
		
	function applySpecialCharacterMapping(terms, ignoreBrackets) {
		for (var i = 0; i < SPECIAL_CHARACTERS.length; i++) {
			if(ignoreBrackets && (SPECIAL_CHARACTERS[i] == '(' || SPECIAL_CHARACTERS[i] == ')')) {
				continue;
			}
			var index = terms.indexOf(SPECIAL_CHARACTERS[i]);
			while (index > -1) {
				terms = terms.replace(SPECIAL_CHARACTERS[i], SPECIAL_CHARACTER_REPLACEMENTS[i]);
				index = terms.indexOf(SPECIAL_CHARACTERS[i]);
			}
		}
		return terms;
	}
	
	function reverseCharacterMaps(terms) {
		for (var i = 0; i < SPECIAL_CHARACTER_REPLACEMENTS.length; i++) {
			var index = terms.indexOf(SPECIAL_CHARACTER_REPLACEMENTS[i]);
			while (index > -1) {
				terms = terms.replace(SPECIAL_CHARACTER_REPLACEMENTS[i], SPECIAL_CHARACTERS[i]);
				index = terms.indexOf(SPECIAL_CHARACTER_REPLACEMENTS[i]);
			}
		}
		return terms;
	}

	function isSearchField(term) {
		if (ALL_SEARCH_FIELDS.indexOf(term) > -1) {
			return true;
		}
		return false;
	}

	function isFunction(fName) {
		var functionName = fName;
		
		var isDefined = eval('(typeof ' + functionName + '==\'function\');');
		if (isDefined) {
			return true;
		}
		else
		{
			return false;
		}
	}
		
</script>






<script type="text/javascript" src="/assets/js/prototype.min.js" charset="utf-8"></script>
<script type="text/javascript" src="/assets/js/prototype_extensions.min.js" charset="utf-8"></script>
<!-- <script type="text/javascript" src="/assets/js/jquery-1.5.1.min.js" charset="utf-8"></script> -->
<script type="text/javascript" src="/assets/js/libs/jquery-1.5.1.js" charset="utf-8"></script>
<script type="text/javascript" src="/assets/js/jquery-ui-1.8.16.custom.min.js"></script>
<script type="text/javascript" src="/assets/js/lib.min.js"></script>
<script type="text/javascript" src="/assets/js/colorbox/jquery.colorbox-min.js" charset="utf-8"></script>
<script type="text/javascript" src="/assets/js/jquery.qtip.min.js"></script>	
<script type="text/javascript" src="/assets/js/search.min.js"></script>
<script type="text/javascript" src="/assets/js/butterfly.min.js"></script>
<script type="text/javascript" src="/assets/js/ieee-webtrends-min.js"></script>
<script type="text/javascript" src="/assets/js/libs/jq-pubsub.js"></script> 
<script type="text/javascript" src="/assets/js/jquery.cookie.js"></script> 
<script type="text/javascript" src="/assets/js/site.js"></script> 


	


		




<!--[if gt IE 8]>
        <link rel="stylesheet" type="text/css" href="/assets/css/ie9.css" />
<![endif]-->

<!--[if IE 8]>
        <link rel="stylesheet" type="text/css" href="/assets/css/ie8.css" />
<![endif]-->

<!--[if IE 7]>
        <link rel="stylesheet" type="text/css" href="/assets/css/ie7.css" />
<![endif]-->

<!--[if IE 6]>
        <link rel="stylesheet" type="text/css" href="/assets/css/ie6.css" />
<![endif]-->
<script type="text/javascript" src="/assets/easyxdm/easyXDM.min.js"></script>
<script type="text/javascript">

xhr = new easyXDM.Rpc({
	//protocol: 0 ,
    //local: "/assets/img/logo.xplore.gif",
    // local: XPLORE_SSL_HOST+'/assets/easyxdm/name.html',
    // hash: "true",	   
    swf: XPLORE_SSL_HOST+"/assets/easyxdm/easyxdm.swf",
    // swfContainer: "flashContainer",
    //swfNoThrottle:"true",
    container: "iframeContainer",	   
    props:{
 		style: { width: "20px", height: "20px", background: "white", allowTransparency: "true",marginwidth: "0", marginheight: "0", frameborder: "0",margin: "0",  border: "0px" }
    
    },
    //remote: XPLORE_SSL_HOST+'/assets/easyxdm/cors/'
    remote: XPLORE_SSL_HOST+"/assets/easyxdm/cors/",
    //remoteHelper: XPLORE_SSL_HOST+'/assets/easyxdm/name.html'    
    onReady: function() 
    {    
    	//alert('activityFrameLoaded: onReady'+XPLORE_SSL_HOST);  // this gets called  
    }
    
    }, {
    	remote: {
             request: {}
       }
});
</script>
	<script type="text/javascript" src="/assets/js/search-pages.js"></script>
	<script type="text/javascript" src="http://partner.googleadservices.com/gampad/google_service.js"></script>
	<script type="text/javascript">
	
	function removeParameter(queryString, paramKey) {
		var start = queryString.indexOf(paramKey + '=');
		if (start > -1) {
			var end = queryString.indexOf('&', start);
			
			// Ignore if & is last character.
			if ((end+1) == queryString.length) {
				end = -1;
			} 
			queryString = (end > start) ? queryString.substring(0, start) + queryString.substring(end+1) : queryString.substring(0, start);
		}
		return queryString;
	}
	
	function showAbstract(articleNumber) {
		var oqs = document.getElementById("oqs").value;
		oqs = removeParameter(oqs, 'arnumber');
		oqs = removeParameter(oqs, 'contentType');
		oqs += '&'+ 'arnumber'+'='+articleNumber;
		var  url_string = '/xpl/articleDetails.jsp?' + oqs;
		if (url_string.indexOf('&resultAction=ABSTRACT') < 0) {
			url_string += '&resultAction=ABSTRACT';
		}
		//url_string = encodeURI(url_string);
		window.location = url_string;	
	}
		
	function BackToSearchresults(articleNumber) {
		var oqs = document.getElementById("oqs").value;
		oqs = removeParameter(oqs, 'arnumber');
		var url_string = '/search/searchresult.jsp?' + oqs;
		url_string += '&resultAction=ABSTRACT';
		//url_string = encodeURI(url_string);
		window.location = url_string;
	}
	
	function loginRedirect() {
	    var url_string = '/Xplore/login.jsp';
	    window.location = url_string;
	}
	
	function sendLoginRedirect() {
		var location_url = location.href;
		//location_url = location_url.replace('freesrchabstract','srchabstract');
	    //var url_string = '/Xplore/login.jsp?url='+ encodeURI(location_url);
	    //var url_string = '/Xplore/login.jsp?url='+ location_url;
	    //By Swati, added fromgateway to the url to send it login.jsp correctly from searchabstract page
	    var url_string = '/Xplore/login.jsp?url='+ location_url+'&fromGateway=true';
	    window.location = encodeURI(url_string);
	}
	
	function checkFormSubmit()
	{
	   if( (document.forms.loginForm.username.value.length > 0) && (document.forms.loginForm.password.value.length > 0) )
	   {
	       return true;
	   } 
	   else
	   {   
	       alert("Please enter username and password.")
	       return false;       
	   }
	   //return ( (document.forms.frm1.id.value.length > 0) && (document.forms.frm1.password.value.length > 0) );
	}
	
	function goToIndexTerms( )
	{
	    hideTabs( );
	    j$( 'IndexTerms' ).show( );
	    j$( 'IndexTab' ).addClassName( 'selected' );
	}
	
	function goToReferences( )
	{
	    hideTabs( );
		j$( 'References' ).show( );
	    j$( 'ReferenceTab' ).addClassName( 'selected' );
	}
	
	function goToCitations( )
	{
	   hideTabs( );
	   j$( 'Citations' ).show( );
	   j$( 'CitationTab' ).addClassName( 'selected' );
	}
	
	function goToStandardVersions( )
	{
		hideTabs( );
		j$( 'StandardVersions' ).show( );
		j$( 'StandardTab' ).addClassName( 'selected' );
	}
	
	function goToDictionaryTerms( )
	{
		hideTabs( );
		j$( 'DictionaryTerms' ).show( );
		j$( 'DictionaryTab' ).addClassName( 'selected' );
	}
	
	function hideTabs( )
	{
		j$( 'IndexTerms' ).hide( );
		j$( 'IndexTab' ).removeClassName( 'selected' );
	
		
	
		
		
		
	}
	
	</script>	
	<meta property="og:type" content="website" />
	<meta property="og:title" content="On the use of windows for harmonic analysis with the discrete Fourier transform" />
	
	<meta property="og:description" content="This paper makes available a concise review of data windows and their affect on the detection of harmonic signals in the presence of broad-band noise, and in the presence of nearby strong harmonic interference. We also call attention to a number of c..."/>	
	<meta property="og:url" content="http://ieeexplore.ieee.org/xpl/articleDetails.jsp?reload=true&arnumber=1455106" />
	<meta property="og:image" content="http://ieeexplore.ieee.org/assets/img/logo-ieee-200x200.png" />
	<meta property="og:site_name" content="IEEE Xplore" />
	<meta property="fb:app_id" content="179657148834307" />


	        <!--				Ads By DART		-->
			
			
									
			
									
			
			
				  					  
			
									
			<script type='text/javascript'>					
				GS_googleAddAdSenseService("ca-pub-7515522322310000");
				GS_googleEnableAllServices();
			</script>
									
			<script language="JavaScript">
				GA_googleAddAttr("usertype", "inst"); 
			</script>
									
			<script type='text/javascript'>
				GA_googleAddSlot("ca-pub-7515522322310000", "xplore_subscription_leadgen");
			</script>
									
			<script type='text/javascript'>
				GA_googleFetchAds();
			</script>
			<!-- Google meta-tags -->
			
			  <meta name="citation_journal_title" content="Proceedings of the IEEE">
			
			
			<meta name="citation_publisher" content="IEEE">
			
			
				
				  <meta name="citation_author" content="Harris, F.J.">
				  
				    <meta name="citation_author_institution" content="Naval Ocean Systems Center, San Diego, CA">
				  
				
			
			<meta name="citation_title" content="On the use of windows for harmonic analysis with the discrete Fourier transform">
			<meta name="citation_date" content="Jan. 1978">
			<meta name="citation_volume" content="66">
			<meta name="citation_issue" content="1">
			<meta name="citation_firstpage" content="51">
			<meta name="citation_lastpage" content="83">
			<meta name="citation_doi" content="10.1109/PROC.1978.10837">
			<meta name="citation_abstract_html_url" content="http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=1455106' escapeXml='false'/>">
			<meta name="citation_pdf_url" content="http://ieeexplore.ieee.org/iel5/5/31261/01455106.pdf?arnumber=1455106">
			<meta name="citation_issn" content="0018-9219">
			<meta name="citation_isbn" content="">
			<meta name="citation_language" content="English">
			<meta name="citation_keywords" content="
			Discrete Fourier transforms;
			Fourier transforms;
			Frequency;
			Harmonic analysis;
			Oceans;
			Parameter estimation;
			Signal processing;
			Signal resolution;
			Signal sampling;
			Smoothing methods;">
						




 
			



<script>

function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}

j$('document').ready(function(){
  if(getCookie('legacyUserName')!=null)
  {
	  if(IBP_WS_ENABLED_FLAG){
	  	Modal.refreshLegacyAccountTransition('/xpl/mwLegacyAccountTransition.jsp');
	  }
  }
});

</script>

	
	<!--Begin Optional Configuration-->
	<script type="text/javascript" src='https://www.ieee.org/ieee-mashup/js/common/jquery.json-2.2.min.js'></script>
	<script type="text/javascript" src="https://www.ieee.org/ieee-mashup/js/common/postmessage.js" ></script>
	<script type="text/javascript" src='https://www.ieee.org/ieee-mashup/js/common/jquery.cookie.js'></script>
	<script type="text/javascript" src="https://www.ieee.org/ieee-mashup/js/auth/ieee-auth-constants.js"></script>
	<script type="text/javascript" src="https://www.ieee.org/ieee-mashup/js/auth/ieee-auth-include.js" ></script>
	
	<!--End Optional Configuration-->

<script type="text/javascript" src="http://s7.addthis.com/js/250/addthis_widget.js#pubid=ra-5005a435228f9245"></script>


		</div>
		<!-- IE7 Sniffer and Message -->
<style type="text/css" media="screen, print">
	@import url(/assets/css/ie7Sniffer.css);
</style>
<script type="text/javascript" src="/assets/js/IE7Sniffer.js"></script>
		
		<!-- END: FooterWrapper -->
			
			
      <!-- END: FooterWrapper -->
	</div>
  </body>
</html>



"""





	

'''
Funkcia, ktora splna zakladne vyhladavanie pomocou sluzby CiteSeerX
@param:keyword - vyhladavacia fraza
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
	html_file=html_doc	
	#parsujem ziskany html_file
	soup = BeautifulSoup(html_file)
	
   ''' spravne extrakcia '''
	url="http://www.utexas.edu/world/univ/alpha/"
	page=urllib2.urlopen(url)
	soup = BeautifulSoup(page.read())
	universities=soup.findAll('a',{'class':'institution'})
	for eachuniversity in universities:
	print eachuniversity['href']+","+eachuniversity.string
''' '''



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


		

        
print authordiv
sys.exit(0)
