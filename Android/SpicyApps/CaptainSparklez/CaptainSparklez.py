import urllib.request as request
import json
import os.path

# Get Latest from Youtube

YoutubeApiKey = 'AIzaSyACJCHu-oaZUtC6gaygvqii3LiBvMrGWBY'
YoutubeChannelID = 'UCqJNTGwKmgMCwfYDbnz514Q'
YoutubeUrl = 'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId='
YoutubeUrl2 = '&type=video&order=date&maxResults=100&key='

save_path = r'C:\GitHub\Android\SpicyApps\CaptainSparklez'


with request.urlopen(
        "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCAJ41d46i6mcNAsvsWRc9hw&type=video&order=date&maxResults=100&key=AIzaSyDS-mEXQ4W7FH_Yp8sahmVghwZQtQ3-YiY") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, 'CaptainSparklez.json')
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')


with request.urlopen(
        "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCo8_GzFxkXAYtwN0QabhJ8A&type=video&order=date&maxResults=100&key=AIzaSyDS-mEXQ4W7FH_Yp8sahmVghwZQtQ3-YiY") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, 'JordanReacts.json')
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')


with request.urlopen(
        "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCshoKvlZGZ20rVgazZp5vnQ&type=video&order=date&maxResults=100&key=AIzaSyDS-mEXQ4W7FH_Yp8sahmVghwZQtQ3-YiY") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, 'CaptainSparklez2.json')
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')



with request.urlopen(
        "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCn7MpX76Bou10j6IkgAcdjg&type=video&order=date&maxResults=100&key=AIzaSyDS-mEXQ4W7FH_Yp8sahmVghwZQtQ3-YiY") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, 'JordanMaron.json')
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')





