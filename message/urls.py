from django.conf.urls import url
from message.views import MessageView

urlpatterns = [
    url(r'(?P<name>)(?P<message>)', MessageView.as_view(), name='message'),
]
