from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.review_list, name="review_list"),
    url(r'^review/(?P<pk>\d+)/$', views.review_detail, name="review_detail"),
    url(r'^review/new/$', views.review_new, name="review_new"),
    url(r'^review/(?P<pk>\d+)/edit/$', views.review_edit, name="review_edit"),
    url(r'^review/(?P<pk>\d+)/publish/$', views.review_publish, name="review_publish"),
    url(r'^review/(?P<pk>\d+)/unpublish/$', views.review_unpublish, name="review_unpublish"),
    url(r'^review/(?P<pk>\d+)/delete/$', views.review_delete, name="review_delete"),
    url(r'^drafts/$', views.review_draft_list, name="review_draft_list"),
]
