from urllib.error import HTTPError
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import nltk
import re

url = input("page you want to check, pls enter url: ")
keyword = input("what is your SEO keyword? ")
keyword = keyword.casefold()
try:
    """
    req = Request(url, headers={'User-Agent':'Mozilla/.0'})
    html_data = urlopen(url=req)
    """
    html_data = urlopen(url=url)

except HTTPError as e:
    print(e)

data = BeautifulSoup(html_data, "html.parser")


def SEO_Title(keyword, data):
    if data.title:
        if keyword in data.title.text.casefold():
            status = "Found"
        else:
            status = "keyword Not Found"
    else:
        status = "No title Found"
    return status


def seo_title_stop_words(data):
    words = 0
    words_list = []
    if data.title:
        with open('stop_words.txt', 'r') as f:
            for line in f:
                if re.search(r'\b' + line.rstrip('\n') + r'\b', data.title.text.casefold()):
                    words += 1
                    words_list.append(line.rstrip('\n'))
            if words > 0:
                stop_words = "Found {} stop words, you should remove {} these.".format(words, words_list)
            else:
                stop_words = "No stop words found"
    else:
        stop_words = "No title Found"
    return stop_words


def seo_data_length(data):
    if data.title:
        if len(data.title.text) < 60:
            length = "it is following suggested length"
        else:
            length = "please check the length, it is {}".format(len(data.title.text))
    else:
        length = "Not found"
    return length


def seo_url(url):
    if url:
        if keyword in url:
            slug_word = "Your keyword was found"
        else:
            slug_word = "You keyword was not found"
    else:
        slug_word = "url not found"
    return slug_word


def seo_url_length(url):
    if url:
        if len(url) < 100:
            length = "you url is having suggested length, good work"
        else:
            length = "Your url length is not good you should have relook/change it, url lrngth is {}".format(len(url))
    else:
        length = "No url found"
    return length


def seo_h1(keyword, data):
    total_h1 = 0
    total_key = 0
    if data.h1:
        all_tags = data.find_all("h1")
        for tag in all_tags:
            tag = str(tag.string)
            total_h1 += 1
            if keyword in tag.casefold():
                total_key += 1
                h1_tag = "keyword found in h1 tag"
            else:
                h1_tag = "Didn't found h1 tag in keyword"
    else:
        h1_tag = "no h1 tags present"
    return h1_tag


def seo_h2(keyword, data):
    if data.h2:
        all_tags = data.find_all("h2")
        for tag in all_tags:
            tag = str(tag.string)
            if keyword in tag.casefold():
                h2_tag = "keyword found in h2 tag"
            else:
                h2_tag = "Didn't found h2 tag in keyword"
    else:
        h2_tag = "no h2 tags present"
    return h2_tag


print(SEO_Title(keyword, data))
print(seo_title_stop_words(data))
print(seo_data_length(data))
print(seo_url(url))
print(seo_url_length(url))
print(seo_h1(keyword, data))
print(seo_h2(keyword, data))
