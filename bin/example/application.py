#!/usr/bin/env python

import sys
from scholar import BasicSearch
from scholar import ExtendedSearch
from citeseerx import extendedSearch
from citeseerx import basicSearch

from optparse import OptionParser
import codecs

usage = "usage: %prog [options] arg"
parser = OptionParser(usage)


parser.add_option("--engine", dest="engine",
                  help="Type of searching engine google=scholar, citeseerx=citeseerx",
                  type="string", metavar="ENGINE")

parser.add_option("--type", dest="type",
                  help="Type of search to use  BASIC or EXTENDED",
                  type="string", metavar="BASIC|EXTENDED")


parser.add_option("--phrase", dest="phrase",
                  help="Phrase we would like to search",
                  type="string", metavar="PHRASE")


parser.add_option("--output", dest="filename",
                  help="File to write report=stdout|filename",default="stdout", metavar="FILE")


parser.add_option("--sort", dest="sort",
                  help="Type of sort for CiteSeeX", type="int", metavar="NUM")


parser.add_option("--citation", dest="citation",
                  help="Include citation for CiteSeeX False=NotInclude True=Include",
                  type="string", metavar="Bool")

parser.add_option("--title", dest="title",
                  help="Title for search for extend search CiteSeerX",
                  type="string", metavar="TITLE")

parser.add_option("--author", dest="author",
                  help="Include autor in extend search CiteSeerX|GoogleScholar",
                  type="string", metavar="Name")

parser.add_option("--authoraffi", dest="authoraffi",
                  help="Include author affiliation in extend search CiteSeerX",
                  type="string", metavar="AFFI")

parser.add_option("--publicvenue", dest="publicvenue",
                  help="Include public venue in extend search CiteSeerX|GoogleScholar",
                  type="string", metavar="VENUE")

parser.add_option("--keywords", dest="keywords",
                  help="Include keywords in extend search CiteSeerX",
                  type="string", metavar="KEYWORDS")

parser.add_option("--abstract", dest="abstract",
                  help="Include name of abstract in extend search CiteSeerX",
                  type="string", metavar="ABST")

parser.add_option("--mincitations", dest="mincitations",
                  help="Include minimal number of citations in extend search CiteSeerX",
                  type="int", metavar="NUM")

parser.add_option("--startyear", dest="startyear",
                  help="Include results from startyear in extend search CiteSeerX|StartYear",
                  type="int", metavar="YEAR")

parser.add_option("--endyear", dest="endyear",
                  help="Include results from endyear in extend search CiteSeerX|GoogleScholar",
                  type="int", metavar="YEAR")

parser.add_option("--withcorrectphrase", dest="withcorrectphrase",
                  help="Include in results withcorrectphrase in extend search GoogleScholar",
                  type="string", metavar="PHRASE")

parser.add_option("--withoutwords", dest="withoutwords",
                  help="DO not include in results withoutwords in extend search GoogleScholar",
                  type="string", metavar="PHRASE")

parser.add_option("--leastoneword", dest="leastoneword",
                  help="Include in results leastoneword in extend search GoogleScholar",
                  type="string", metavar="PHRASE")

parser.add_option("--occurence", dest="occurence",
                  help="Search in occurence in title = 1| in hole article=2 in extend search GoogleScholar",
                  type="string", metavar="1|2")

parser.add_option("--format", dest="format",
                  help="format results=NEWLINE|TAB", type="string",
                  metavar="FORM")

(options, args) = parser.parse_args()


if (len(sys.argv) < 6):
    print "Nedostatocny pocet parametrov"
    sys.exit(1)

if (options.engine != "scholar" and options.engine != "citeseerx"):
    print "Neznamy vyhladavaci engine"
    sys.exit(1)

if (options.format != "TAB" and options.format != "NEWLINE"):
    print "Neznamy typ formatovania"
    sys.exit(1)

options.filename = str(options.filename)
options.engine = str(options.engine)
options.type = str(options.type)
options.format = str(options.format)
options.phrase = str(options.phrase)


options.leastoneword = str(options.leastoneword)
options.withoutwords = str(options.withoutwords)


options.abstract = str(options.abstract)
options.keywords = str(options.keywords)
options.authoraffi = str(options.authoraffi)
options.author = str(options.author)
options.title = str(options.title)
options.citation = str(options.citation)

options.publicvenue = str(options.publicvenue)

if (options.leastoneword == "None"):
    options.leastoneword = False

if (options.withoutwords == "None"):
    options.withoutwords = False


if (options.abstract == "None"):
    options.abstract = False

if (options.authoraffi == "None"):
    options.authoraffi = False

if (options.author == "None"):
    options.author = False

