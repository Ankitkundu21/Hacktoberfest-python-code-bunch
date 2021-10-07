import sys
import numpy as np
import tweepy
import os
import requests

from keras.models import Sequential
from keras.layers import Dense
from textblob import TextBlob

consumer_key = "zYfepKVChCXVHyd6tYQEEcsmF"
comsumer_secret = "g7NhffplUKTV8pCnmRn5SdY9aD0cOkVTLzqZK7nCEp53kr12yV"
access_token = "1636245794-6lSimXGxl25ThnAPbObNcT795a6F8XK09uPkXMq"
access_secret = "jaguuzAsxJfsWwkYP4mgunwwReLI1XkGc0xp0FqbOXOD3"
login = tweepy.OAuthHandler(consumer_key, comsumer_secret)
login.set_access_token(access_token, access_secret)
user = tweepy.API(login)

file = 'historical.csv'

def get_name(symbol):
    url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(symbol)
    result = requests.get(url).json()
    for x in result['ResultSet']['Result']:
        if x['symbol'] == symbol:
            return x['name']

def sentiment(quote, num):
    tweet_list = user.search(get_name(quote), count = num)
    positive = 0
    null = 0
    for tweet in tweet_list:
        check = TextBlob(tweet.text).sentiment
        if check.subjectivity == 0:
            null += 1
            next
        if check.polarity > 0:
            positive += 1

    if positive > ((num - null)/2):
        return True

def get_data(quote):
    url = "https://www.quandl.com/api/v3/datasets/NSE/{}.csv?api_key=-2RZqXCVrgC5VNizaqb8".format(quote)
    # url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={}&interval=1min&apikey=STOPKETMIGTW8LT4&datatype=csv".format(quote)
    r = requests.get(url)

    if r.status_code != 400:
        with open(file, 'wb') as fl:
            for line in r:
                fl.write(line)
    return True

def predict():
    data = []
    with open(file) as f:
        for num, line in enumerate(f):
            if num != 0:
                data.append(float(line.split(',')[1]))
    data = np.array(data)

    def create_set(data):
        datax = [data[n+1] for n in range(len(data)-2)]
        return np.array(datax), data[2:]

    trainx, trainy = create_set(data)

    classifier = Sequential()
    classifier.add(Dense(8, input_dim = 1, activation = 'relu'))
    classifier.add(Dense(1))
    classifier.compile(loss = 'mean_squared_error', optimizer = 'adam')
    classifier.fit(trainx, trainy, epochs= 200, batch_size = 2, verbose = 0)

    prediction = classifier.predict(np.array([data[0]]))
    return 'from %s to %s' % (data[0], prediction[0][0])

quote = raw_input("Enter stock quote: ").upper()


if not get_data(quote):
    print ('ERROR, please re-run the script')

print(predict())

if not sentiment(quote, num = 100):
    print ('This stock has good sentiment')
else:
    print ('This stock has bad sentiment')

os.remove(file)
