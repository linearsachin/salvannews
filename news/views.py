from django.shortcuts import render,redirect
from django.views.generic import CreateView,View,ListView,UpdateView,TemplateView
from django.http import HttpResponse,HttpResponseRedirect
from .models import NewsData,Category,NEWS_CATEGORY,IP
import datetime


class Homeview(ListView):
    def get(self, request, *args, **kwargs): 
        news1 = NewsData.objects.all().order_by('-time')  
        news =  delete_news_after_30(news1)
        context={
            'NewsData':news,
            'category':NEWS_CATEGORY,
            'my': "W"
        }
        return render(request,'news/home.html',context)


def category_news(request,category,*args,**kwargs):
        category_ = Category.objects.get(category=category)
        # ip = request.META.get('REMOTE_ADDR')

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
            allip = IP.objects.filter(IP=ip,visit_to = category_.category )
            if not allip.exists():
                IP.objects.create(IP=ip,visit_to = category_.category)
                category_.views = category_.views + 1
                category_.save()
        else:
            ip = request.META.get('REMOTE_ADDR')
            allip = IP.objects.filter(IP=ip,visit_to = category_.category )
            if not allip.exists():
                IP.objects.create(IP=ip,visit_to = category_.category)
                category_.views = category_.views + 1
                category_.save()

            
        news1 = NewsData.objects.filter(category=category_).order_by('-time')

        news = delete_news_after_30(news1)
        
        context = {

            'selman':category_,
            'my':category,
            'NewsData':news,
            'category':NEWS_CATEGORY,
        }
   
        return render(request,'news/category_news.html',context)

def delete_news_after_30(news):
    for news_ in news:
        if news_.get_time_diff() > 30:
            news_.delete()
        
    return news

    


    
        
# def views(request,category,*args,**kwargs):
#     views = Category.objects.get(category=category)
#     context = {
#         'views' : views.views
#     }
#     return render(request, 'footer.html',context)
