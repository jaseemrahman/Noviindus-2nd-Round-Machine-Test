#Import from the core django
from django.urls import path
#Import from local app/library
from tree import views

urlpatterns = [
    path('',views.tree,name='tree'),
    path('table',views.table_view,name='table'),
    # path('last',views.last_child,name='last'),
    path('ajax',views.ajax_function,name='ajax'),
]