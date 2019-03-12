from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.

class crwl:
    
    def blockchain(request):
        r = requests.get('https://news.google.com/search?q=%EB%B8%94%EB%A1%9D%EC%B2%B4%EC%9D%B8&hl=ko&gl=KR&ceid=KR%3Ako') 
        # s_idx = 0
        # e_idx = 0
        # while True:
        #     s_idx = r.find('<>', e_idx)
        #     if s_idx ==-1:
        #         break
        #     e_idx = r.find('</>',s_idx)
        #     print(r[s_idx+4:e_idx])
        print(r.text)
        return render(request,'crawlingapp/blockchain.html',{})
    
    def basic(request):
        return render(request,'crawlingapp/basic.html',{})