if (options.title == "None"):
    options.title = False

if (options.publicvenue == "None"):
    options.publicvenue=False


if (options.engine == "citeseerX" and options.citation == "None"):
    print "Pre sluzby citeseerx neboli zadane citacie"
    sys.exit(1)

if (options.engine != "scholar" and options.engine != "citeseerx"):
    print "Neznamy vyhladavaci engine"
    sys.exit(1)


pom1 = str(options.endyear)
pom2 = str(options.startyear)
pom3 = str(options.mincitations)
pom4 = str(options.occurence)
pom5 = str(options.sort)
Year = False
zoznam = []

options.citation = str(options.citation)
if (options.engine == "citeseerx" and options.citation == "False"):
    options.citation = False
elif (options.engine == "citeseerx" and options.citation == "True"):
    options.citation = True



if (pom1 != "None" and pom2 != "None"):
    Year = True
    zoznam.append(options.startyear)
    zoznam.append(options.endyear)
else:
    Year = False

if (pom3 == "None"):
    options.mincitations = False

if (options.engine == "scholar" and options.type == "EXTENDED" and pom4 == "None"):
    print "Chyba pre Google Scholar rozsirene vyhladavanie nebol zadane vyskyt"
    sys.exit(1)

if (options.engine == "citeseersx" and options.type == "EXTENDED" and pom5 == "None"):
    print "Chyba pre sluzby citeseerx  rozsirene vyhladavanie, nebol zadany sort"
    sys.exit(1)

slovnik = dict()
if (options.type != "EXTENDED" and options.type != "BASIC"):
    print "Neznamy typ vyhladavania ani zakladne ani rozsirene"
    sys.exit(1)

if (options.engine == "scholar"):
    if (options.type == "BASIC"):
        try:
            slovnik = BasicSearch(options.phrase)
        except ValueError:
            print "Chybna hodnota vstupnych parametrov"
            sys.exit(1)
        except Exception:
            "Chyba pri pripajani/chyba v typoch parametrov"
            sys.exit(1)
    else:
        
        options.occurence = int(options.occurence)
        try:
            slovnik = ExtendedSearch(
                options.phrase,options.withcorrectphrase, options.leastoneword, options.withoutwords,
                options.occurence, options.author,
                options.publicvenue, int(zoznam[0]), int(zoznam[1]))
        except ValueError:
            print "Chybna hodnota vstupnych parametrov"
            sys.exit(1)
        except Exception:
            "Chyba pri pripajani/chyba v typoch parametrov"
            sys.exit(1)
elif (options.engine == "citeseerx"):
    if (options.type == "BASIC"):
        try:
            slovnik = basicSearch(options.phrase, options.citation, options.sort)
        except ValueError:
            print "Chybna hodnota vstupnych parametrov"
            sys.exit(1)
        except Exception:
            "Chyba pri pripajani/chyba v typoch parametrov"
            sys.exit(1)
    else:
        try:
            slovnik = extendedSearch(
                options.phrase, options.title, options.author,
                options.authoraffi, options.publicvenue,
                options.keywords, options.abstract, 
                Year, zoznam,  options.mincitations,options.citation, options.sort)
        except ValueError:
            print "Chybna hodnota vstupnych parametrov"
            sys.exit(1)
        except Exception:
            "Chyba pri pripajani/chyba v typoch parametrov"
            sys.exit(1)

if (options.filename == "stdout"):
    pocet_poloziek = 0

    if (options.engine == "citeseerx"):
        if (options.citation is False):
            pocet_poloziek = 10
        else:
            pocet_poloziek = 11
    else:
        pocet_poloziek = 8
    for i in range(1, len(slovnik) + 1):
        sys.stdout.write(str(i))
        sys.stdout.write(": ")
        for h in range(0, pocet_poloziek - 1):
            sys.stdout.write(slovnik[i][h])
            sys.stdout.write("#")
        if (options.format == "TAB"):
            sys.stdout.write("\t")
        if (options.format == "NEWLINE"):
            sys.stdout.write("\n")


else:
    f = codecs.open(options.filename, 'w', 'utf-8')
    pocet_poloziek = 0
    
    if (options.engine == "citeseerx"):
        if (options.citation is False):
            pocet_poloziek = 10
        else:
            pocet_poloziek = 11
    else:
        pocet_poloziek = 8
    for i in range(1, len(slovnik) + 1):
        f.write(str(i))
        f.write(": ")
        for h in range(0, pocet_poloziek - 1):
            f.write(slovnik[i][h])
            f.write("#")
        if (options.format == "TAB"):
            f.write("\t")
        if (options.format == "NEWLINE"):
            f.write("\n")
    f.close()
sys.exit(0)
