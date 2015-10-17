from json import loads
from re import sub
from sys import argv
from urllib2 import Request, urlopen, URLError

url = "https://api.deckbrew.com/mtg/cards"
card = str(argv[1])

url_value = card.replace(' ', '-').lower()
specials = "[:,'?!()]"
removeSpecials = sub(specials, '', url_value)

url_complete = url + '/' + removeSpecials

print url_complete + "\n"

request = Request(url_complete)

try:
	response = urlopen(request)
	card_desc = response.read()
	response = loads(card_desc)

	for item, value in response['formats'].items():
		print item, value

except URLError, e:
	print 'Nao vou possivel pegar a legalidade da carta'
