import sys
import requests

if __name__ == "__main__":
    print sys.argv

parsed_names = []
for word in sys.argv[1:]:
    if word[-1] != ";":
        parsed_names.append(word)
    else:
        word = word[:-1]
        parsed_names.append(word)
        output = "+".join(parsed_names)
        r = requests.get("http://www.imdb.com/find?ref_=nv_sr_fn&q=" + output + "&s=all")
        text = r.text.encode('utf-8', 'ignore')
        print r.url
        parsed_names = []
