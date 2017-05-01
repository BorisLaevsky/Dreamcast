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
            text = r.text
	    print r.url
	    soup = BeautifulSoup(text, "html.parser")
	    items = soup.find_all(attrs={'class': 'findResult odd'})   
            link = items[0].find_all('a')
            actor_url = link[0].get('href')
            list_of_actors_urls.append(str("http://www.imdb.com" + actor_url))
            
            output = ""
    print list_of_actors_urls
        
        


