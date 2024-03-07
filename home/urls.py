from .views import home
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('home', home, basename='home')

urlpatterns = router.urls