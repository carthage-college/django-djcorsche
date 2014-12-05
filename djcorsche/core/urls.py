from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(
        r'^students', include('djcorsche.students.urls')
    ),
    url(
        r'^$', 'djcorsche.core.views.home', name="home"
    ),
)
