"""
import twitter
api = twitter.Api(consumer_key='',
		  consumer_secret='',
                  access_token_key='',
                  access_token_secret='')

results = api.GetSearch(
    raw_query="https://api.twitter.com/2/tweets/search/recent?query=Huracan Maria&max_results=100")
"""
"""
import requests

url = "https://api.twitter.com/2/tweets/search/recent?query=Huracan Maria&max_results=100"

payload = {}
headers = {
  'Authorization': 'Bearer ',
  'Cookie': 'personalization_id="v1_U3N4nOLpl+CTvaSKqv/ZFw=="; guest_id=v1%3A160192601085866552'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text)
#print(response.text.encode('utf8'))
"""
import tweepy
import csv #Import csv
auth = tweepy.auth.OAuthHandler('', '')
auth.set_access_token('', '')

api = tweepy.API(auth)

# Open/create a file to append data to
csvFile = open('temblores.csv', 'a')

#Use csv writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,
                           q = "temblor sur",
                           since = "2016-01-01",
                           until = "2020-10-30"
                           ).items():

    # Write a row to the CSV file. I use encode UTF-8
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    print(tweet.created_at, tweet.text)
csvFile.close()
