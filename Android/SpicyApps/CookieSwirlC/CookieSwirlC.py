import urllib.request as request
import json
import os.path

# Get Latest from Youtube

YoutubeApiKey = 'AIzaSyACJCHu-oaZUtC6gaygvqii3LiBvMrGWBY'
YoutubeChannelID = 'UCqJNTGwKmgMCwfYDbnz514Q'
YoutubeUrl = 'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId='
YoutubeUrl2 = '&type=video&order=date&maxResults=100&key='

save_path = r'C:\GitHub\Android\SpicyApps\CookieSwirlC'


with request.urlopen(
        "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCelMeixAOTs2OQAAi9wU8-g&type=video&order=date&maxResults=100&key=AIzaSyDnoxRyPtrO9We-Aa3ACMpluNag24-DLIc") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, 'Cookieswirlc.json')
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')


with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLL-Nk7g-sSABT_w_HdKRwm8791DHakMjO&key=AIzaSyDnnQb152LtaUR3dBCXNDoRbuV7cGdtb6I") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "LOLSurprisePetsVideos.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')


with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLL-Nk7g-sSAApdavUTekRLmVxg4FjbGd5&key=AIzaSyDnnQb152LtaUR3dBCXNDoRbuV7cGdtb6I") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "ShopkinsSeason.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')



with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLL-Nk7g-sSACaLvIyKnwd_AqptIeS4qap&key=AIzaSyDnnQb152LtaUR3dBCXNDoRbuV7cGdtb6I") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "BarbieVideoSeriesUnboxing.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')



with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLL-Nk7g-sSADRdR4fhoPXTqL6HQv4qEIG&key=AIzaSyDnnQb152LtaUR3dBCXNDoRbuV7cGdtb6I") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "ShopkinsBasketVideosOpeningReviews.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')



with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLL-Nk7g-sSAAVp4-GdGjmj0_hGuSO5gR4&key=AIzaSyDnnQb152LtaUR3dBCXNDoRbuV7cGdtb6I") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "MyLittlePonyVideos.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')


