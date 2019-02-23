import re
import requests
from concurrent import futures
import time
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'}
def download(_url):
    try:
        time.sleep(0.3)
        html3 = requests.head(_url,headers = headers)
        download_url = html3.headers['Location']
        
        video_file = requests.get(download_url,headers = headers)
        file_name = download_url.split('=')[-1]
        print(file_name)
    except:
        print('Error')
    with open(file_name + '.mp4','wb') as code:
        code.write(video_file.content)
def main():
    data_file = open('url.txt')
    data_url = data_file.read()
    data_url_list1 = data_url.split('\n')
    Threads = futures.ThreadPoolExecutor(min(Max_workers,len(data_url_list1)))
    for x in data_url_list1:
        html1 = requests.head(x)
        first_url = html1.headers['Location']
        html2 = requests.get(first_url,headers = headers)
        text_data = html2.text
        video_player_url1 = re.findall('playAddr: "(.*?)"',text_data,re.S)[0]
        video_player_url2 = video_player_url1.replace('wm','')
        #download(video_player_url2)
        Threads.submit(download,video_player_url2)
        
        
Max_workers = 5        
main()
