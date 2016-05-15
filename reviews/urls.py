from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.reviews_list, name="reviews_list"),
    url(r'^review/(?P<pk>\d+)/$', views.review_detail, name="review_detail"),
]
