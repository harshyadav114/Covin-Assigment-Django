"""
URL configuration for splitwise project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from expenses import views
from rest_framework.authtoken.views import obtain_auth_token
router = routers.DefaultRouter()


router.register(r'users', views.UserViewSet)
router.register(r'expense', views.ExpenseViewSet)
router.register(r'individual_expense', views.IndividualExpenseViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('create_expense/', views.CreateExpense.as_view()),
     path('api/user_balance/', views.user_balance, name='user_balance'),
    path('login/', views.CustomAuthToken.as_view()),
]


urlpatterns += router.urls
