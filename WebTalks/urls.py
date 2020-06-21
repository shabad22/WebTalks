from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as users_views

# Text for admin page
admin.site.site_header = "WebTalks Admin Page"
admin.site.index_title = "Admin Panel" 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', users_views.register, name='register'),
    path('profile/', users_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    # path('reset-pass/', auth_views.PasswordResetView.as_view(template_name='users/reset_pass.html'), name='reset-pass'),
    # path('reset-pass/email-sent', auth_views.PasswordResetDoneView.as_view(template_name='users/reset_pass_done.html'), name='reset-pass-done'),
    # path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='reset-pass-confirm'),
    path('', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)