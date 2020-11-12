from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create_emp, name="create-emp"),
    path('update/<int:emp_id>', views.update_emp, name="update"),
    path('delete/<int:emp_id>', views.delete_emp, name="delete"),
    path('', views.index, name="index")

]
