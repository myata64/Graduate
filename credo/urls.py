"""
URL configuration for credo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views, settings
from django.conf.urls.static import static

app_name = 'credo'

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('error/', views.error, name='error'),
                  path('account/', views.account, name='account'),
                  path('addpost/', views.add_post, name='add_post'),
                  path('auth/', views.auth, name='auth'),
                  path('blog/', views.blog, name='blog'),
                  path('blog/', views.blog_2, name='blog_2'),
                  path('cart/', views.cart, name='cart'),
                  path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
                  # path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
                  path('catalog/gallery/', views.catalog_gallery, name='catalog_gallery'),
                  path('catalog/gallery/', views.catalog_gallery_2, name='catalog_gallery_2'),
                  path('catalog/list/', views.catalog_list, name='catalog'),
                  path('catalog/list/', views.catalog_list_2, name='catalog_list_2'),
                  path('catalog/table/', views.catalog_table, name='catalog_table'),
                  path('compare/', views.compare, name='compare'),
                  path('contacts/', views.contacts, name='contacts'),
                  path('elements/', views.elements, name='elements'),
                  path('', views.home, name='home'),
                  path('post/', views.post, name='post'),
                  path('product/', views.product, name='product'),
                  path('product/', views.product_2, name='product_2'),
                  path('wishlist/', views.wishlist, name='wishlist'),

                  path('register/', views.register, name='register'),
                  path('login/', views.login_view, name='login'),
                  path('logout/', views.logout_view, name='logout')

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
