from flask import Flask, jsonify, request
import redis
import sys


app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, db=0)

# Route to display all tweets
@app.route('/tweets', methods=['GET'])
def get_tweets():
    tweets = []
    for tweet_id in r.lrange('tweets', 0, -1):
        tweet = r.hgetall(tweet_id)
        tweets.append(tweet)
    return jsonify(tweets)

# Route to add a new tweet to Redis
@app.route('/tweets', methods=['POST'])
def add_tweet():
    tweet = request.json
    tweet_id = r.incr('tweet_id')
    r.hmset(tweet_id, tweet)
    r.lpush('tweets', tweet_id)
    return jsonify({'id': tweet_id})

# Route to assign a tweet to a person
@app.route('/tweets/<int:tweet_id>/assign', methods=['PUT'])
def assign_tweet(tweet_id):
    person = request.json['person']
    r.hset(tweet_id, 'assigned_to', person)
    return '', 204

# Route to retweet a tweet
@app.route('/tweets/<int:tweet_id>/retweet', methods=['POST'])
def retweet_tweet(tweet_id):
    retweet_id = r.incr('tweet_id')
    tweet = r.hgetall(tweet_id)
    tweet['retweeted_from'] = tweet_id
    r.hmset(retweet_id, tweet)
    r.lpush('tweets', retweet_id)
    return jsonify({'id': retweet_id})

# Route to display all subjects
@app.route('/subjects', methods=['GET'])
def get_subjects():
    subjects = r.smembers('subjects')
    return jsonify([s.decode() for s in subjects])

# Route to display all tweets related to a subject
@app.route('/subjects/<subject>', methods=['GET'])
def get_tweets_by_subject(subject):
    tweets = []
    for tweet_id in r.smembers('subject:'+subject):
        tweet = r.hgetall(tweet_id)
        tweets.append(tweet)
    return jsonify(tweets)


#fonction main de notre projet qui permet d'executer notre Flask apllication.
if __name__ == "__main__":
    if len(sys.argv) > 1 :
        if sys.argv[1] == "check_syntax":
            print("Build [ OK ]")
            exit(0)
        else:
            print("Passed argument not supported ! Supported argument : check_syntax")
            exit(1)
    app.run(debug=True)
