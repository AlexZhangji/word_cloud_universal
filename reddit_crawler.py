import re
# from urllib2 import Request, urlopen

from bs4 import BeautifulSoup
import requests
import time

__author__ = 'JI'


#  get beautiful soup object by id with browser mask
def get_soup_by_url(url, parser=None):
    req = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    page = req.text
    if parser is None:
        soup = BeautifulSoup(page, 'html.parser')
    else:
        soup = BeautifulSoup(page, str(parser))
    return soup


# get all the post links in given pages for certain subreddit
def get_subreddit_entries(subName, pageNum):
    # init the page counter
    page_counter = 1
    url = 'https://www.reddit.com/r/' + subName + '/'
    # mega_comment_list = []

    f = open('reddit_text.txt', 'w')
    # crawl until reach the given page number
    while page_counter < pageNum:
        print('url:' + url)

        soup = get_soup_by_url(url)
        # post name, link, num of comments
        for post in soup.findAll("div", class_='entry unvoted'):
            title = post.contents[0].find('a').text
            title = title.split('(')[0]
            title = re.sub(r'\W+', ' ', title).encode('utf-8')
            try:
                link = (post.contents[2]).find('a').get('href').encode('utf-8')
                num_comment = re.findall(r'\d+', post.contents[2].text)[0].encode('utf-8')
            except IndexError:
                num_comment = '0'

            except AttributeError as e:
                print('AttributeError happens to reading post')
                print('error ' + str(e))
                print(title)

            if int(num_comment) > 30:
                print(title + '\n' + str(link) + '\n' + 'comments:' + str(num_comment) + '\n')

                # get the list of comments
                # mega_comment_list += get_text_from_post(link)
                # f.write("\n".join(get_text_from_post_with_filter(link, ['barcelona', 'messi', 'barca'])))
                comments = get_text_from_post(link)
                for comment in comments:
                    f.write("\n" + str(comment))


        # get the url for next page and update the url
        next_btn = soup.find("div", class_='nav-buttons')
        try:
            for in_text in next_btn.contents[0].findAll('a'):
                if 'next' in in_text.text:
                    next_page_url = in_text.get('href').encode('utf-8')
        except AttributeError:
            time.sleep(2)
            soup = get_soup_by_url(url)
            next_btn = soup.find("div", class_='nav-buttons')
            for in_text in next_btn.contents[0].findAll('a'):
                if 'next' in in_text.text:
                    next_page_url = in_text.get('href').encode('utf-8')
                else:
                    print('you have reached the bottom of rabbit hole.')
                    return False

        if next_page_url == url:
            print('you have reached the bottom of rabbit hole.')
            return False

        page_counter += 1
        print('\npage:' + str(page_counter) + ' ' + next_page_url + '\n')
        url = next_page_url
        # not sure if necessary
        time.sleep(1)

        # return mega_comment_list


# only extract post with certain words
# filterList is list of words
def get_text_from_post_with_filter(url, filterList=None):
    list_comment = []
    # url = 'https://www.reddit.com/r/soccer/comments/3u9ho3/dani_carvajal_goal_vs_shakhtar_donetsk_03/'
    soup = get_soup_by_url(url)
    for post in soup.findAll("div", class_="usertext-body"):
        if len(post.text):
            # get rid of static msg in every reddit post
            if not post.find('blockquote'):
                # parse comment so that it only contains alphabet and numeric chars
                content = " ".join(re.findall("[a-zA-Z0-9]+", post.text))
                for filter_word in filterList:
                    if filter_word in content.lower():
                        list_comment.append(content.encode('utf-8'))
                        print(content.encode('utf-8'))
                        # only break this chain
                        break
    return list_comment


def get_text_from_post(url):
    list_comment = []
    # url = 'https://www.reddit.com/r/soccer/comments/3u9ho3/dani_carvajal_goal_vs_shakhtar_donetsk_03/'
    soup = get_soup_by_url(url)
    for post in soup.findAll("div", class_="usertext-body"):
        if len(post.text):
            # get rid of static msg in every reddit post
            if not post.find('blockquote'):
                # parse comment so that it only contains alphabet and numeric chars
                content = " ".join(re.findall("[a-zA-Z0-9]+", post.text))
                list_comment.append(content.encode('utf-8'))
    return list_comment


# estimate time
# start_time = time.time()
# get_subreddit_entries('starcraft', 60)

# url = 'https://www.reddit.com/r/soccer/comments/3u9ho3/dani_carvajal_goal_vs_shakhtar_donetsk_03/'
# print(get_text_from_post(url))
# print("--- %s seconds ---" % (time.time() - start_time))
