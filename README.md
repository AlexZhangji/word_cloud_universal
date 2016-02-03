# Word Cloud Universal

This is a personal side project that generate word cloud visualization based on any websites. With customized crawler for Twitter and Reddit. 

  - Works for any sites.
  - Customized crawler for Twitter and Reddit.
  - Generating word cloud with customizable outline.

*Most of this project was done in the first two months when I was learning Python.  So it can be rough around the edges.

###Sample Results
![sample_1](https://github.com/AlexZhangji/word_cloud_universal/blob/dev_/img/sample_1.png?raw=true)

![sample_2](https://github.com/AlexZhangji/word_cloud_universal/blob/dev_/img/sample_2.png?raw=true)


### Version
0.7.1

### Tech

Word Cloud Universal uses a number of open source projects to work properly:

* [wordcloud] -Word cloud visualization using PIL Matplotlib
* [Tweepy] - Twitter for Python!
* [requests] - Python HTTP Requests for Humans™
* [BeautifulSoup] - Pulling data out of HTML and XML 
* [jieba] - Chinese text segmentation


### Set up
Set "wc.font_path " as absolute directory file path to font file:

    wc.font_path = 'C:\GitHub\word_cloud\_fonts\lth.ttf'

*Font files can be found under _fonts folder.
*Compatible with various fonts.


Set different mask in place "mask" or  global variable"mask_img":

    mask = np.array(Image.open(path.join(d, mask_img)))

*Masks templates can be found under mask folder.
*Compatible with various masks.
![*Some mask templates](https://github.com/AlexZhangji/word_cloud_universal/blob/dev_/img/masks.png?raw=true)


###Run

In wordCloud.py:

for Reddit: 
  
    # generate from reddit forum
    # by default read 10 pages of recent posts. 
    numPage = 10
    subName = 'soccer' 
    make_reddit_word_cloud(subName , numPage)


for Twitter:

    # word cloud from twitter feed given any keyword 
    # by default read 77 tweet, since twitter API is kinda slow and 77 is a fantastic number.
    keyword = 'barcelona' 
    make_twitter_word_cloud(keyword)


for arbitrary sites:

    # generate from url 
    url = 'https://en.wikipedia.org/wiki/The_Library_of_Babel' 
    word_cloud_url(url)


for local files:

    # generate from local text file 
    word_cloud_local_file('resources/got.txt')

### Todos

 - Making this as a Restful API using Python/Flask.(60% done)
 - Intelligent and more general useful forum crawler. 
 - Customizable color, selected color scheme.
 - Auto generated image outline for any given keywords or sites.

License
----

MIT


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [wordcloud]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [wordcloud]: <https://github.com/amueller/word_cloud>
   [requests]: <https://github.com/kennethreitz/requests>
   [BeautifulSoup]: <http://www.crummy.com/software/BeautifulSoup/>
   [jieba]: <https://github.com/fxsjy/jieba>
   [Ace Editor]: <http://ace.ajax.org>
   [Tweepy]: <https://github.com/tweepy/tweepy>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [keymaster.js]: <https://github.com/madrobby/keymaster>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>
   
   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]:  <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>


