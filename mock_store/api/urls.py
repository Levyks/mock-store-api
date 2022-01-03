from django.urls import path

from .views import resources, auth

urlpatterns = [

    path('csrf/', auth.CsrfView.as_view(), name='csrf'),

    # Auth
    path('auth/login/', auth.LoginView.as_view(), name='login'),
    path('auth/logout/', auth.LogoutView.as_view(), name='logout'),
    path('auth/whoami/', auth.WhoAmIView.as_view(), name='whoami'),
    path('auth/change-password/', auth.ChangePasswordView.as_view(), name='change-password'),

    # Resources
    path('products/', resources.ProductList.as_view(), name='products'),
    path('products/<int:pk>/', resources.ProductDetail.as_view(), name='product-detail'),
    path('categories/', resources.CategoryList.as_view(), name='categories'),
    path('categories/<int:pk>/', resources.CategoryDetail.as_view(), name='category-detail'),
]
