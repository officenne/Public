import urllib.request as request
import json
import os.path

# Get Latest from Youtube

YoutubeApiKey = 'AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI'
YoutubeChannelID = 'UCnxju7_Ug6VbC6en6tBL6Aw'
YoutubeUrl = 'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId='
YoutubeUrl2 = '&type=video&order=date&maxResults=100&key='

save_path = 'C:/example/'


with request.urlopen(YoutubeUrl+YoutubeChannelID+YoutubeUrl2+YoutubeApiKey) as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path,  "Farouk.json")
        with open(completeName, 'w') as outfile:
            json.dump(data,  outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')