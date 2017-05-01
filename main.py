import sys
import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    
    print sys.argv
    temp_list = []
    list_of_actors_urls = []
    output = ""
    for word in sys.argv[1:]:
        if word[-1] != ";":
            output += word + "+"
        else:
            output += word[:-1] + "+"
            r = requests.get("http://www.imdb.com/find?ref_=nv_sr_fn&q=" + output[:-1] + "&s=all")
            text = r.text.encode('utf-8', 'ignore')
	    print r.url
	    soup = BeautifulSoup(text, "html.parser")
	    for item in soup.find_all(attrs={'class': 'findResult odd'}):
                for link in item.find_all('a'):
                    temp_list.append(link.get('href'))
            list_of_actors_urls.append(str("http://www.imdb.com" + temp_list[0]))
            temp_list = [] 
            output = ""
        print list_of_actors_urls
        
        


