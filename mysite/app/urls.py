from django.urls import path

from . import views

urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    # ex: /university/1/
    path('university/<int:univ_id>/', views.university_page, name='university'),
    # ex: /faculty/2/
    path('faculty/<int:fac_id>/', views.faculty_page, name='faculty'),
    # ex: /speciality/3/
    path('speciality/<int:spec_id>/', views.speciality_page, name='speciality'),
    # ex: /group/4/
    path('group/<int:group_id>/', views.group_page, name='group'),
]
