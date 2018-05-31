#-*- coding: utf-8 -*-
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

consumer_key =''
consumer_secret = ''
access_token = ''
access_secret = ''

from tweepy.streaming import StreamListener, json
from pymongo import MongoClient

#mongodb
cliente = MongoClient('localhost', 27017)
banco = cliente.sams
tweets_collection = banco.tweets
erros_collection = banco.erros

#tweepy
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)
        tweet = dict()
        tweet['tweet'] = status.text                             #conteúdo do tweet
        tweet['language'] = status.user.lang                     #idioma
        tweet['location'] = status.user.location                 #localização
        tweet['coordinates'] = status.coordinates                #coordenadas
        tweet['time'] = status.user.time_zone                    #time_zone
        tweet['geo'] = status.user.geo_enabled                   #geo
        tweet['name'] = status.user.name                         #nome
        tweet['followers'] = status.user.followers_count         #seguidores
        tweet['friends'] = status.user.friends_count             #seguindo
        tweet['at'] = status.user.created_at                     #criacao da conta do usuário
        tweet['back'] = status.user.profile_background_color     #cor de fundo do usuário
        tweet['source'] = status.source                          #fonte de origem
        tweet['create'] = status.created_at
        tweets_collection.insert_one(tweet)



    def on_error(self, status):
        print("Error on_data: %s" % str(status))
        tweets_collection.insert_one(json.loads(status))
        return True


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=['worldcup', 'worldcup2018', '2018worldcup', 'FIFA 2018', 'FIFA2018', '2018FIFA', 'copa do mundo', 'copa2018', 'copadomundo2018', 'fifaworldcuprussia2018' , 'worldcuprussia2018','worldcuprussia', 'Russia2018','Mundial2018', 'boladacopa', 'boladacopa2018', 'fifa18worldcup'])



