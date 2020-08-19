from django.urls import path, include
from . import api
urlpatterns = [
    # registration
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    # metadata
    path('metadata/', api.MetaDataListView.as_view()),
    path('metadata/<str:name>/', api.MetaDataListView.as_view()),

    # docs
    path('docs/', api.DocumentsListView.as_view()),
    path('docs/<str:name>/', api.DocumentsListView.as_view()),
]

