import time
import json
from django.http import HttpResponse
from logica.analizador.analizador import sentimiento,asecret,atoken,auth,ckey,csecret
import tweepy
from tweepy import Stream
from webAnalisis.models import Tuit
from tweepy.streaming import StreamListener
auth.set_access_token(atoken, asecret)

def index(request):
    palabra = ['Lenin Moreno', '#SOSEcuador', 'Palacio de Carondelet', '#Quito']
    primero(palabra)
    segundo(palabra)
    return HttpResponse("Hello, world. You're at the polls index.")



def primero(palabra):
    print("-------------    PRIMER METODO BUSQUEDA")
    api = tweepy.API(auth)
    public_tweets = api.home_timeline()
    for tweet in tweepy.Cursor(api.search, q=[palabra]).items(10000000000):
        if (tweet.lang == 'es'):
            print('------------------------------------------------------')
            dia = tweet._json
            ss = sentimiento(tweet.text)
            dia['sentimiento'] = ss

            print(dia)
            return dia

# segunda metodo extraer tiempo real
def segundo(palabra):
    print("-------------    SEGUNDO METODO TIEMPO REAL")
    start_time = time.time()
    try:
        class listener(StreamListener):
            def __init__(self, start_time, time_limit=120000):
                self.time = start_time
                self.limit = time_limit

            def on_data(self, data):
                while (time.time() - self.time) < self.limit:
                    try:
                        dia = json.loads(data)
                        s = sentimiento(dia['text'])
                        dia['sentimiento'] = s
                        print(dia)
                        return True
                    except BaseException:
                        pass
                        time.sleep(5)
        twitterStream = Stream(auth, listener(start_time, time_limit=120000))
        twitterStream.filter(track=palabra, languages=['es'])
    except ValueError:
        pass
