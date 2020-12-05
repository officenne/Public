git pull



cd C:\Users\medisaapps\Public\Android\EgyptApps\Madrestna

curl "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCnxju7_Ug6VbC6en6tBL6Aw&type=video&order=date&maxResults=100&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI" > Madrestna_Channel.json


curl "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCnxju7_Ug6VbC6en6tBL6Aw&type=video&eventType=live&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI" > Madrestna_Channel_Live.json


curl "https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&channelId=UCnxju7_Ug6VbC6en6tBL6Aw&q=%D8%A7%D9%84%D8%B5%D9%81+%D8%A7%D9%84%D8%AB%D8%A7%D9%86%D9%89&maxResults=50&order=date&key=AIzaSyCT6mFtx_a5gqWpvjnSnUS7lDd6wrrLmgI" > Madrestna_M2.json


git add -A


git commit -m "file updated "



git push origin master



