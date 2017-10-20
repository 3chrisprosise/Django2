"""Django2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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

from django.urls import path
from . import views
app_name = 'Basic'
# 使用url反转的话就得指明 app_name 而且是必须存在的
urlpatterns = [


    # path('', views.index, name='index'),
    # path('polls/<int:question_id>/', views.detail, name='detail'),
    # path('polls/<int:question_id>/results/', views.results, name='results'),
    # path('polls/<int:question_id>/vote/', views.vote, name='vote'),

    # 以上为复杂化实现的view和url机制，下面介绍更为简单的url机制

    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('homework', views.homework),
    path('md5', views.md5_test)
]


