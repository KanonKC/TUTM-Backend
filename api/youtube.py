from decouple import config
import requests

CREDENTIAL = config("YOUTUBE_API_KEY")

def secondFormat(duration):
    second = 0
    number = ""
    for i in range(2,len(duration)):
        if duration[i] == "H":
            second += int(number)*3600
            number = ""
        elif duration[i] == "M":
            second += int(number)*60
            number = ""
        elif duration[i] == "S":
            second += int(number)
            number = ""
        else:
            number += duration[i]
    return second

def getVideoData(url):
    snippet = requests.get(f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={url}&key={CREDENTIAL}").json()
    contentDetails = requests.get(f"https://www.googleapis.com/youtube/v3/videos?part=contentDetails&id={url}&key={CREDENTIAL}").json()
    if 'error' in snippet:
        return None
    return {
        "title": snippet['items'][0]['snippet']['title'],
        "channel_title": snippet['items'][0]['snippet']['channelTitle'],
        "description": snippet['items'][0]['snippet']['description'],
        "thumbnail": snippet['items'][0]['snippet']['thumbnails']['medium']['url'],
        "url": url,
        "duration": secondFormat(contentDetails['items'][0]['contentDetails']['duration'])
    }

def search_video(text):
    result = requests.get(f"https://youtube.googleapis.com/youtube/v3/search?q={text}&type=video&part=snippet&key={CREDENTIAL}").json()
    if 'error' in result:
        return []
    return [{**i['snippet'],"id":i['id']} for i in result['items']]

def search_playlist(playlistId):
    result = requests.get(f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={playlistId}&maxResults=50&key={CREDENTIAL}").json()
    print(result)
    if 'error' in result:
        return []
    return [{**i['snippet'],"id":i['id']} for i in result['items']]