# -*- coding: utf-8 -*-
from os import path
# import Image
import os
import re
from PIL import Image
from bs4 import BeautifulSoup
import jieba
import numpy as np
import matplotlib.pyplot as plt
import requests
from wordcloud import WordCloud


# from nltk.corpus import stopwords

stop_words_list = {}
mask_img = "mask/terran.jpg"
abs_font_dir = 'C:\Users\JI\Documents\GitHub\PycharmProjects\myDrone\word_cloud\_fonts\lth.ttf'


# filter with stop words and get the words frequency
# does not filter both English and Chinese due to performance consideration
def get_sorted_word_list(content, filter_size):
    hist = {}

    # get the list of stop words for filter
    # by default set to english, can change to 'cn'
    en_stop_words = get_stop_words_list('en')

    for word in jieba.cut(content):
        # word.isalpha can check if a word is actual word.
        if len(word) >= filter_size and word.isalpha() and word.lower().encode('utf-8') not in en_stop_words:
            hist[word] = hist.get(word, 0) + 1

    hist_sorted = sorted(hist.items(), key=lambda d: d[1], reverse=True)
    for i in range(20):
        print((hist_sorted[i][0]) + ' :' + str(hist_sorted[i][1]))

    return hist_sorted


# make word cloud given content of text
# core part of word cloud visualization
def make_word_cloud(content):
    # read the mask image
    d = path.dirname(__file__)
    # alice_mask = np.array(Image.open(path.join(d, "mask/terran.jpg")))
    mask = np.array(Image.open(path.join(d, mask_img)))
    # font__dir = '/var/www/FlaskApp/FlaskApp/word_cloud_min/_fonts/lth.ttf'
    # font__dir = 'C:\Users\zjsep_000\PycharmProjects\myDrone\word_cloud_min\_fonts\lth.ttf'
    # font__dir = '_fonts/lth.ttf'

    wc = WordCloud(background_color="white", max_words=1000, mask=mask)

    # give the absolute dir for font ttf file
    # wc.font_path = 'C:\Users\JI\Documents\GitHub\PycharmProjects\myDrone\word_cloud\_fonts\lth.ttf'
    wc.font_path = abs_font_dir
    # wc.font_path = 'C:\Users\zjsep_000\PycharmProjects\myDrone\word_cloud_min\_fonts\lth.ttf'

    # wc.font_path = '_fonts/lth.ttf'
    # wc.font_path = '/var/www/FlaskApp/FlaskApp/word_cloud_min/_fonts/lth.ttf'
    # brush options: {'shoujin_brush.ttf','Japan_brush.ttf','qingke_fangzheng.ttf','KouzanBrushFont.ttf'}
    # serfi-fonts:[]

    wc.generate_from_frequencies(content)
    # generate word cloud
    # wc.generate(text)


    # store to file
    wc.to_file(path.join(d, "img/output.png"))
    # store to static foder in web server
    # wc.to_file(path.join(d, "../static/output.png"))

    # show
    plt.imshow(wc)
    plt.axis("off")
    plt.figure()
    plt.imshow(mask, cmap=plt.cm.gray)
    plt.axis("off")
    plt.show()


# return stop words list from local file for Chinese and English and use accordingly
def get_stop_words_list(lan):
    # if global var exist
    if stop_words_list:
        # check if language required is the sames
        if stop_words_list[0] is lan:
            return stop_words_list
        else:
            stop_words_list.clear()
            get_stop_words_list(lan)
    else:
        # get stop list according to the language
        if lan is 'en':
            fn = os.path.join(os.path.dirname(__file__), 'stop_words/stop-words_english_en.txt')
            return open(fn, 'rb').read().split()
        elif lan is 'cn':
            fn = os.path.join(os.path.dirname(__file__), 'stop_words/stop_words_cn.txt')
            return open(fn, 'rb').read().split()
        else:
            return {}


# generate word cloud for local files
# filter words that has length less than 2

def word_cloud_local_file(filename):
    d = path.dirname(__file__)
    # Read the whole text.
    text = open(path.join(d, filename)).read()
    # second parameter is the filter size
    content = get_sorted_word_list(text, 2)
    make_word_cloud(content)


# helper function that return BeautifulSoup object by given url
def get_soup_by_url(url, parser=None):
    sourceCode = requests.get(url)
    plainText = sourceCode.text
    if parser is None:
        # get rid of html parser warning
        soup = BeautifulSoup(plainText, 'html.parser')
    else:
        soup = BeautifulSoup(plainText, str(parser))
    return soup


# filter out non-alphanumerical chars and scripts in html page
def clean_html(url):
    soup = get_soup_by_url(url)
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()  # rip it out
    # get text
    text = soup.body.get_text()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())

    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    # strip non-alphanumeric chars
    text = re.sub(r'\W+', ' ', text)
    return text


def word_cloud_url(url):
    # filter out non-alphanumerical chars
    url_text = clean_html(url)
    content = get_sorted_word_list(url_text, 2)
    make_word_cloud(content)


def make_reddit_word_cloud(subName, subPage):
    from reddit_crawler import get_subreddit_entries
    get_subreddit_entries(subName, subPage)
    word_cloud_local_file('reddit_text.txt')


# Integrated with tweepy and Twitter API
# by default read 77 tweets
def make_twitter_word_cloud(keyword):
    # discard previously crawled files
    fileName = 'twitter_text.csv'
    if os.path.isfile(fileName):
        os.remove(fileName)

    from tweepyTest import get_stream
    get_stream(keyword)
    word_cloud_local_file(fileName)


# change mask and font here
# mask_img = "mask/terran.jpg"
# abs_font_dir = 'C:\Users\JI\Documents\GitHub\PycharmProjects\myDrone\word_cloud\_fonts\lth.ttf'


# generate from reddit forum
# by default read 10 pages of recent posts.
numPage = 20
make_reddit_word_cloud('soccer', numPage)


# generate from url
# url = 'http://us.blizzard.com/en-us/company/careers/posting.html?id=15000YC'
# word_cloud_url(url)


# word cloud from twitter feed given any keyword
# by default read 77 tweet, since twitter API is kinda slow.
# keyword = 'barcelona'
# make_twitter_word_cloud(keyword)


# generate from local text file
# word_cloud_local_file('resources/got.csv')
# word_cloud_local_file('twitter_text.csv')
