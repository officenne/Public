import urllib.request as request
import json
import os.path

# Get Latest from Youtube

YoutubeApiKey = 'AIzaSyACJCHu-oaZUtC6gaygvqii3LiBvMrGWBY'
YoutubeChannelID = 'UCqJNTGwKmgMCwfYDbnz514Q'
YoutubeUrl = 'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId='
YoutubeUrl2 = '&type=video&order=date&maxResults=100&key='

save_path = 'C:\GitHub\Android\SpicyApps\MissKaty'


with request.urlopen(
        "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UC_8PAD0Qmi6_gpe77S1Atgg&type=video&order=date&maxResults=100&key=AIzaSyCYhHtLs42EUKEq5Jc6fR80_oF2penoDNg") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, 'MisterMax.json')
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')



with request.urlopen(
        "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCcartHVtvAUzfajflyeT_Gg&type=video&order=date&maxResults=100&key=AIzaSyCYhHtLs42EUKEq5Jc6fR80_oF2penoDNg") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, 'MissKaty.json')
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')



with request.urlopen(
        "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCjB2ziXgFTei3xGr3avOIig&type=video&order=date&maxResults=100&key=AIzaSyCYhHtLs42EUKEq5Jc6fR80_oF2penoDNg") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, 'MisterMaxPlay.json')
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')



with request.urlopen(
        "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCvd_X-p3MEFQKoDGQjb3OiQ&type=video&order=date&maxResults=100&key=AIzaSyCYhHtLs42EUKEq5Jc6fR80_oF2penoDNg") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, 'FedorUKVlogs.json')
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')



with request.urlopen(
        "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCufUZVlt_xWA2w0l_I2H6uw&type=video&order=date&maxResults=100&key=AIzaSyCYhHtLs42EUKEq5Jc6fR80_oF2penoDNg") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, 'KatyPLAY.json')
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')





with request.urlopen(
        "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCYKtRnIfwiJkVic89Yt51Pw&type=video&order=date&maxResults=100&key=AIzaSyCYhHtLs42EUKEq5Jc6fR80_oF2penoDNg") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, 'PapaPlay.json')
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')





with request.urlopen(
        "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UC9XUOGLM460u7Wb2d28DuaQ&type=video&order=date&maxResults=100&key=AIzaSyCYhHtLs42EUKEq5Jc6fR80_oF2penoDNg") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, 'BooBooRhymes.json')
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')




