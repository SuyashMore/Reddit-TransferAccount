import praw


# HOW to get CLient ID and Client Secret
# https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps

source = praw.Reddit(client_id='CLIENT-ID',
                     client_secret='CLIENT-SECRET',
                     password='PASSWORD', 
                     user_agent='USERAGENT', 
                     username='USERNAME')

target = praw.Reddit(client_id='CLIENT-ID',
                     client_secret='CLIENT-SECRET',
                     password='PASSWORD', 
                     user_agent='USERAGENT', 
                     username='USERNAME')

                     


def getSubReddits(redditObj):
    subscribed_subreddits = list(redditObj.user.subreddits(limit=None))
    subs = []
    for sub in subscribed_subreddits:
        subs.append((str(sub)))
    return subs

def getSavedPostURL(redditObj):
    saved_links = redditObj.user.me().saved()  
    for link in saved_links:
        print(link.url)


def subscribe(redditObj,sub):
    redditObj.subreddit(sub).subscribe()


def transferSubs(source,target):
    sourceSubs = getSubReddits(source)
    print(f"SourceSubs:{sourceSubs}")
    for sub in sourceSubs:
        print(f"Subscribing {sub}")
        subscribe(target,sub)

    print(f"Target Subs:{getSubReddits(target)}")    
    print("All SubReddits Transferred !")


if __name__ == "__main__":
    transferSubs(source,target)
