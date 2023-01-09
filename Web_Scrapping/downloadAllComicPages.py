import os, bs4, requests


url = 'https://xkcd.com'
os.makedirs('xkcd' , exist_ok = True)
while not url.endswith('#'):
    print('Downloaing page %s.....'%(url))
    res = requests.get(url)
    res.raise_for_status()
    
    
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    
    comic_elem = soup.select('#comic img')
    if comic_elem == []:
        print("Could not find comic image.")
    else:
        comic_url = 'https:' + comic_elem[0].get('src')
        
        print("downloading the image for %s"%comic_url)
        res = requests.get(comic_url) 
        res.raise_for_status()
        
        
        image_file = open(os.path.join("xkcd",os.path.basename(comic_url)),'wb')
        
        for chunk in res.iter_content(10000000):
            image_file.write(chunk)
        image_file.close()
    prev = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com'+prev.get('href')
        
print("Done") 
        