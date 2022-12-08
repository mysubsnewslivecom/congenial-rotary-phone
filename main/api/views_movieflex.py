from django.conf import settings
from rest_framework.response import Response
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from rest_framework import viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

from main.api import serializers
from main.movieflex.models import Media, Watching
from main.utility import WebScrapping
from datetime import datetime
from main.utility.functions import LoggingService
from bs4 import BeautifulSoup as BS


log = LoggingService()

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)


# @method_decorator(cache_page(CACHE_TTL))
# @method_decorator(vary_on_cookie)
class MediaViewset(viewsets.ModelViewSet):
    serializer_class = serializers.MediaSerializer
    queryset = Media.objects.all()


class WatchingViewset(viewsets.ModelViewSet):
    serializer_class = serializers.WatchingSerializer
    queryset = Watching.objects.all()


class WebScrappingViewset(viewsets.ViewSet):
    serializer_class = serializers.WebscrapingSerializer

    @method_decorator(cache_page(CACHE_TTL))
    @method_decorator(vary_on_cookie)
    def list(self, request):
        rss_url = "https://animixplay.to/rss.xml"
        features = "xml"
        article_list = list()
        soup = WebScrapping(url=rss_url, features=features).get_soup()
        articles = soup.findAll("item")
        for a in articles:
            title = " ".join(str(a.find("title").text).split()[:-2])
            link = a.find("link").text
            ep = a.find("ep").text
            pub_date = a.find("pubDate").text
            description = a.find("description").text
            img = BS(description, 'html.parser').find("img").get("src")
            published = datetime.strptime(pub_date, "%a, %d %b %Y %H:%M:%S %z")
            published = published.strftime("%a, %d-%b-%Y %H:%M:%S")
            article = {
                "title": title,
                "link": link,
                "published": published,
                "ep": ep,
                "img": img,
            }
            article_list.append(article)
        return Response(article_list)

    def retrieve(self, request, pk=None):
        pass
