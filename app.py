from urllib.error import HTTPError
from urllib.request import  urlopen
from bs4 import BeautifulSoup

url = input("page you want to check, pls enter url: ")
keyword = input("what is your SEO keyword? ")

try:
    html_data = urlopen(url=url)

except HTTPError as e:
    print(e)

data = BeautifulSoup(html_data,"html.parser")

def SEO_Title(keyword, data):
    if keyword.casefold() in data.title.text.casefold():
        status = "Found"
    else:
        status = "Not Found"
    return status
print(SEO_Title(keyword,data))