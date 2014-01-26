# startup weekend euro, 1/26/2014, seattle, wa
# life path
# designed by cj sperber

import sys
import re
import json
from time import sleep
from random import randint
import mechanize
import cookielib
from bs4 import BeautifulSoup


# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(False)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

#br.set_debug_http(True)
#br.set_debug_redirects(True)
#br.set_debug_responses(True)

br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]


def htmlFromFilename(filename):
    with open(filename, "r") as fp:    
        data = fp.read()

    return data


def strWoSpaces(str):
    return " ".join(str.strip().split()).encode('utf-8')


def scrapeLinkedInProfile(uri, idUri):
    r = br.open(uri)
    html = r.read()

    soup = BeautifulSoup(html)

    experiences = soup.find_all("div", "experience")
    #print experiences[0]

    orgs = soup.find_all("p", "orgstats")
    #print orgs[0]

    sdates = soup.find_all("abbr", "dtstart")
    #print sdates[0]

    edates1 = soup.find_all("abbr", "dtstamp")
    edates2 = soup.find_all("abbr", "dtend")
    edates = edates1 + edates2

    descs = soup.find_all("p", "description") # start at pos 1

    linkedInRecs = []

    ctr = 0
    while True:
        try:
            """
            print strWoSpaces(experiences[ctr].find("span", "title").get_text())
            print strWoSpaces(experiences[ctr].find("span", "summary").get_text())
            print strWoSpaces(orgs[ctr].get_text())
            print strWoSpaces(descs[ctr+1].get_text())
            print strWoSpaces(sdates[ctr].get("title"))
            print strWoSpaces(edates[ctr].get("title"))
            print "---"
            """

            rec = {}

            rec["userid"] = idUri
            rec["type"] = "j"
            rec["name"] = strWoSpaces(experiences[ctr].find("span", "summary").get_text())
            rec["title"] = strWoSpaces(experiences[ctr].find("span", "title").get_text())
            rec["industry"] = strWoSpaces(orgs[ctr].get_text())
            rec["desc"] = strWoSpaces(descs[ctr+1].get_text())
            rec["start"]  = strWoSpaces(sdates[ctr].get("title"))
            rec["end"] = strWoSpaces(edates[ctr].get("title"))

            linkedInRecs.append(rec)

            ctr += 1
        except:
            break

    unis = soup.find_all("h3", "summary fn org")
    #print unis

    degrees = soup.find_all("span", "degree")
    majors = soup.find_all("span", "major")

    ctr = 0
    while True:
        try:
            """
            print strWoSpaces(unis[ctr].get_text())
            print strWoSpaces(degrees[ctr].get_text())
            print strWoSpaces(majors[ctr].get_text())
            """

            rec = {}

            rec["userid"] = idUri
            rec["type"] = "e"
            rec["name"] = strWoSpaces(unis[ctr].get_text())
            rec["title"] = strWoSpaces(degrees[ctr].get_text())
            rec["industry"] = strWoSpaces(majors[ctr].get_text())
            rec["desc"] = ""
            rec["start"]  = ""
            rec["end"] = ""

            linkedInRecs.append(rec)

            ctr += 1
        except:
            break

    return linkedInRecs


def getLinkedInProfiles(input_filename, output_filename, debug=False):
    if debug == True:
        sys.stderr.write("Starting; scraping LinkedIn URIs ...\n")

    append_fp = open(output_filename, "a")

    with open(input_filename, "r") as input_fp:
        while True:
            try:
                idUri = strWoSpaces(input_fp.readline())
                print idUri
            except:
                continue

            if not idUri:
                break

            jsonRec = json.dumps(scrapeLinkedInProfile("https://www.linkedin.com/in/" + idUri, idUri))

            if jsonRec:
                append_fp.write(jsonRec)
                append_fp.write(",\n")

            #print jsonRec

            # delay
            sleepSecs = randint(3,9)
            if debug == True:
                sys.stderr.write("Delaying ... %s\n" % str(sleepSecs))
            sleep(sleepSecs)

    append_fp.close()

#print json.dumps(scrapeLinkedInProfile("https://www.linkedin.com/in/billgates", "billgates"))
#print json.dumps(scrapeLinkedInProfile("https://www.linkedin.com/in/csperber", "csperber"))

if __name__ == "__main__":
    getLinkedInProfiles(sys.argv[1], "linkedin-data.txt", True)