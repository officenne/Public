import urllib.request as request
import json
import os.path

# Get Latest from Youtube

YoutubeApiKey = 'AIzaSyACJCHu-oaZUtC6gaygvqii3LiBvMrGWBY'
YoutubeChannelID = 'UCqJNTGwKmgMCwfYDbnz514Q'
YoutubeUrl = 'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId='
YoutubeUrl2 = '&type=video&order=date&maxResults=100&key='

save_path = r'C:\GitHub\Android\SpicyApps\MobileLegendsBangBang'


with request.urlopen(
        "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCEH7P7kyJIkS_gJf93VYbmg&type=video&order=date&maxResults=100&key=AIzaSyDS-mEXQ4W7FH_Yp8sahmVghwZQtQ3-YiY") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, 'Live.json')
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')




with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLj6liTXGYadCre9c3GTlLJqvVsza1x-fN&key=AIzaSyD5cWTcxuWVXgeN4J80BUC-nkk8sL8Oaqw") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "MostViewed.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')




with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLj6liTXGYadCjqRS2O5Ig4wiQNRrpL-b3&key=AIzaSyD5cWTcxuWVXgeN4J80BUC-nkk8sL8Oaqw") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "Popular.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')





with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLj6liTXGYadBXntGGoUTNZnN5rmx5KF_N&key=AIzaSyD5cWTcxuWVXgeN4J80BUC-nkk8sL8Oaqw") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "OfficialVideos.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')


