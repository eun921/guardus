from django.conf.urls import include, url
# from rest_framework.routers import DefaultRouter
from . import views
from django.conf import settings
from django.conf.urls.static import static

# router=DefaultRouter()
# router.register('post',views.PostViewSet)
# router.register('comment',views.CommentViewSet)


urlpatterns=[
    url('api-auth/',include('rest_framework.urls')),
    url(r'^$',views.PostViewSet.as_view(),name='post'),
    url(r'^comment/$',views.CommentViewSet.as_view(),name='comment'),
    url(r'^post/$',views.PostViewSet.as_view(),name='post'),
    url(r'^post/create/$',views.CreateViewSet.as_view(),name='create'),
    url(r'^post/(?P<pk>\d+)/$', views.DetailViewSet.as_view(), name='detail'),
    url(r'^post/(?P<pk>\d+)/update/$', views.UpdateViewSet.as_view(), name='update'),
    url(r'^post/(?P<pk>\d+)/delete/$', views.DeleteViewSet.as_view(), name='delete'),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
