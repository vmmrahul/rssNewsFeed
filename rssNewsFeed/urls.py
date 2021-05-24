"""rssNewsFeed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from view import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admins', login, name='loginPage'),
    path('dashboard', dashboard, name='dashboard'),
    path('signout', signout, name='signout'),
    path('changePassword', changePassword, name='changePassword'),
    # category Work Start
    path('addcateogry', addcateogry, name='addcateogry'),
    path('addCategoryAction', addCategoryAction, name='addCategoryAction'),
    path('viewCategory', viewCategory, name='viewCategory'),
    path('deletCategroy', deletCategroy, name='deletCategroy'),
    path('editCategoryPage', editCategoryPage, name='editCategoryPage'),
    path('editCategoryAction', editCategoryAction, name='editCategoryAction'),
    # End of category Work
    path('addNewsPage', addNewsPage, name='addNewsPage'),
    path('viewNews', viewNews, name='viewNews'),
    path('deleteNews/<int:id>', deleteNews, name='deleteNews'),
    path('viewNewsDescription', viewNewsDescription, name='viewNewsDescription'),
    path('addNewsVedio', addNewsVedio, name='addNewsVedio'),
    path('addNewsVedioAction', addNewsVedioAction, name='addNewsVedioAction'),
    path('deleteNewsVedio', deleteNewsVedio, name='deleteNewsVedio'),

    #
    path('', Home, name='Home'),
    path('viewMyNews', viewMyNews, name='viewMyNews'),
    path('navbarCategoryNews', navbarCategoryNews, name='navbarCategoryNews'),
    path('vedioNews', vedioNews, name='vedioNews'),
    path('contactus', contactus, name='contactus'),
    path('AllNewsViews', AllNewsViews, name='AllNewsViews'),
]
