import urllib.request as request
import json
import os.path
import subprocess

# Get Latest from Youtube

YoutubeApiKey = 'AIzaSyDnnQb152LtaUR3dBCXNDoRbuV7cGdtb6I'
YoutubeChannelID = 'UCqJNTGwKmgMCwfYDbnz514Q'
YoutubeUrl = 'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId='
YoutubeUrl2 = '&type=video&order=date&maxResults=100&key='

save_path = r'C:\GitHub\Android\EgyptApps\riyadrzq'

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCsc0cXTWBI7suJmQXvfs5Hw&type=video&order=date&maxResults=100&key=AIzaSyAQyLjGqjOnLMnuEmD7LqsaOqd80HD7sps") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "riyadrzqx.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')




subprocess.call([r'C:\GitHub\UpdateOnly.bat'])

