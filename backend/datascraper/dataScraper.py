import sys
import re
from urllib2 import Request, urlopen
import urllib
from bs4 import BeautifulSoup

def grabLinkedInData(uri = '', queryString = ''):
    constructedUri = uri % urllib.quote_plus(queryString)

    req_google = Request(constructedUri)
    req_google.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB;    rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')

    html_google = urlopen(req_google).read()

    soup = BeautifulSoup(html_google)

    regex = ur"http://www.linkedin.com/in/[^&%]*"

    for link in soup.find_all('a'):
        theLink = link.get('href')
        if len(theLink) > 1:
            #print "Link = " + theLink
            linksFound = re.findall(regex, theLink)
            if len(linksFound) > 0:
                #print "Link = " + theLink
                print linksFound

grabLinkedInData('http://www.google.com/search?q=%s', 'site:www.linkedin.com/in')