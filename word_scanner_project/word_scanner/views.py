# word_scanner/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ScannedArticle, Word
import json
# @login_required
def scan_article(request):
    # 处理扫描文章的逻辑
    if request.method == 'POST':
        # title = request.POST['title']
        # content = request.POST['content']
         # 读取请求数据流并缓存
        request_data = request.body

        # 解析JSON数据
        data = json.loads(request_data)
        print(data)
        # article = ScannedArticle.objects.create(user=request.user, title=title, content=content)
        
        words = data.split() 
        for word in words:
            print(word)
            return word
            # Word.objects.create(article=article, word=word)
    
    return render(request, 'scan_article.html')
