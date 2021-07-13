from django.urls import re_path
from . import views
urlpatterns = [
    # 判断用户名是否重复
    re_path('^/$',views.UsernameCountView.as_view()),
]