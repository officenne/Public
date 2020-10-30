git pull

cd C:\Users\medisaapps\Public\Youtube\mmoshaya


curl "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCPOw2O3_uZ1doro9iR4x6vw&type=video&order=date&maxResults=100&key=AIzaSyCYxmlE2_KKAPQkbo2TnyrzS_ujoVwBsrE" > mmoshaya.json

curl "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCmIp3opkQ6cEeJ6ybGrC_2A&type=video&order=date&maxResults=100&key=AIzaSyCYxmlE2_KKAPQkbo2TnyrzS_ujoVwBsrE" > mmoshaya2.json

curl "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCR60erWn2_8aoaLE3OoVu4w&type=video&order=date&maxResults=100&key=AIzaSyCYxmlE2_KKAPQkbo2TnyrzS_ujoVwBsrE" > Iman_Moshaya.json


cd C:\Users\medisaapps\Public\Youtube\KidsDianaShow

curl "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCk8GzjMOrta8yxDcKfylJYw&type=video&order=date&maxResults=100&key=AIzaSyCYxmlE2_KKAPQkbo2TnyrzS_ujoVwBsrE" > KidsDianaShow.json



cd C:\Users\medisaapps\Public\Android\EgyptApps\Madrestna

curl "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCGgeDgjIJ3GXZcLUnExAybw&type=video&order=date&maxResults=100&key=AIzaSyCYxmlE2_KKAPQkbo2TnyrzS_ujoVwBsrE" > Madrestna_Channel.json


curl "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCGgeDgjIJ3GXZcLUnExAybw&type=video&eventType=live&key=AIzaSyCYxmlE2_KKAPQkbo2TnyrzS_ujoVwBsrE" > Madrestna_Channel_Live.json




pause 


git add -A


git commit -m "file updated "



git push origin master


pause 
