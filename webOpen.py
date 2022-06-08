import webbrowser
import requests
from bs4 import BeautifulSoup
import threading
import smtplib
import urllib.request
import os

# to download yt video
from pytube import YouTube



def latestNews(news=3):
	URL = 'https://indianexpress.com/latest-news/'
	result = requests.get(URL)
	src = result.content

	soup = BeautifulSoup(src, 'html.parser')

	headlineLinks = []
	headlines = []

	divs = soup.find_all('div', {'class': 'title'})

	count = 0
	for div in divs:
		count += 1
		if count > news:
			break
		a_tag = div.find('a')
		headlineLinks.append(a_tag.attrs['href'])
		headlines.append(a_tag.text)

	return headlines



def openWebsite(url='https://www.google.com/'):
	webbrowser.open(url)

def openWebsiteByName(query):
    query = query.replace('open', '')
    query = query.replace('website', '')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53'
    }
    page = requests.get('https://google.com/search?q=' +
                        query, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    print("Searching for website...")
    soup = BeautifulSoup(page.content, "html.parser")
    # got name of class using inspect element cite class
    result = soup.find(class_='iUh30 qLRx3b tjvcx').get_text()
    result = result.replace(' › ...', '')
    result = result.replace('https://www.','')
    result = result.replace('http://www','')
    
    print(result)
    webbrowser.open('http://www.'+result)

def handleQuery(query):

    URL = "https://www.google.co.in/search?q=" + query

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53'
    }

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    # got name of class using inspect element
    result = soup.find(class_='Z0LcW').get_text()
    return result


def youtube(query):
	query = query.replace('play', ' ')
	query = query.replace('on youtube', ' ')
	query = query.replace('youtube', ' ')

	print("Searching for videos...")
	from youtubesearchpython import VideosSearch
	videosSearch = VideosSearch(query, limit=1)
	results = videosSearch.result()['result']
	print("Finished searching!")

	webbrowser.open('https://www.youtube.com/watch?v=' + results[0]['id'])
	return "Enjoy..."

# for downloading yt video
def get_itag(yt=None):
    tag_audio = list(yt.streams.filter(only_audio=True))
    tag_video = list(yt.streams.filter(file_extension='mp4'))

    audio_itag = {}
    video_itag = {}
    video_itag_nosound = {}
    all_res = []

    i = 1
    for stream in tag_audio:
        stream = f'{stream}'
        stream = stream.split(' ')
        itag, abr = stream[1], stream[3]
        itag_num = itag.split('"')[1]
        abr_num = abr.split('"')[1]

        audio_itag[i] = {abr_num: itag_num}
        i += 1

    j = 1
    for stream in tag_video:
        stream = f'{stream}'
        stream = stream.split(' ')
        itag, res, fps, pro = stream[1], stream[3], stream[4], stream[-2]

        if 'True' in pro:
            if 'res' in res:
                itag_num = itag.split('"')[1]
                res_num = res.split('"')[1]
                fps_num = fps.split('"')[1]

                video_itag[j] = {f'{res_num}-{fps_num}': itag_num}
                j += 1

        else:
            if 'res' in res:
                if res not in all_res:
                    all_res.append(res)

                    itag_num = itag.split('"')[1]
                    res_num = res.split('"')[1]
                    fps_num = fps.split('"')[1]

                    video_itag_nosound[j] = {
                        f'no-sound-{res_num}-{fps_num}': itag_num}
                    j += 1

    return audio_itag, video_itag, video_itag_nosound


def download_by_itag(PATH, itag=None, type='mp4', yt=None, title=None):
    stream = yt.streams.get_by_itag(itag)
    if type == 'mp3':
        stream.download(PATH, f'audio.{type}')
    else:
        stream.download(PATH, f'video.{type}')

def downloadVideo(query):
	query = query.replace('download', '')
	query = query.replace('from youtube', '')
	query = query.replace('from yt', '')

	from youtubesearchpython import VideosSearch
	videosSearch = VideosSearch(query, limit=1)
	results = videosSearch.result()['result']
	print("Finished searching!")

	URL = 'https://www.youtube.com/watch?v=' + results[0]['id']

	yt = YouTube(URL)

	title = yt.title
	print(f'!Downloading : {title}')
	audio_itag, video_itag, video_itag_nosound = get_itag(yt)
	save_title = query

	qt = 2  # currently 720p resolution
	if qt <= len(video_itag):
		itag = int(list(video_itag[qt].values())[0])
	else:
		itag = int(list(video_itag_nosound[qt].values())[0])
	
	download = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads')

	PATH = os.path.join(download, title)
	print(f'\ndownloading video.. {title}')
	download_by_itag(PATH, itag, 'mp4', yt, 'video')

	print('download successfull... check "Downloads" folder...')


def googleSearch(query):
    if 'image' in query:
        query += "&tbm=isch"
    
    query = query.replace('images', '')
    query = query.replace('image', '')
    query = query.replace('search', '')
    query = query.replace('show', '')
    query = query.replace('on google','')

    webbrowser.open("https://www.google.com/search?q=" + query)
    return "Here you go..."


def downloadImage(query, n=2):
	query = query.replace('of', '')
	query = query.replace('images', '')
	query = query.replace('image', '')
	query = query.replace('download', '')
	URL = "https://www.google.com/search?tbm=isch&q=" + query
	result = requests.get(URL)
	src = result.content

	soup = BeautifulSoup(src, 'html.parser')
	imgTags = soup.find_all('img', class_='yWs4tf')  # old class name -> t0fcAb

	if os.path.exists('Downloads') == False:
		os.mkdir('Downloads')

	count = 0
	for i in imgTags:
		if count == n:
			break
		try:
			urllib.request.urlretrieve(i['src'], 'Downloads/' + str(count) + '.jpg')
			count += 1
		except Exception as e:
			raise e
	print('Downloaded', count,'images')


if __name__ == "__main__":
    #downloadImage('download images of cat')
    #googleSearch('search tom cruise on google')
    #youtube("play gangnum style on youtube")
    #openWebsiteByName('open apple website')
    #openWebsite()
    #print(weather())
	downloadVideo('download rainy day short 30 sec animation video')

    #print(latestNews())

    #print(handleQuery("age of milky way"))
    #print(handleQuery("height of mount everest"))
    #print(handleQuery("when was Aryabhatta born"))
    #print(handleQuery("prime minister of india"))
    #print(handleQuery("what is the population of india"))
