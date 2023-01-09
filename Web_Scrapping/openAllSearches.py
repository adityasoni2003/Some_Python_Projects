import requests,sys,webbrowser,bs4,pyperclip


    
res = requests.get('https://pypi.org/search/?q=' +'+'.join(sys.argv[1:]) +'&o=')


soup = bs4.BeautifulSoup(res.text , 'html.parser')
linkElems = soup.select('.package_snippet')
print(linkElems.get('href'))

numOpen = min(5,len(linkElems))

for i in range(numOpen):
    UrlToOpen = "https://pypi.org" + linkElems[i].get('href')
    print('Opening ' +UrlToOpen)
    webbrowser.open(UrlToOpen)