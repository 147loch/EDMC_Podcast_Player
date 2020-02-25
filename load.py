# -*- coding: utf-8 -*-

import listparser
import feedparser
import requests
import os.path
import sys
import io
from player import player

this = sys.modules[__name__]

OPML_FILE = 'feeds.opml'


def plugin_start3(plugin_dir):
    return plugin_start(plugin_dir)


def plugin_start(plugin_dir):
    """
    Load this plugin into EDMC
    """

    this.plugin_dir = plugin_dir

    print("I am loaded! My plugin folder is {}".format(
        plugin_dir.encode("utf-8")))
    #available_podcasts = load_opml()
    # print(available_podcasts)

    rss_feed_url = 'http://laveradio.com/feed/laveradio.xml'
    rss_feed = feedparser.parse(rss_feed_url)
    explore_rss_feed(rss_feed)

    rss_feed_item_url = get_rss_feed_item_url(rss_feed, 0)
    downloaded_audio = download_audio(rss_feed_item_url)
    #save_file = 'downloads/lr0.mp3'
    #download_audio(rss_feed_item_url, 0, save_file)
    play_audio(downloaded_audio)

    return "PodPlayer"


def load_opml():
    opml_feed_list = listparser.parse(OPML_FILE)
    opml_feeds = opml_feed_list.feeds
    print("Read in some opml_feeds [" + str(len(opml_feeds)) + "]")
    opml_dict = {}
    for opml_feed in opml_feeds:
        print("adding " + opml_feed.title + " : " + opml_feed.url)
        opml_dict.update({opml_feed.title: opml_feed.url})
    return opml_dict


def play_audio(file):
    player.start_next_song(file)
    print(file + ' finished')


def get_rss_feed_item_url(rss_feed, index):
    entries = rss_feed.entries
    entry = entries[index]
    links = entry.links
    url = ''
    for link in links:
        type = link.type
        if "audio" in type:
            url = link.href
            return url
    return None


# TODO: This should be multithreaded, because otherwise we'll have huge latency problems


def download_audio(rss_feed_item_url):
    filename_index = rss_feed_item_url.rfind('/')
    file_name = os.path.join(this.plugin_dir, 'downloads',
                             rss_feed_item_url[filename_index+1:])

    print(os.path.abspath(file_name))
    if not os.path.exists(file_name):
        print("Downloading " + rss_feed_item_url)
        # getsize = os.path.getsize(file_name)
        _file = requests.get(rss_feed_item_url, allow_redirects=True)
        with open(file_name, 'wb') as f:
            f.write(_file.content)
    else:
        print(rss_feed_item_url + " already exists")
    return file_name


def explore_opml_feed(opml_feed):
    # print(feed)
    print(opml_feed.title)
    print(opml_feed.url)
    #rss_feed = feedparser.parse(opml_feed.url)
    # explore_rss_feed(rss_feed)


def explore_rss_feed(rss_feed):
    # print(rss_feed)
    # print(rss_feed.feed.content)

    entries = rss_feed.entries
    # print(entries)
    print("Read in some entries [" + str(len(entries)) + "]")

    for entry in entries:
        #link = entry.link
        # print(link)
        links = entry.links
        for link in links:
            type = link.type
            # print(type)
            if "audio" in type:
                url = link.href
                print(url)


def plugin_stop():
    """
    EDMC is closing
    """
    print("Farewell cruel world!")
    pos = player.get_pos()
    print("Audio pos [" + str(pos) + "]")


plugin_start('.')
anyKey = input("Enter command...")
print(anyKey + " isn't the any key, but I'll stop anyway!")
plugin_stop()
