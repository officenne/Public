import urllib.request as request
import json
import os.path

# Get Latest from Youtube

YoutubeApiKey = 'AIzaSyDnnQb152LtaUR3dBCXNDoRbuV7cGdtb6I'
YoutubeChannelID = 'UCqJNTGwKmgMCwfYDbnz514Q'
YoutubeUrl = 'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId='
YoutubeUrl2 = '&type=video&order=date&maxResults=100&key='

save_path = 'C:\GitHub\Android\EgyptApps\Badr_Family'


with request.urlopen(
        "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCYogOW28QIQdfvfY5KyzDsw&type=video&order=date&maxResults=100&key=AIzaSyDnnQb152LtaUR3dBCXNDoRbuV7cGdtb6I") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "Badr_Family.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')


with request.urlopen(
        "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCBA_nLOERvrGchrHHxYTqXQ&type=video&order=date&maxResults=100&key=AIzaSyDnnQb152LtaUR3dBCXNDoRbuV7cGdtb6I") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "khwlh.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')
        

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLVnWQ4Ee6xUQ9__gVa5H4EPJCKrt6G3at&key=AIzaSyDnnQb152LtaUR3dBCXNDoRbuV7cGdtb6I") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "Challenges.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLVnWQ4Ee6xUR_jAoD76k3OuLlrgKhnovG&key=AIzaSyDnnQb152LtaUR3dBCXNDoRbuV7cGdtb6I") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "Travel.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

