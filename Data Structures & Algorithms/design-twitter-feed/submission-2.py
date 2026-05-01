from collections import defaultdict
import heapq as hq
class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        for t in self.tweets[userId][-10:]:
            hq.heappush(heap, t)
        
        for u in self.following[userId]:
            for t in self.tweets[u][-10:]:
                hq.heappush(heap, t)
        
        return [tweetId for _,tweetId in hq.nlargest(10,heap)]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
