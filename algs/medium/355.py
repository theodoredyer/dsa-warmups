class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([tweetId, self.time])
        self.time -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        followees = self.followMap[userId]
        minheap = []

        self.followMap[userId].add(userId)
        for followee in followees:
            if followee in self.tweetMap:
                index = len(self.tweetMap[followee]) - 1
                tweetId, posted_time = self.tweetMap[followee][index]
                heapq.heappush(minheap, [posted_time, tweetId, followee, index - 1])

        while minheap and len(result) < 10:
            posted_time, tweetId, followee, index_of_next = heapq.heappop(minheap)
            result.append(tweetId)
            
            if index_of_next >= 0:
                tweetId, time = self.tweetMap[followee][index_of_next]
                heapq.heappush(minheap, [time, tweetId, followee, index_of_next - 1])

        return result


        pointer_list = [(len(i) - 1) for i in followers_tweets]
        heap = []
        for pointer in pointer_list:
            heap.append(followers_tweets)
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)     



"""
Should absolutely be an LC Hard, this problem is pretty tricky:

Things to note:
- we want to store the map of users as a dictionary with key=userids, value=set of followees
    we do this because followees will be unique, and we want O(1) add and remove
- store the tweets as a dictionary with key=userid, value = list of tweet ids and timestamps
- to follow and unfollow, just manipulate the users dictionary
- to get most recent tweets, we need to first get the lists of all of the tweets among people we
    follow, and then set up a maxheap looking at most recent posting date where each element in the heap
    also contains enough information for us to then go back and get the next tweet from each user. 

so for example for this heap we might have
[time1, user1, tweet1, next_index_in_user_tweet_list]
[time2, user2, tweet2, next_index_in_user_tweet_list]

So that after suppose we grab tweet1 from user1, we can find out user1's next candidate
tweet is going to be:
count, tweet_id = tweetmap[user1][next_index_in_user_tweet_list]

after generating our min heap we just iterate 10 times or until minheap is empty
and then after each iteration do whatever maintenance we need to do to repopulate minheap
for the popped user's tweet info
"""