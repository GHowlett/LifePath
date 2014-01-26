# startup weekend euro, 1/25/2014, seattle, wa
# life path
# designed by cj sperber

import sys
import re
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


def getLinkedInUris(startRec=0):
    r = br.open('https://www.google.com/search?q=site%3Awww.linkedin.com%2Fin&start=' + str(startRec))
    html = r.read()

    # Show the source:
    #print html or br.response().read()

    soup = BeautifulSoup(html)

    regex = ur"http://www.linkedin.com/in/[^&% ]*"

    allLinksFound = []

    for link in soup.find_all('a'):
        theLink = link.get('href')
        #print theLink
        if len(theLink) > 1:
            #print "Link = " + theLink
            linksFound = re.findall(regex, theLink)
            if len(linksFound) > 0:
                #print "Link = " + theLink
                if linksFound[0] not in allLinksFound:
                    allLinksFound.append(linksFound[0])

    return allLinksFound


def getLinkedInUrisByLoopsOfTen(loopsOfTen=10, debug=False):
    if debug == True:
        sys.stderr.write("Starting; scraping LinkedIn URIs ...\n")
    for i in xrange(0, loopsOfTen):
        uris = getLinkedInUris(i*10)
        for uri in uris:
            print uri

        # delay
        sleepSecs = randint(3,9)
        if debug == True:
            sys.stderr.write("Loop %d, Delaying ... %s\n" % (i, str(sleepSecs)))
        sleep(sleepSecs)

getLinkedInUrisByLoopsOfTen(100, True)