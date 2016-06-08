from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.movie_list, name="movie_list"),
    #url(r'^review/new/$', views.review_new, name="review_new"),
    url(r'^(?P<slug>[\w-]+)/$', views.movie_detail, name="movie_detail"),
    #url(r'^review/(?P<slug>[\w-]+)/edit/$', views.review_edit, name="review_edit"),
    #url(r'^review/(?P<slug>[\w-]+)/publish/$', views.review_publish, name="review_publish"),
    #url(r'^review/(?P<slug>[\w-]+)/unpublish/$', views.review_unpublish, name="review_unpublish"),
    #url(r'^review/(?P<slug>[\w-]+)/delete/$', views.review_delete, name="review_delete"),
    #url(r'^drafts/$', views.review_draft_list, name="review_draft_list"),
]
