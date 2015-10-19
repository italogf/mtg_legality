#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
from re import sub
from sys import argv, exit
from urllib import request, error

url = "https://api.deckbrew.com/mtg/cards"
cards_file = "cards.txt"

def show_legality(card):
  url_value = card.replace(' ', '-').lower()
  specials = "[:,'?!()]"
  removeSpecials = sub(specials, '', url_value)

  url_complete = url + '/' + removeSpecials

  print (card.strip())

  req = request.Request(url_complete)

  try:
    response = request.urlopen(req)

  except error.HTTPError as e:
    print (e.reason +" "+ card)

  except error.URLError as e:
    print (e.reason)

  else:
    card_desc = response.read().decode('utf-8')
    response = json.loads(card_desc)

    for item, value in response['formats'].items():
      print ("  "+ item, value if value == "legal" else value +"***")

  print()

def cards_from_file():
  try:
    f = open(cards_file, "r")
    for line in f:
      show_legality(line)
    f.close()
  except:
    print("Card name and cards.txt file missing")
    exit()

def card_from_cmd():
  card = str(argv[1])
  show_legality(card)

def init():
  if not len(argv) == 2:
    cards_from_file()
  else:
    card_from_cmd()

init()