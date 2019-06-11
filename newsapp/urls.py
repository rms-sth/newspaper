from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


app_name = 'newsapp'


urlpatterns = [
    path('', ClientHomeView.as_view(), name='clienthome'),
    path('<int:pk>/detail/', ClientPostDetailView.as_view(), name='clientnewsdetail'),
    path('posts/topic/<int:pk>/', ClientPostTopic.as_view(), name='clientnewstopic'),
    path('posts/tag/<int:pk>/', ClientPostTag.as_view(), name='clientnewstag'),
    path('posts/category/<int:pk>/', ClientPostCategory.as_view(), name='clientnewscategory'),
    
    



    # CLIENT URL PATTERNS

    # path('', ClientHomeView.as_view(), name="clienthome"),
    # path('blogs/', ClientDemoView.as_view(), name="clientbloglist"),



    # ADMIN URL PATTERNS


    #  ADMIN AUTHENTICATION
    path('admin-login/', auth_views.LoginView.as_view(template_name='admintemplates/adminlogin.html'), name='adminlogin'),
    path('admin-logout/', auth_views.LogoutView.as_view(template_name='admintemplates/adminlogout.html'), name='adminlogout'),

    # ADMIN:NEWS CRUD
    path('admin-panel/news/',
         AdminNewsListView.as_view(),
         name='adminnewslist'),
    path('admin-panel/news/<int:pk>/detail/',
         AdminNewsDetailView.as_view(),
         name='adminnewsdetail'),
    path('admin-panel/news/create/',
         AdminNewsCreateView.as_view(),
         name='adminnewscreate'),
    path('admin-panel/news/<int:pk>/update/',
         AdminNewsUpdateView.as_view(),
         name='adminnewsupdate'),
    path('admin-panel/news/<int:pk>/delete/',
         AdminNewsDeleteView.as_view(),
         name='adminnewsdelete'),





    # path('album/create/', AdminGalleryCreateView.as_view(), name='adminalbumcreate'),
    

    path('album/create/', AdminGalleryView.as_view(), name='adminalbumcreate'),
#     path('album/delete/<int:pk>', AdminImageDeleteView.as_view(), name='adminalbumdelete'),
    path('album/delete/<int:pk>', adminDeleteImage, name='adminalbumdelete'),

    # path('album/<int:pk>/', AdminAlbumDetailView.as_view(), name='adminalbumlist'),


    # path('admin-panel/blog/create/',
    #      BlogCreateView.as_view(),
    #      name='adminblogcreate'),
    # path('admin-panel/blog/<int:pk>/update/',
    #      BlogUpdateView.as_view(),
    #      name='adminblogupdate'),
    # path('admin-panel/blog/<int:pk>/delete/',
    #      BlogDeleteView.as_view(),
    #      name='adminblogdelete'),

]
