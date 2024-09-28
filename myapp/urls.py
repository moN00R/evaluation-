from rest_framework.routers import DefaultRouter
from myapp.views import MyAppViewSet, UserViewSet, AdminMyAppViewSet, MyAppObjectsViewSet, ConfigurationViewSet

router = DefaultRouter()

router.register('my-app', MyAppViewSet, 'my-app')
router.register('my-app-objects', MyAppObjectsViewSet, 'my-app-objects')
router.register('user', UserViewSet, 'user')
router.register('admin-my-app', AdminMyAppViewSet, 'admin-my-app')
router.register('tax', ConfigurationViewSet, 'tax')

urlpatterns = router.urls 


