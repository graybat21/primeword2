"""primeword_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view

from record.views import StudyRecordDetail, StudyRecordList, TestRecordList, TestRecordDetail
from users.views import ProfileList, ProfileDetail, SchoolGroupList, AcademyGroupDetail, SchoolGroupDetail, \
    AcademyGroupList, UserTextbookList
from .api import router

schema_view = get_swagger_view(title='Primeword API')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^swagger/', schema_view),

    url(r'^users/$', ProfileList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', ProfileDetail.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/textbooks/$', UserTextbookList.as_view()),

    url(r'^schools/$', SchoolGroupList.as_view()),
    url(r'^schools/(?P<pk>[a-z]+)/$', SchoolGroupDetail.as_view()),
    url(r'^academies/$', AcademyGroupList.as_view()),
    url(r'^academies/(?P<pk>[a-z]+)/$', AcademyGroupDetail.as_view()),

    url(r'^studyrecords/$', StudyRecordList.as_view()),
    url(r'^studyrecords/(?P<pk>[a-z]+)/$', StudyRecordDetail.as_view()),
    url(r'^testrecords/$', TestRecordList.as_view()),
    url(r'^testrecords/(?P<pk>[a-z]+)/$', TestRecordDetail.as_view()),

    url(r'^', include(router.urls))
]
