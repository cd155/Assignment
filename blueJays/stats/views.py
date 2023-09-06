import requests
from xml.etree import ElementTree
from django.shortcuts import render

def home(request):
    news_feeds = requests.get('https://www.mlb.com/feeds/news/rss.xml')
    tree = ElementTree.fromstring(news_feeds.content)

    news_lst = []

    # the current setting only show four news feeds
    i = 0
    for item in tree[0].findall('item'):
        if i>3: break
        news_dict = {
            'title': item.find('title').text,
            'link': item.find('link').text,
            'date': item.find('pubDate').text[0:16],
            'creator': item.find("{http://purl.org/dc/elements/1.1/}creator").text,
            'image_url': item.find('image').attrib['href'],
        }
        news_lst.append(news_dict)
        i+=1

    return render(request, 'index.html', {'board_n': range(0,3),
                                          'news_lst': news_lst})


 

def team(request, pk):
    return render(request, 'team.html', {})


def player(request, pk):
    return render(request, 'player.html', {})
