from django.urls import path
from .views import hello, HelloView, MonthPost, year_post,post_detail, my_view, TemplIf, veiw_for, view_index, view_about, author_post, pull_full, add_comment



urlpatterns = [
    path('hello/', hello, name='hello'),
    path('hello2/', HelloView.as_view(), name='hello2'),
    path('posts/<int:year>', year_post, name='year_post'),
    path('posts/<int:year>/<int:month>', MonthPost.as_view(), name='month_post'),
    path('posts/<int:year>/<int:month>/<slug:slug>', post_detail, name='post_detail'),
    path('', my_view, name='my_view'),
    path('if/',TemplIf.as_view(), name='templ_if'),
    path('for/', veiw_for, name='veiw_for'),
    path('index/', view_index, name='view_index'),
    path('about/', view_about, name='view_about'),
    path('author/<int:author_id>', author_post, name='author_post'),
    path('post/<int:post_id>', pull_full, name='post_full'),
    path('add_com/<int:id_post>', add_comment, name='add_newcomment'),
]


