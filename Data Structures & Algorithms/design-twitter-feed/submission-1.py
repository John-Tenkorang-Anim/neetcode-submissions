import heapq
from collections import defaultdict
class Twitter:

    def __init__(self):
        self.timestamps = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamps += 1
        self.tweets[userId].append((self.timestamps, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        for t in self.tweets[userId][-10:]:
            heapq.heappush(heap, t)

        for followee in self.following[userId]:
            for t in self.tweets[followee][-10:]:
                heapq.heappush(heap, t)

        return [tweetId for _,tweetId in heapq.nlargest(10,heap)]
        #since the most recent tweet will have a larger time if the tweet
        #started at 0

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        
