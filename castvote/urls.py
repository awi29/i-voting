from django.conf.urls import url

app_name = 'castvote'

urlpatterns = [
	url(r'^$','castvote.views.voting',name='voting'),
	url(r'^done/$','castvote.views.storevote', name='storevote')
]
