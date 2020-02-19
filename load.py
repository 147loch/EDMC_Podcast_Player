import listparser
import feedparser

import urllib.request
from time import sleep

from player import player


def plugin_start(plugin_dir):
    """
    Load this plugin into EDMC
    """
    print("I am loaded! My plugin folder is {}".format(plugin_dir.encode("utf-8")))
    available_podcasts = load_opml()
    print(available_podcasts)

    #rss_feed_url = 'http://laveradio.com/feed/laveradio.xml'
    save_file = 'downloads/FISH Lave Radio Spot.mp3'
    #download_audio(rss_feed_url, 0, save_file)
    play_audio(save_file)
    return "Test"


def load_opml():
    opml_feed_list = listparser.parse(OPML_FILE)
    opml_feeds = opml_feed_list.feeds
    print("Read in some opml_feeds [" + str(len(opml_feeds)) + "]")
    opml_dict = {}
    for opml_feed in opml_feeds:
        print("adding " + opml_feed.title + " : " + opml_feed.url)
        #dict1 = {opml_feed.title:'geeks', 'key4':'is', 'key5':'fabulous'}
        opml_dict.update({opml_feed.title : opml_feed.url})
    return opml_dict

def play_audio(file):
    player.start_next_song(file)
    print(file + ' finished')


def download_audio(rss_feed_url, index, save_file_name):
    rss_feed = feedparser.parse(rss_feed_url)
    entries = rss_feed.entries
    first_entry = entries[index]
    links = first_entry.links
    url =''
    for link in links:
        type = link.type
        #print(type)
        if "audio" in type:
            url = link.href
            print(url)
            urllib.request.urlretrieve(url, save_file_name)


def explore_opml_feed(opml_feed):
    #print(feed)
    print(opml_feed.title)
    print(opml_feed.url)
    #rss_feed = feedparser.parse(opml_feed.url)
    #explore_rss_feed(rss_feed)

def explore_rss_feed(rss_feed):
    #print(rss_feed)
    #print(rss_feed.feed.content)

    entries = rss_feed.entries
    #print(entries)
    print("Read in some entries [" + str(len(entries)) + "]")

    for entry in entries:
        print(entry.title)
        #link = entry.link
        #print(link)
        links = entry.links
        for link in links:
            type = link.type
            #print(type)
            if "audio" in type:
                url = link.href
                print(url)




def plugin_stop():
    """
    EDMC is closing
    """
    print("Farewell cruel world!")


OPML_FILE = 'feeds.opml'
plugin_start('.')
anyKey = input("Press any key to stop...")
print(anyKey + " isn't the any key, but I'll stop anyway!")
plugin_stop()