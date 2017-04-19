import sys
import requests

if __name__ == "__main__":
    print sys.argv

output = ""
for word in sys.argv[1:]:
    if word[-1] != ";":
        output += word + "+"
    else:
        output += word[:-1] + "+"
        r = requests.get("http://www.imdb.com/find?ref_=nv_sr_fn&q=" + output[:-1] + "&s=all")
        text = r.text.encode('utf-8', 'ignore')
        print text
        output = ""
