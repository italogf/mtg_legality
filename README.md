# mtg_legality

Simple Python script to show legality of mtg cards using https://deckbrew.com/api/

## Python 2
### usage:

```shell
[user:~/mtg_legality]$ python mtg_legality.py "Aboshan's Desire"
```
### output:
  https://api.deckbrew.com/mtg/cards/aboshans-desire
  vintage legal
  legacy legal
  commander legal


## Python 3
### usage:

```shell
[user:~/mtg_legality]$ python mtg_legality.py "Aboshan's Desire"
```
Or, if the card name is omitted, it'll get the card names from cards.txt file (1 card name per line)

```shell
[user:~/mtg_legality]$ python mtg_legality.py
```

### output:
```shell
lightning bolt
  legacy legal
  vintage legal
  modern legal
  commander legal

brainstorm
  legacy legal
  vintage restricted***
  commander legal

force of nature
  legacy legal
  vintage legal
  modern legal
  commander legal

