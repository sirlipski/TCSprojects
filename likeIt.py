from InstagramAPI import InstagramAPI
import json
import requests
from pprint import PrettyPrinter
from getpass import getpass
import time

pp =  PrettyPrinter(indent=2)

def like(self, mediaId):
        data = json.dumps({'_uuid': self.uuid,
                           '_uid': self.username_id,
                           '_csrftoken': self.token,
                           'media_id': mediaId})
        return self.SendRequest('media/' + str(mediaId) + '/like/', self.generateSignature(data))

def getTotalFollowers(api, user_id):
    """
    Returns the list of followers of the user.
    It should be equivalent of calling api.getTotalFollowers from InstagramAPI
    """

    followers = []
    next_max_id = True
    while next_max_id:
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''

        _ = api.getUserFollowers(user_id, maxid=next_max_id)
        followers.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return followers

def getRecentActivity(self):
    activity = self.SendRequest('news/inbox/?')
    return activity

def explore(self):
    return self.SendRequest('discover/explore/')

def getUserFeed(self, usernameId, maxid='', minTimestamp=None):
        query = self.SendRequest('feed/user/%s/?max_id=%s&min_timestamp=%s&rank_token=%s&ranked_content=true'
                                 % (usernameId, maxid, minTimestamp, self.rank_token))

def getTotalUserFeed(self, usernameId, minTimestamp=None):
        user_feed = [] 
        next_max_id = ''
        while True:
            self.getUserFeed(usernameId, next_max_id, minTimestamp)
            temp = self.LastJson
            for item in temp["items"]:
                user_feed.append(item)
            if temp["more_available"] is False:
                return user_feed
            next_max_id = temp["next_max_id"]

def like_users_posts(self,userID):
    TARGET = {
    'username': '',
    'media': '',
    'media_like': [],
    }

    TARGET['username'] = userID

    self.searchUsername(TARGET['username'])

    TARGET['user_data'] = self.LastJson['user']

    # pp.pprint(TARGET['user_data'])
    print('Okay! i want check {0} post.\n'.format(
        TARGET['username']
    ))

    self.getUserFeed(str(TARGET['user_data']['pk']))

    media = TARGET['media'] = self.LastJson['items']

    print('Total Post @{0}: {1} post.'.format(
        TARGET['username'],
        len(TARGET['media'])
    ))
    for post in media:
        like(self,post['pk'])
    time.sleep(2)

username = 'tonyanevko'
password = 'lkjhgfdsa321'

InstagramAPI = InstagramAPI(username, password)
InstagramAPI.login()

#following = InstagramAPI.getTotalFollowings(InstagramAPI.username_id)
like_users_posts(InstagramAPI,'i.lipski')

InstagramAPI.logout()