import requests, argparse, json, webbrowser

parser = argparse.ArgumentParser()

parser.add_argument("-j", help="Open a browser and show the result", nargs=1)
parser.add_argument("-b", help="Open a browser and show the result", nargs=1)
args = parser.parse_args()



def fetching():
    argJ = args.j[0] + '\"'
    url = 'http://jisho.org/api/v1/search/words?keyword=\"' + argJ
    response = requests.get(url)
    response.raise_for_status()
    termData = json.loads(response.text)
    t = termData['data']

    for item in t:
        
        print(item['japanese'])
        print(item['senses'], '\n')

# ------- print [0]
#    td = t[0]
#
#    tr = td['senses'] 
#    eng = tr[0]
#    print(td['japanese'])
#    print(eng['english_definitions'])

def browser():
    argB = args.b[0]
    webbrowser.open('http://jisho.org/search/' + argB, new=2)

def menuInit():
    if args.j:
        fetching()

    elif args.b:
        browser()

    else:
        print("Oooops!")

menuInit()
