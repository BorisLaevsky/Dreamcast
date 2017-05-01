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
            class_with_urls = soup.find(attrs = {'class': 'findResult odd'})
            link = class_with_urls.find('a').get('href')
            list_of_actors_urls.append(str("http://www.imdb.com" + link)) 
            output = ""
    
    print list_of_actors_urls
        
        


