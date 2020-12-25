import urllib.request as request
import json
import os.path

# Get Latest from Youtube

YoutubeApiKey = 'AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI'
YoutubeChannelID = 'UCnxju7_Ug6VbC6en6tBL6Aw'
YoutubeUrl = 'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId='
YoutubeUrl2 = '&type=video&order=date&maxResults=100&key='

save_path = 'C:\GitHub\Public\Android\EgyptApps\Madrestna'


with request.urlopen(
        "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCnxju7_Ug6VbC6en6tBL6Aw&type=video&order=date&maxResults=100&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "Madrestna_Channel.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')
with request.urlopen(
        "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCnxju7_Ug6VbC6en6tBL6Aw&type=video&eventType=live&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "Madrestna_Channel_Live.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')
with request.urlopen(
        "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCZ-g-5yYrEI7KCLIDZAEF-w&type=video&order=date&maxResults=100&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "Madrestna_Channel2.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')




with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P"
        "-Q9VZESQd61-89p1wl_YEfK&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "science_الصف_الثاني_الإعدادي.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P"
        "-StWx58VVCwZVeHa9CLmoUR&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "Math_-_الصف_الخامس_الإبتدائي.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P-QAsd5JbXHJPfP7TAaHJiWG&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "Math_-_الصف_الثالث_الإعدادي.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P-SI1synglY_UyqYpA06wweO&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "Science_-_الصف_الرابع_الإبتدائي.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P-RYlJesJkWcrvFUKu-tCLUn&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "Science_-_الصف_الثالث_الإعدادي.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P-RpQ1xQ5g8x2aYcdWt22lMU&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "Math_-_الصف_الرابع_الإبتدائي.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P-SCMxv0SneDE4t37nU1nvas&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "Science_-_الصف_الخامس_الإبتدائي.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P-SYN6OB5xMFETS5TpjjY_dq&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "Math_-_الصف_الثاني_الإعدادي.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P-SrkoVw8e-zBTLIMNJ2uNQm&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "الصف_الأول_الإعدادي_-_Science.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P-RRJNABgwCyou-Wt52k_LWh&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "science_-_الصف_السادس_الإبتدائي.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P-TSV8y7TdwkONvHwBBz4lmX&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "Math_-_الصف_الأول_الإعدادي.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P-TYU5RUCbU51AP6s1ug8iu6&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "مادة_اللغة_العربية_-_الصف_الخامس_الابتدائى.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P-Qu58pIV1oE8igmbDSRzajD&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "مادة_العلوم_-_الصف_الثالث_الاعدادى.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P-QHpZxdUoAGCq1Iv6akymnA&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "مادة_اللغة_العربية_-_الصف_الثالث_الاعدادى.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P-TvM7vTuwAYgX_TxxDzvm3c&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "مادة_العلوم_-_الصف_الثانى_الاعدادى.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P-Qhnlc_rSYUNesHj49msNKP&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "مادة_اللغة_العربية_-_الصف_السادس_الابتدائى.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P-QqaEgETQzU1Cj2xlvNidpi&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "مادة_الرياضيات_-_الصف_الاول_الاعدادى.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P-ROjdJSTtfnTPMyaInMtWNP&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "مادة_اللغة_الانجليزية_-_الصف_الخامس_الابتدائى.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P-RDkeOkEAOFb-mkYTTKloky&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "مادة_العلوم_-_الصف_الرابع_الابتدائى.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P-ROJszrI38IIdYIjQFickvp&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "مادة_اللغة_الانجليزية_-_الصف_الرابع_الابتدائى.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P-QdvODlSGqw5wCo0uYn39Bq&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "مادة_الدراسات_الاجتماعية_-_الصف_الخامس_الابتدائى.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P-RptC967_xkaLJibs4XxxKv&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "مادة_الرياضيات_-_الصف_السادس_الابتدائى.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P-TFsBM-FDZC8lJSmXi1KXUz&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "مادة_الرياضيات_-_الصف_الثالث_الاعدادى.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P-QrX1EFMP49AJC49BaA21-4&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "مادة_اللغة_العربية_-_الصف_الثانى_الاعدادى.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P-QtSjdcMQhquvPlFt2GWPnr&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "مادة_الدراسات_الاجتماعية_-_الصف_الاول_الاعدادى.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P-R1QJw2yCO72bdM7j0r1XWf&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "مادة_اللغة_الانجليزية_-_الصف_السادس_الابتدائى.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P-Tu6OV8-4Jyys6Y63vnD7Il&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "مادة_العلوم_-_الصف_الخامس_الابتدائى.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P-Qub3yaiRzrJf7IpXPZL6x3&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "مادة_الدراسات_الاجتماعية_-_الصف_الرابع_الابتدائى.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P-SZDHzTroTdxIdRhvw8nS8k&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "مادة_اللغة_الانجليزية_-_الصف_الثالث_الاعدادى.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P-QiBLHS4cxZpnvidBZNqiQq&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "مادة_الدراسات_الاجتماعية_-_الصف_الثانى_الاعدادى.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P-QBWYWTbYoDSh46y5zJquyj&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "مادة_اللغة_العربية_-_الصف_الاول_الاعدادى.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P-QL1z0Ejd5x3j6yrHxIqKrO&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "مادة_الرياضيات_-_الصف_الثانى_الاعدادى.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P-Q1S4GkDHvEbQSjqZe0Vc8X&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "مادة_العلوم-_الصف_السادس_الابتدائى.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P-SKnqyHPo6qT0NkD23QjSzs&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "مادة_الرياضيات_-_الصف_الخامس_الابتدائى.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P-TyyW73tDWQDVhNSeV04HpS&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "مادة_الدراسات_الاجتماعية_-_الصف_الثالث_الاعدادى.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P-QnqKyzEtAq5ruJqSW9-vmF&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "اللغة_الانجليزية_-_الصف_الثانى_الاعدادى.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P-QWhTmTydrUTDZBm2iQTxNb&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "مادة_العلوم_-_الصف_الاول_الاعدادى.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P-Q4lNniG4RL2M-omcPFAhQe&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "مادة_اللغة_العربية_-_الصف_الرابع_الابتدائى.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P-RDluja-NGZ9aauvPu83bEU&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "مادة_الدراسات_الاجتماعية_-_الصف_السادس_الابتدائى.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P-RLlTlSiV1FDR1RSat78BFS&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "مادة_الرياضيات_-_الصف_الرابع_الابتدائى.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')

with request.urlopen(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=100&playlistId=PLZpdfXc71P-SN_FPj2ZCWLscTIfhHi-Go&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI") as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        # print(data)
        completeName = os.path.join(save_path, "اللغة_الانجليزية_-_الصف_الاول_الاعدادى.json")
        with open(completeName, 'w') as outfile:
            json.dump(data, outfile, indent=4)
    else:
        print('An error occurred while attempting to retrieve data from the API.')
