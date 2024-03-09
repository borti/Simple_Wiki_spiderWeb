import requests
from bs4 import BeautifulSoup

def findTitolo(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    # titoli = soup.find_all('h1')  # ottiene i titoli in sintassi <h1>nome titolo</h1>
    titoli = [titolo.text for titolo in soup.find_all('h1')]
    
    return titoli[0]

def spiderWiki(url):
    
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    # links -> lista dizionari contenente i link divisi in 'a' e 'href'
    links = [{'a': link.text, 'href': link.get('href')} for link in soup.find_all('a') if link.get('href') and link['href'].startswith('/wiki/')] # se il link href non è None e inizia con /wiki, estrai i link da tutti gli hypertext 'a'
    listLinkCompleti = ['https://it.wikipedia.org/wiki' + link['href'] for link in links if 'href' in link]

    
    count = 0
    for i in links:
        tit = findTitolo('https://it.wikipedia.org'+i['href'])
        if count < 31:
            print(f"{count}) titolo = {tit} | link = {i['href']}")
            count += 1
        if count>=31:
            break
    
    optSecondLink(links)

    
def optSecondLink(links):
    index = int(input("\nSeleziona l'indice del prossimo nodo: "))
    count = 0
    for i in links:
        if count == index:
            spiderWiki('https://it.wikipedia.org'+i['href'])
            break
        count +=1
        
    exit("ERRORE")


############ MAIN ############

url = input("inserire link di partenza : ")
spiderWiki(url)


        
        


