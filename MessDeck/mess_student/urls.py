from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views

from .views import Home,CreateProfile,view_profile,view_menu,CreateReview,DetailReview,ExcelFileUpdateView,ExcelFileCreateView,MenuList,MenuDetail,rate_items,calc_avg_rating,mark_attendance,Home,Bill_List,check_new_user,AttendeeList,convert_bill_to_excel

urlpatterns=[
    #path('',),
    path('',Home,name='home'),
    path('staffloginpage/',auth_views.LoginView.as_view(template_name='login.html'), name='LoginPage'),
    path('stafflogoutpage/',auth_views.LogoutView.as_view(template_name='logout.html'), name='LogoutPage'),
    path('createprofile/',CreateProfile,name='createprofile'),
    path('profile/',view_profile,name='profile'),
    path('scanmenu/',view_menu,name='menu'),
    path('writereview/',CreateReview.as_view(),name='createreview'),
    path('reviews/',DetailReview.as_view(),name='reviewlist'),
     path('changemenu/', ExcelFileCreateView.as_view(), name='upload-excel'),
    #path('updatemenu/<int:pk>/', ExcelFileUpdateView.as_view(), name='update-excel'),
    path('viewmenu/',MenuList.as_view(),name='viewmenu'),
    path('viewmenu/<int:pk>/',MenuDetail.as_view(),name='viewmenudetail'),
    path('viewmenu/<int:pk>/rate/',rate_items,name='rate'),
    path('viewmenu/<int:pk>/avgrate/',calc_avg_rating,name='avgrate'),
    path('mark_attendance/',mark_attendance,name='mark_attendance'),
     path('billlist/', Bill_List.as_view(), name='bill_list'),
     path('checkuser/',check_new_user, name='check_user'),
     path('attend_list/',AttendeeList.as_view(),name='attendance'),
    path('convert_to_excel/<int:pk>/',convert_bill_to_excel,name='convert_to_excel')

     

     

    











]