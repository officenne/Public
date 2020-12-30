import urllib.request as request
import json
import os.path
import subprocess

# Get Latest from Youtube

YoutubeApiKey = 'AIzaSyCU5vD9hgQ0jYH9ZGgAgnYTaIluZiXPbMk'
YoutubeChannelID = 'UCnxju7_Ug6VbC6en6tBL6Aw'
YoutubeUrl = 'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId='
YoutubeUrl2 = '&type=video&order=date&maxResults=100&key='

save_path = 'D:\Github\Android\EgyptApps\Families'

with request.urlopen(YoutubeUrl + "UCYogOW28QIQdfvfY5KyzDsw" + YoutubeUrl2 + YoutubeApiKey) as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "Badr_Family.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(YoutubeUrl + "UCsc0cXTWBI7suJmQXvfs5Hw" + YoutubeUrl2 + YoutubeApiKey) as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "riyadrzq.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(YoutubeUrl + "UC_Bd5Yrn9kL8fisLfPmH5ww" + YoutubeUrl2 + YoutubeApiKey) as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "feehan.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(YoutubeUrl + "UCPOw2O3_uZ1doro9iR4x6vw" + YoutubeUrl2 + YoutubeApiKey) as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "mmoshaya.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(YoutubeUrl + "UCmIp3opkQ6cEeJ6ybGrC_2A" + YoutubeUrl2 + YoutubeApiKey) as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "mmoshaya2.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(YoutubeUrl + "UCR60erWn2_8aoaLE3OoVu4w" + YoutubeUrl2 + YoutubeApiKey) as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "Iman_Moshaya.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(YoutubeUrl + "UCfZVRPD9O6rlSFnanpNXG4A" + YoutubeUrl2 + YoutubeApiKey) as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "Yazan_Family.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(YoutubeUrl + "UCqJNTGwKmgMCwfYDbnz514Q" + YoutubeUrl2 + YoutubeApiKey) as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "anasala_family.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

#subprocess.call([r'C:\GitHub\Public\UpdateOnly.bat'])

