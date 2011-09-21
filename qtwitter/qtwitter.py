__author__ = 'Gollum23'

from twython.twython import Twython
from datetime import *

class ObjTwitter:
    """
    Objeto donde se captura la informacion de twitter
    """
    def __init__(self, usuario, mensaje, timestamp):
        self.usuario = usuario
        self.mensaje = mensaje
        self.timestamp = timestamp
        self.avatar = ""

    def imprimir(self):
        print("%s" % self.usuario)

    def __str__(self):
        return self.mensaje

def buscador(q, excep):
    twitter = Twython()
    query = q
    #tweets = twitter.searchTwitter(q = query, rpp = "100", page = "1")
    tweets = twitter.searchTwitter(q = query, rpp = "100")
    lista_tweets = []
    for tweet in tweets['results']:
        if tweet['text'].encode('utf-8').find(excep) < 0:
            contenido = tweet['text'].encode('utf-8')
            usuario = tweet['from_user'].encode('utf-8')
            hora = tweet['created_at']
            hora_convert = datetime.strptime(hora, '%a, %d %b %Y %H:%M:%S +0000')
            horaColombia = hora_convert - timedelta(minutes = 300)
            
            objetoTweet = ObjTwitter(usuario = usuario, mensaje=contenido, timestamp=horaColombia)
            objetoTweet.avatar = tweet['profile_image_url'].encode('utf-8')
            lista_tweets.append(objetoTweet)

    return lista_tweets