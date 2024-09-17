from rest_framework import routers
from .views import TaskViewSet

router = routers.DefaultRouter()
router.register(r'task', TaskViewSet, basename = 'task')

urlpatterns = router.urls 