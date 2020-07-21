import sys
import re
import urllib.request

#looks for profile id in https://www.instagram.com/username/?__a=1 to generate rss feed link

bridgeip = "Bridge.IP.Goes.here"

# input arguement is instagram username
uname = sys.argv[1]

# fetch the url and run the hacky parser to get the profileid
url = 'https://www.instagram.com/' + uname + '/?__a=1'
html = urllib.request.urlopen(url)
doc = html.read().decode()
parts = doc.split(",")
for each in parts:
    if re.search(r'profilePage', each):
        tags  = each.split(":")
for item in tags:
    if re.search(r'profilePage', item):
        urlparts = item.split("_")
profileid = urlparts[1][:-1]

# assmeble the parts for an atom feed and print it out
feedurl = "http://" + bridgeip + "/rss-bridge/?action=display&bridge=Instagram&context=Username&u=" + profileid + "&media_type=all&format=Atom"
print (feedurl)
