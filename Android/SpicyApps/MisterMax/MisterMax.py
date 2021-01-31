import urllib.request as request
import json
import os.path

# Get Latest from Youtube

YoutubeApiKey = 'AIzaSyACJCHu-oaZUtC6gaygvqii3LiBvMrGWBY'
YoutubeChannelID = 'UCqJNTGwKmgMCwfYDbnz514Q'
YoutubeUrl = 'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId='
YoutubeUrl2 = '&type=video&order=date&maxResults=100&key='

save_path = r'C:\GitHub\Android\SpicyApps\MisterMax'


with request.urlopen(
        "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UC_8PAD0Qmi6_gpe77S1Atgg&type=video&order=date&maxResults=100&key=AIzaSyDnoxRyPtrO9We-Aa3ACMpluNag24-DLIc") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, 'MisterMax.json')
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')


