from django.conf.urls import url
from . import views

app_name = "cart"

urlpatterns = [
    url(r'^categories/$', views.CategoryList.as_view(), name="categories"),
    url(r'^categories/(?P<cat_id>\d+)/$', views.show_category, name="show_category" ),
    url(r'^add_to_cart/$', views.add_to_cart, name='add_to_cart'),
    url(r'^cart/$', views.show_cart, name='show_cart'),
]
