from django.conf.urls import url
from example import views

# SET THE NAMESPACE
app_name = 'example'

urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^add_object/$',views.add_object,name='add_object'),
]
