'''
PURPOSE
I want to
 - verify that I have the most recent file from a remote site.
 - Download the file only if necessary
 - Use as little network traffic as possible.

SOLUTION REQUIRES 
Webserver that is configured to honour the http header If-Modified-Since


https://stackoverflow.com/questions/15207145/detect-if-a-web-page-is-changed
'''

import urllib2

def print_header(headers, h):
    print('{:<20}{:<20}{}'.format('http-header', h, headers[h]))
    
def url_change():
    url = 'https://www.eff.org/pages/legal-assistance'
    last_date = 'Sat, 29 Oct 1994 19:43:31 GMT'       # Content weil zu alt
    last_date = 'Tue, 08 Aug 2017 19:38:12 GMT'       # Content weil 1 Sek zu alt
    last_date = 'Tue, 08 Aug 2017 19:38:13 GMT'       # Kein Content weil das ist das Alter

    request = urllib2.Request(url)
    request.add_header("If-Modified-Since", last_date)
    try:
        response = urllib2.urlopen(request)           # Make the request
        ###print(dir(response))           # show methods
        headers = response.headers
        ###print(dir(headers))            # show methods
        ###print(headers.keys())
        print_header(headers, 'last-modified')
        # For the non believers
        print_header(headers, 'content-length')
        content = response.read()
        print('{:<40}{}'.format('Content length counted by Python', len(content)))
    except urllib2.HTTPError, err:
        if err.code == 304:
            print "You are up to date"
        else:
            print "Error code:", err.code 
            pass


url_change()
