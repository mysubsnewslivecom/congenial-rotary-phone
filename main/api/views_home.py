from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework import generics, viewsets
from rest_framework.response import Response

from main.api import serializers
from main.utility.functions import Ipify, WebScrapping

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)


class IpifyAPI(generics.GenericAPIView):
    serializer_class = serializers.IpifySerializer

    @method_decorator(cache_page(CACHE_TTL))
    @method_decorator(vary_on_cookie)
    def get(self, request):
        ip = Ipify().get_ipify()
        serializer = self.serializer_class(ip)
        return Response(data=serializer.data)


class EPLListing(viewsets.ViewSet):
    serializer_class = serializers.EPLSerializer

    @method_decorator(cache_page(CACHE_TTL))
    @method_decorator(vary_on_cookie)
    def list(self, request):
        url = "https://onefootball.com/en/competition/premier-league-9/table"
        soup = WebScrapping(url=url, features="lxml").get_soup_text()
        table = soup.find_all("a", class_="standings__row-grid")
        team_list = list()
        for tab in table:
            list_temp = list()
            dict_temp = dict()
            list_temp = tab.text.split()
            dict_temp["position"] = int(list_temp[0])
            if len(list_temp) == 8:
                dict_temp["team"] = list_temp[1]
            elif len(list_temp) == 9:
                dict_temp["team"] = " ".join([list_temp[1], list_temp[2]])
            elif len(list_temp) == 10:
                dict_temp["team"] = " ".join([list_temp[1], list_temp[2], list_temp[3]])
            dict_temp["played"] = int(list_temp[-6])
            dict_temp["wins"] = int(list_temp[-5])
            dict_temp["draws"] = int(list_temp[-4])
            dict_temp["lost"] = int(list_temp[-3])
            dict_temp["goal_difference"] = int(list_temp[-2])
            dict_temp["points"] = int(list_temp[-1])
            team_list.append(dict_temp)

        return Response(team_list)


