import sys
import requests

if __name__ == "__main__":
    print sys.argv
for i in range(1,len(sys.argv), 2):
    r = requests.get("http://www.imdb.com/find?ref_=nv_sr_fn&q=" + sys.argv[i] + "+" + sys.argv[i+1] + "&s=all")
#test
