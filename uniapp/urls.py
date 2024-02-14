from django.urls import path
from .views import *
urlpatterns = [
    path('',home),
    path('about',about),
    path('recruitment',recruitment),
    path('seo',seo),
    path('timecodes-translation',timecodes_translation),
    path('publishing',publishing),
    path('website-development',web_dev),
    path('qa-services',qa_services)
]