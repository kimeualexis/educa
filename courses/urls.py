from django.conf.urls import url
from . import views

app_name = 'courses'

urlpatterns = [
    url('mine/', views.ManageCourseListView.as_view(), name='manage_course_list'),
    url('create/', views.CourseCreateView.as_view(), name='course_create'),
    url('(?P<pk>\d+)/edit/', views.CourseUpdateView.as_view(), name='course_edit'),
    url('(?P<pk>\d+)/delete/', views.CourseDeleteView.as_view(), name='course_delete'),
    url('(?P<pk>\d+)/module/', views.CourseModuleUpdateView.as_view(), name='course_module_update'),

    url('module/(?P<module_id>\d+)/content/(?P<model_name>\w+)/create/', views.ContentCreateUpdateView.as_view(),
        name='module_content_create'),
    url('module/(?P<module_id>\d+)/content/(?P<model_name>\w+)/(?P<id>\d+)/', views.ContentCreateUpdateView.as_view(),
        name='module_content_update'),

    url('module/(?P<module_id>\d+)/', views.ModuleContentListView.as_view(), name='module_content_list'),
    url('content/(?P<id>\d+)/delete/', views.ContentDeleteView.as_view(), name='module_content_delete'),
    ]
