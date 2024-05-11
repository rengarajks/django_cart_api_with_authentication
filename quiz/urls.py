from django.urls import path,include
from . import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('student',views.ProfileViewSet,basename="student_profile")


urlpatterns=[
    path('quiz/',views.QuizListView.as_view()),
    path('quiz/<int:id>',views.SingleQuizView.as_view()),
    path('auth/',include('djoser.urls')),
    path('profile/',include(router.urls))
]