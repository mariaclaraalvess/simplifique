from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.tela_inicial, name='tela_inicial'),
    path('painel/', views.painel_controle, name='painel_controle'),
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout
    path('cadastro/', views.cadastro, name='cadastro'),  # Cadastro

    # Rotas para redefinição de senha
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
