from django.db import models
from django.utils.timezone import utc
import datetime
# Create your models here.
NEWS_CATEGORY =(
    ('W',"World"),#https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen
    ('C',"Country"),#https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRE55YXpBU0FtVnVLQUFQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen
    ('T',"Technology"),#https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen
    ('B',"Business"),#https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen
    ('SC',"Science"),#https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp0Y1RjU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen
    ('E',"Entertainment"),#https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen
    ('S',"Sports"),#https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen
    ('H',"Health"),#https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtVnVLQUFQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen   
)
class NewsData(models.Model):
<<<<<<< HEAD
    title = models.CharField(max_length=255,blank=True, null=True)
=======
    title = models.CharField(max_length=100,blank=True, null=True)
>>>>>>> 268cc11f3259bf84d8428935cd9653ecf7c8c766
    link = models.TextField()
    image = models.TextField()
    website = models.CharField(max_length=255,blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    def __str__(self):
        return self.title

    def get_time_diff(self):
        if self.time:
            now = datetime.datetime.utcnow().replace(tzinfo=utc)
            timediff = now - self.time
            return round(timediff.total_seconds()//3600)

class Category(models.Model):
    category = models.CharField(max_length=2,choices=NEWS_CATEGORY,default="W")
    url = models.URLField()
<<<<<<< HEAD
    views = models.IntegerField(default=0)
=======
>>>>>>> 268cc11f3259bf84d8428935cd9653ecf7c8c766

    def __str__(self):
        return self.category

<<<<<<< HEAD
class IP(models.Model):
    IP = models.GenericIPAddressField()
    visit_to = models.CharField(max_length=3,choices=NEWS_CATEGORY,default="W")

    def __str__(self):
        return self.IP


=======
>>>>>>> 268cc11f3259bf84d8428935cd9653ecf7c8c766
    