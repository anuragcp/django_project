from django.conf.urls import url, include

from .views import StatusListSearchAPIView

urlpatterns = [
    url(r'^$', StatusListSearchAPIView.as_view()),
    # url(r'^create/$', StatusCreateAPIView.as_view()),
    # url(r'^(?P<id>.*)/$', StatusDetailAPIView.as_view()),
    # url(r'^(?P<id>.*)/update/$', StatusUpdateAPIView.as_view()),
    # url(r'^(?P<id>.*)/delete/$', StatusDeleteAPIView.as_view()),
]


# api/status/ -> ListView
# api/status/create -> create
# api/status/12/ -> Detail
# api/status/12/update -> Update
# api/status/12/delete -> delete
