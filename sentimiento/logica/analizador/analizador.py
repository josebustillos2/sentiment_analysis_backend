from textblob import TextBlob
import tweepy

ckey = "hAy0NSnunVBaC6ytzQR4YCXS8"
csecret = "4TDUVUj0Z5DjqGLbhLy8hlsYCvL0ZhYQ1n8OyF7lI5vqr1xXVj"
atoken = "850297886-pufDHZRPM4EoQMv0yG014Zwbow8mZwaYTN3EQ24v"
asecret = "xEYwVegry2mK0iQRcElHLEuvsFxRR4FDEuBAIZso1eDYc"

auth = tweepy.OAuthHandler(ckey, csecret)

def sentimiento(tweet):
    analysis = TextBlob(tweet)
    # analysis2 = TextBlob(tweet,analyzer=NaiveBayesAnalyzer())
    #print('\n', analysis.sentiment)
    # print('\n', analysis2.sentiment)
    # print(analysis2.sentiment[0])
    if analysis.sentiment[0] > 0:
        return ('Positivo')
    elif analysis.sentiment[0] < 0:
        return ('Negativo')
    else:
        return ('Neutral')


