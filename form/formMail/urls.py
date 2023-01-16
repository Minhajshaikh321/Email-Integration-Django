from django.urls import path
from .import views
# from .views import Update_Short_Question
urlpatterns=[
    path('',views.home,name='homepage'),
    path('showdata',views.showData,name='showdata'),
    path('email/<int:id>',views.sendMessage,name='sendmsg'),
    path('email/all/',views.sendMessageall,name='sendall'),
    # path('email/delete/<int:id>',views.deletemessage,name='dltmsg'),
   
]
