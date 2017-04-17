import sys
import requests

if __name__ == "__main__":
    print sys.argv

parsed_names = []
for word in sys.argv[1:]:
    if word[-1] != ";":
        parsed_names.append(word)
    else:
        word = word.replace(";", "")
        parsed_names.append(word)
        output = reduce( lambda x, y: x + "+" + y, parsed_names )
        r = requests.get("http://www.imdb.com/find?ref_=nv_sr_fn&q=" + output + "&s=all")
        print r.url
        output = []
        parsed_names = []
