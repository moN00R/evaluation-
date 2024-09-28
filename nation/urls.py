from rest_framework.routers import DefaultRouter
from nation.views import (
    AdminCountryViewSet,
    AdminCityViewSet,
    AdminAreaViewSet,
    CountryViewSet,
    CityViewSet,
    AreaViewSet,
)


router = DefaultRouter()

router.register('admin-country', AdminCountryViewSet, 'admin-country')
router.register('admin-city', AdminCityViewSet, 'admin-city')
router.register('admin-area', AdminAreaViewSet, 'admin-area')
router.register('country', CountryViewSet, 'country')
router.register('city', CityViewSet, 'city')
router.register('area', AreaViewSet, 'area')

urlpatterns = router.urls
