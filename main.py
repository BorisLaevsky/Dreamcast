import sys
import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    
    print sys.argv
    
    list_of_actors_urls = []
    output = ""
    for word in sys.argv[1:]:
        if word[-1] != ";":
            output += word + "+"
        else:
            output += word[:-1] + "+"
            r = requests.get("http://www.imdb.com/find?ref_=nv_sr_fn&q=" + output[:-1] + "&s=all") 
	    print r.url 
	    soup = BeautifulSoup(r.text, "html.parser")
            link = soup.find(attrs = {'class': 'findResult odd'}).find('a').get('href') 
            list_of_actors_urls.append("http://www.imdb.com" + str(link)) 
            output = ""
    
    print list_of_actors_urls
        
    for url in list_of_actors_urls:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")    
        links = soup.find(attrs = {'class': 'filmo-category-section'}).find_all('b')
	for link in links:
	    print link.get_text(';', strip = True)
        
       
