import urllib.request as request
import json
import os.path
import requests

# Get Latest from Youtube

YoutubeApiKey = 'AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI'
YoutubeChannelID = 'UCnxju7_Ug6VbC6en6tBL6Aw'
YoutubeUrl = 'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId='
YoutubeUrl2 = '&type=video&order=date&maxResults=100&key='
nextPageToken = None

save_path = 'C:\GitHub\Android\EgyptApps\Madrestna'

# First request
r = requests.get(
    "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&channelId=" + YoutubeChannelID + "&order=date&key=" + YoutubeApiKey)
if r.status_code == 200:
    json_data = r.json()
    nextPageToken = json_data.get("nextPageToken")
    print(r)

    completeName = os.path.join(save_path, "Recent.json")
    with open(completeName, 'w') as outfile:
        json.dump(json_data, outfile, indent=4)
else:
    print('An error occurred while attempting to retrieve data from the API.')

# Retrieve all the rest of the pages
i = 1
n = 1
while nextPageToken and i <= 10:
    i += 1
    r = requests.get(
        "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&channelId=" + YoutubeChannelID + "&order=date&key=" + YoutubeApiKey + "&pageToken=" + nextPageToken)

    if r.status_code == 200:

        json_data = r.json()
        nextPageToken = json_data.get("nextPageToken")
        print(r)

        name = str(n)

        completeName = os.path.join(save_path, name + ".json")
        with open(completeName, 'w') as outfile:
            json.dump(json_data, outfile, indent=4)
        n = n + 1

    else:
        print('An error occurred while attempting to retrieve data from the API.')
