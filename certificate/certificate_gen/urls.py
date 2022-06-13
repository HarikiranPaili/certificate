from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('add_event', add_event ,name='add_event'),
    path('preview', preview ,name='preview'),
    path('certificate', download ,name='certificate'),
    path('edit_event/<str:pk>', edit_event, name='edit_event'),
    path('edit_sign/<str:pk>', edit_sign, name='edit_sign'),
    path('update/<str:event_name>', update_event, name='update_event'),
    path('update_sign/<str:pk>', update_sign, name='update_sign'),

    # path('create', create_new_student, name='create'),
    # path('sum', sum_of_natural, name='sum'),
    # path('edit/<str:pk>', edit, name='edit'),
    # path('update/<str:pk>', update, name='update'),
    # path('Delete/<str:pk>', Delete, name='Delete'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
