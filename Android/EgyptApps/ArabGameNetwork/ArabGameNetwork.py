import urllib.request as request
import json
import os.path

# Get Latest from Youtube

YoutubeApiKey = 'AIzaSyACJCHu-oaZUtC6gaygvqii3LiBvMrGWBY'
YoutubeChannelID = 'UCqJNTGwKmgMCwfYDbnz514Q'
YoutubeUrl = 'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId='
YoutubeUrl2 = '&type=video&order=date&maxResults=100&key='

save_path = 'C:\GitHub\Android\EgyptApps\ArabGameNetwork'


with request.urlopen(
        "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCV2JkEBmtfSYGAIlprAhAyQ&type=video&order=date&maxResults=100&key=AIzaSyDhUCsJgoE0yIMc1Go_Alcyc15kDc_T-qI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "agn.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')


with request.urlopen(
        "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCBAy1yyCcsjmNtQZTUpeXjA&type=video&order=date&maxResults=100&key=AIzaSyDhUCsJgoE0yIMc1Go_Alcyc15kDc_T-qI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "SAYED.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')


