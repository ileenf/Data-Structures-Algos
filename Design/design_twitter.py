class Twitter:
    # this method uses heaps (nsmallest) and tracking of user's following and their own tweets
    # iterate through only valid tweets: the tweets posted by user and their following
    def __init__(self):
        self.following = defaultdict(set)
        self.user_to_tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_to_tweets[userId].append([self.time, tweetId])
        self.time -= 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        following = self.following[userId]
        following.add(userId)
        
        tweets_from_following = []
        heapq.heapify(tweets_from_following)
        
        for followed_user in following:
            for tweet in self.user_to_tweets[followed_user]:
                heapq.heappush(tweets_from_following, tweet)
        
        news_feed = heapq.nsmallest(10, tweets_from_following)
        return [tweet[1] for tweet in news_feed]
            
    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
 
class Twitter:
    # this method keeps track of user's following and all tweets in one list. no heaps used since tweets are already
    # in chronological order in self.tweets
    # slightly less efficient because we iterate over invalid tweets (tweets not posted by user's following),
    # since we can't access knowledge of who posted which tweet easily
    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append([userId, tweetId])
        
    def getNewsFeed(self, userId: int) -> List[int]:
        news_feed = []
        following = self.following[userId]
        following.add(userId)
        
        for user_id, tweet_id in self.tweets[::-1]:
            if len(news_feed) == 10:
                break
            if user_id in following:
                news_feed.append(tweet_id)
        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
