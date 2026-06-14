from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from accounts.views import MeView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Autenticação
    path('api/auth/', include('accounts.urls')),
    path('api/auth/login/',
         TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/auth/refresh/',
         TokenRefreshView.as_view(),
         name='token_refresh'),
    path('api/me/', MeView.as_view(), name='user_me'),

    # Recurso protegido
    path('api/', include('journal.urls')),
]