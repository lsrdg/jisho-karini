import requests, argparse, json

parser = argparse.ArgumentParser()

parser.add_argument("-j", help="Open a browser and show the result", nargs=1)
args = parser.parse_args()

argJ = args.j[0] + '\"'

def fetching():
    url = 'http://jisho.org/api/v1/search/words?keyword=\"' + argJ
    response = requests.get(url,)
    response.raise_for_status()
    termData = json.loads(response.text)
    t = termData['data']
    td = t[0]

    tr = td['senses'] 
    eng = tr[0]
    print(td['japanese'])
    print(eng['english_definitions'])

if args.j:
    fetching()
