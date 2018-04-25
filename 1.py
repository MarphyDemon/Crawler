

page = 1
class AsySpider(object):
    """A simple class of asynchronous spider."""
    def __init__(self, urls, concurrency):
        urls.reverse()
        self.urls = urls
        self.concurrency = concurrency
        self._q = queues.Queue()
        self._fetching = set()
        self._fetched = set()
        
    def handle_page(self, url, html):
        global page
        ......

def run_spider(city):
    urls = []
    urls.append('https://www.lagou.com/jobs/positionAjax.json?px=new&city='+city+'&needAddtionalResult=false')
    s = AsySpider(urls, 16)
    s.run()
def main():
    p = Pool()
    for (i,) in results:
        res.append(i)
    for i in res:
        p.apply_async(run_spider, args=(i,))

    django-admin startproject project         #创建project项目
    python3 manage.py startapp backend         #进入项目根目录创建backend




    url(r'^$', TemplateView.as_view(template_name="index.html")),   #urls.py中配置
    #settings.py下配置
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': ['frontend/dist'],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "frontend/dist/static"),
    ]