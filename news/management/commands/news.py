import requests 
from bs4 import BeautifulSoup 
import csv 
from django.core.management.base import BaseCommand
from news.models import Category, NewsData




class Command(BaseCommand):
    help = "collect news"
    def get_news(self,url):
        try:

            URL = url
            print(URL)
            headers = {
                "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
            }

            r = requests.get(URL,headers=headers) 
            soup = BeautifulSoup(r.content, 'html.parser')

            allNews = soup.find_all(class_="xrnccd F6Welf R7GTQ keNKEd j7vNaf", limit=10)
            news_for_you={}
            n=0
            for single_news in allNews:
                n+=1
                 
                title = single_news.find(class_="DY5T1d").text
        
                atag = single_news.find('a')
                href = atag['href'].replace(".","")
                link= 'https://news.google.com'+href
            
                # print(link)
                image_tag=  single_news.find(class_="tvs3Id QwxBBf")
                if image_tag is not None:
                    image = image_tag['src']
                else:
                    image="https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Google_News_icon.svg/768px-Google_News_icon.svg.png"
            
            
                website= single_news.find(class_="wEwyrc AVN2gc uQIVzc Sksgp").text


                time_tag=  single_news.find(class_="WW6dff uQIVzc Sksgp")
                time= time_tag['datetime']
                
               
                news_for_you['news'+str(n)]= {
                    'title':title,
                    
                    'link':link ,
                    'image':image,
                    'website':website, 
                    'time':time,
                    }
        except InterruptedError as e:
            print("Error occured")
        return news_for_you
    

    def handle(self, *args, **options):
        NEWS_CATEGORY =(
        'W',#https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen
        'C',#https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRE55YXpBU0FtVnVLQUFQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen
        'T',#https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen
        'B',#https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen
        'SC',#https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp0Y1RjU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen
        'E',#https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen
        'S',#https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen
        'H',#https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtVnVLQUFQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen   
        )

        for category in NEWS_CATEGORY:
            category = Category.objects.get(category=category)
            news=self.get_news(category.url) 
            n=0
            for new in news:
                n+=1
                news1=news['news'+str(n)]
                title=news1['title']
                link=news1['link']
                image=news1['image']
                website=news1['website']
                time=news1['time']
                NewsData.objects.get_or_create(
                   title=title,
                    website=website,
                    category=category,
                    time=time 
                )
                newss = NewsData.objects.get(title=title,
                    website=website,
                    category=category,
                    time=time)
                newss.link=link
                newss.image=image
                newss.save()
            





