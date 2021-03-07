import urllib.request as request
import json
import os.path

# Get Latest from Youtube

YoutubeApiKey = 'AIzaSyACJCHu-oaZUtC6gaygvqii3LiBvMrGWBY'
YoutubeChannelID = 'UCqJNTGwKmgMCwfYDbnz514Q'
YoutubeUrl = 'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId='
YoutubeUrl2 = '&type=video&order=date&maxResults=100&key='

save_path = r'C:\GitHub\Android\SpicyApps\CKNToys'


with request.urlopen(
        "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UC135_IPK8XOEEdXdtcseR4w&type=video&order=date&maxResults=100&key=AIzaSyD5cWTcxuWVXgeN4J80BUC-nkk8sL8Oaqw") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, 'CKNToys.json')
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')


with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLaFtxW0stqq06OOpzgQEwC2xYU2gvGYFS&key=AIzaSyD5cWTcxuWVXgeN4J80BUC-nkk8sL8Oaqw") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "ToysReview.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')


with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLaFtxW0stqq2h_HS1lmcn0BWzcT_bXcV8&key=AIzaSyD5cWTcxuWVXgeN4J80BUC-nkk8sL8Oaqw") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "PawPatrolToys.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')



with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLaFtxW0stqq3cU9dCeHGC-Tl5rMzevbd8&key=AIzaSyD5cWTcxuWVXgeN4J80BUC-nkk8sL8Oaqw") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "GamesandPlaytimeFun.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')



with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLaFtxW0stqq3_lGzv2goq4nt9egisUarN&key=AIzaSyDnnQb152LtaUR3dBCXNDoRbuV7cGdtb6I") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "UnboxingBatteryPoweredRideOnCars.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')



with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLaFtxW0stqq0VSC-fsak1wYeM8h3_FOWI&key=AIzaSyD5cWTcxuWVXgeN4J80BUC-nkk8sL8Oaqw") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "PlayDohSurpriseEgg.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')


