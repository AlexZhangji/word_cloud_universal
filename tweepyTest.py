import time
from tweepy import OAuthHandler, StreamListener
from tweepy import Stream

ckey = ''
csecret = ''
atoken = ''
asecret = ''


class listener(StreamListener):
    # change the number of tweet when
    tweetCount = 0
    stopAt = 77

    def on_data(self, data):

        tweet = data.split(',"text":"')[1].split('","source')[0]
        print tweet
        tweet = tweet.replace('RT', '')
        tweet = tweet.replace('nhttps', ' ')
        tweet = tweet.replace('amp', ' ')
        # increment tweet count by 1
        listener.tweetCount += 1
        # save = str(time.time()) + '::' + tweet
        saveFile = open('twitter_text.csv', 'a')
        saveFile.write(tweet)
        saveFile.write('\n')

        if listener.tweetCount < listener.stopAt:
            return True
        else:
            print('maxNum = ' + str(listener.tweetCount))
        saveFile.close()
        return False

    def on_error(self, status):
        print status


def get_stream(keyword):
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    twitterStream = Stream(auth, listener())
    twitterStream.filter(track=[keyword])

# get_stream('China')

# auth = OAuthHandler(ckey, csecret)
# auth.set_access_token(atoken, asecret)
# twitterStream = Stream(auth, listener())
# twitterStream.filter(track=['barcelona'])
