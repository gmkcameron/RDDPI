from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import TemplateView

from backend.views import medico_view, pacientes_view, prontuario_view

from .views.admin_dashboad_view import dashboard_admin
from .views.contact_view import contato
from .views.dashboard_handle_view import dashboard

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name="index"),
    path('sobre/', TemplateView.as_view(template_name='sobre.html'), name='sobre'),
    path('contato/', contato, name='contato'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login.html'), name='logout'),
    path('dashboard/admin/', dashboard_admin, name='dashboard_admin'),
    path('dashboard/', dashboard, name='dashboard'),
    
    path('paciente/list/', pacientes_view.paciente_list, name='paciente_list'),
    path('paciente/create/', pacientes_view.paciente_create, name='paciente_create'),
    path('paciente/delete/<int:id>', pacientes_view.paciente_delete, name='paciente_delete'),
    path('paciente/detail/<int:id>', pacientes_view.paciente_detail, name='paciente_detail'),
    path('paciente/update/<int:id>', pacientes_view.paciente_update, name='paciente_update'),
    
    path('medico/list/', medico_view.medico_list, name='medico_list'),
    path('medico/create/', medico_view.medico_create, name='medico_create'),
    path('medico/detail/<int:id>/', medico_view.medico_detail, name='medico_detail'),
    path('medico/update/<int:id>/', medico_view.medico_update, name='medico_update'),
    path('medico/delete/<int:id>', medico_view.medico_delete, name='medico_delete'),


    path('prontuario/list/', prontuario_view.prontuario_list, name='prontuario_list'),
    path('prontuario/create/', prontuario_view.prontuario_create, name='prontuario_create'),
    path('prontuario/detail/<int:id>/', prontuario_view.prontuario_detail, name='prontuario_detail'),
    path('prontuario/update/<int:id>/', prontuario_view.prontuario_update, name='prontuario_update'),
    path('prontuario/delete/<int:id>/', prontuario_view.prontuario_delete, name='prontuario_delete'),
    
 ]
