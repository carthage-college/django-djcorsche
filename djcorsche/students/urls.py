from django.conf.urls.defaults import *

urlpatterns = patterns('djcorsche.students.views',
    url(
        r'^getstudentexams/$',
        'getstudentexams', name="getstudentexams"
    ),
    url(
        r'^searchwithincourse/$',
        'getjquerystudents', name="getjquerystudents"
    ),
    url(
        r'^addtoexamrec/$',
        'addtoexamrec', name="addtoexamrec"
    ),
    url(
        r'^removefromexamrec/$',
        'removefromexamrec', name="removefromexamrec"
    ),
    url(
        r'^prepopulate/$',
        'prepopulatestudents', name="prepopulatestudents"
    ),
    url(
        r'^getcourses/$',
        'getcourses', name='getcourses'
    ),
)
