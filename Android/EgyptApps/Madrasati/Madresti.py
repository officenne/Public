import urllib.request as request
import json
import os.path

# Get Latest from Youtube

YoutubeApiKey = 'AIzaSyCghMwZZstjt92Zx5Mep8V2_aCvvVdkI1A'
YoutubeChannelID = 'UCnxju7_Ug6VbC6en6tBL6Aw'
YoutubeUrl = 'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId='
YoutubeUrl2 = '&type=video&order=date&maxResults=100&key='

save_path = 'C:\GitHub\Android\EgyptApps\Madrasati'

with request.urlopen(YoutubeUrl + "UCndb1LGM5oQJVhjh2NViU5g" + YoutubeUrl2 + YoutubeApiKey) as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "DorosIEN.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(YoutubeUrl + "UCL-2Lb4n3uiKbmLu9q9KroQ" + YoutubeUrl2 + YoutubeApiKey) as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "Madrasati.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        YoutubeUrl + "UCndb1LGM5oQJVhjh2NViU5g" + "&type=video&eventType=live&key=" + YoutubeApiKey) as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "Madrestna_Channel_Live.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')
