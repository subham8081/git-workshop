from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags=soup('a')
#x=0
#ans=list()
for tag in tags:
    print("value :   ",tag.contents[0])
    print("\nlinks: ", tag.get("href",None))
    #ans.append(int(tag.contents[0]))
    #x=x+1
#print("sum: ",sum(ans))
