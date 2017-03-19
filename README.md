# Jisho-karini

Basic access to the [Jisho API](http://jisho.org/forum/54fefc1f6e73340b1f160000-is-there-any-kind-of-search-api).

For personal use only. It is a really simple script, but it helps in case you
need to take a look at the best Japanese-English dictionary from the command
line.

## Requirements

It was tested only with Python 3 on Archlinux. Under _these_ conditions it
should just work, or else, open an issue. (:

## Featuring

* Search the Jisho API from the command line
* Open Jisho.org on the page you need from the command line
* If you use [Neovim's](http://neovim.io/) built in terminal... well, then you know.

## Unfeaturing

* Pretty dirty print (see below)
* Horrible code crafted by a nonprogrammer

## Commands

**-b** will open [Jisho.org](http://jisho.org/) showing the result of your
search:

```
$ python jisho-karini.py -b house
```

**-r** will access the Jisho API and print the result as in the example below:

```
$ python jisho-karini.py -r house

[{'word': '椅子', 'reading': 'いす'}, {'word': '倚子', 'reading': 'いす'}, {'reading': 'イス'}]
[{'english_definitions': ['chair', 'stool'], 'parts_of_speech': ['Noun'], 'links': [], 'tags': [], 'restrictions': [], 'see_al
so': [], 'antonyms': [], 'source': [], 'info': []}, {'english_definitions': ['post', 'office', 'position'], 'parts_of_speech':
 [], 'links': [], 'tags': [], 'restrictions': [], 'see_also': [], 'antonyms': [], 'source': [], 'info': []}, {'english_definit
ions': ['Chair'], 'parts_of_speech': ['Wikipedia definition'], 'links': [{'text': 'Read “Chair” on English Wikipedia', 'url':
'http://en.wikipedia.org/wiki/Chair?oldid=495544638'}, {'text': 'Read “椅子” on Japanese Wikipedia', 'url': 'http://ja.wikiped
ia.org/wiki/椅子?oldid=42406984'}], 'tags': [], 'restrictions': [], 'see_also': [], 'antonyms': [], 'source': [], 'info': [],
'sentences': []}]

[{'reading': 'チェア'}, {'reading': 'チェアー'}]
[{'english_definitions': ['chair'], 'parts_of_speech': ['Noun'], 'links': [], 'tags': [], 'restrictions': [], 'see_also': [],
'antonyms': [], 'source': [], 'info': []}]
```

**-j** the same as above but there will be line breaks in instead of long lines:

```
$ python jisho-karini.py -j house

[ {'reading': 'いす', 'word': '椅子'},
  {'reading': 'いす', 'word': '倚子'},
  {'reading': 'イス'}]
[ { 'antonyms': [],
    'english_definitions': ['chair', 'stool'],
    'info': [],
    'links': [],
    'parts_of_speech': ['Noun'],
    'restrictions': [],
    'see_also': [],
    'source': [],
    'tags': []},
  { 'antonyms': [],
    'english_definitions': ['post', 'office', 'position'],
    'info': [],
    'links': [],
    'parts_of_speech': [],
    'restrictions': [],
    'see_also': [],
    'source': [],
    'tags': []},
  { 'antonyms': [],
    'english_definitions': ['Chair'],
    'info': [],
    'links': [ { 'text': 'Read “Chair” on English Wikipedia',
                 'url': 'http://en.wikipedia.org/wiki/Chair?oldid=495544638'},
               { 'text': 'Read “椅子” on Japanese Wikipedia',
                 'url': 'http://ja.wikipedia.org/wiki/椅子?oldid=42406984'}],
    'parts_of_speech': ['Wikipedia definition'],
    'restrictions': [],
    'see_also': [],
    'sentences': [],
    'source': [],
    'tags': []}]


[{'reading': 'チェア'}, {'reading': 'チェアー'}]
[ { 'antonyms': [],
    'english_definitions': ['chair'],
    'info': [],
    'links': [],
    'parts_of_speech': ['Noun'],
    'restrictions': [],
    'see_also': [],
    'source': [],
    'tags': []}]

```

## Credits and licences

Jisho.org rocks. Period.
If you wanna know more about the content, its licences, where does it come from
etc, it is as easy as taking a look at [Jisho's about
page](http://jisho.org/about).

## Support

I doubt someone is going to use it, but if you do, just keep two things in mind:

* [ ] do **not** bother Jisho's team with any problem created by
  `lsrdg/jisho-karini` (:
* [ ] it will be a pleasure to listen your feedback and help you out o/
