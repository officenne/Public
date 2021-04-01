import urllib.request as request
import json
import os.path
import subprocess

# Get Latest from Youtube

YoutubeApiKey = 'AIzaSyACJCHu-oaZUtC6gaygvqii3LiBvMrGWBY'
YoutubeChannelID = 'UCqJNTGwKmgMCwfYDbnz514Q'
YoutubeUrl = 'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId='
YoutubeUrl2 = '&type=video&order=date&maxResults=100&key='

save_path = 'C:\GitHub\Android\EgyptApps\shfa'


with request.urlopen(
        "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCwHE1kM1CPJd_pI9FQ0-4dg&type=video&order=date&maxResults=100&key=AIzaSyB2nXPdK7FHisTZbvW-qNZuQ82NPZKSzd4") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "shfa.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCQ7x25F6YXY9DvGeHFxLhRQ&type=video&order=date&maxResults=100&key=AIzaSyB2nXPdK7FHisTZbvW-qNZuQ82NPZKSzd4") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "shfa2.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UC1hNgneuRwhoWhfzSem86fA&type=video&order=date&maxResults=100&key=AIzaSyB2nXPdK7FHisTZbvW-qNZuQ82NPZKSzd4") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "LikeShfaVlog.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCItvCYsrioqP8bHqJvbAejA&type=video&order=date&maxResults=100&key=AIzaSyB2nXPdK7FHisTZbvW-qNZuQ82NPZKSzd4") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "shfa_gaming.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCNvYCW3cMbkWy2g2v4Wb6xw&type=video&order=date&maxResults=100&key=AIzaSyB2nXPdK7FHisTZbvW-qNZuQ82NPZKSzd4") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "shfa_show_India.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCCLyyLeiiARb8Rg3K4K_8iA&type=video&order=date&maxResults=100&key=AIzaSyB2nXPdK7FHisTZbvW-qNZuQ82NPZKSzd4") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "shfa_family_IDN.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCkV2W_4Zur037NrECHHtKMg&type=video&order=date&maxResults=100&key=AIzaSyB2nXPdK7FHisTZbvW-qNZuQ82NPZKSzd4") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "shfa_spanish.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

subprocess.call([r'C:\GitHub\UpdateOnly.bat'])
