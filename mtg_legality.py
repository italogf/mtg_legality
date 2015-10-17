from json import loads
from re import sub
from sys import argv
from urllib2 import Request, urlopen, URLError
from pprint import pprint

url = "https://api.deckbrew.com/mtg/cards"

card = str(argv[1])
data = {}
data['name'] = card

url_value = card.replace(' ', '-').lower()
#url_value = urllib.urlencode(data)
specials = "[:,'?!()]"
removeSpecials = sub(specials, '', url_value)

url_complete = url + '/' + removeSpecials
print url_complete + "\n"
request = Request(url_complete)

try:
	response = urlopen(request)

	card_desc = response.read()
	#print card_desc
	response = loads(card_desc)
	#pprint(data["formats"])
	for item, value in response['formats'].items():
		print item, value

except URLError, e:
	print 'Nao vou possivel pegar a legalidade da carta'

