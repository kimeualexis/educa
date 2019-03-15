from django.conf.urls import url
from . import views

app_name = 'courses'

urlpatterns = [
    url('mine/', views.ManageCourseListView.as_view(), name='manage_course_list'),
    url('create/', views.CourseCreateView.as_view(), name='course_create'),
    url('(?P<pk>\d+)/edit/', views.CourseUpdateView.as_view(), name='course_edit'),
    url('(?P<pk>\d+)/delete/', views.CourseDeleteView.as_view(), name='course_delete'),
    url('(?P<pk>\d+)/module/', views.CourseModuleUpdateView.as_view(), name='course_module_update'),
]
