from django.urls import path

from . import views

urlpatterns = [
path('form/',views.student_form, name='student_insert' ),
path('form/<int:id>/',views.student_form, name='student_update' ),
path('studentlist/',views.student_list, name='student_list'),
path('delete/<int:id>/',views.student_delete, name='student_delete')
    ]