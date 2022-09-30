from rest_framework import routers
from .api import StaticViewSet, NotificetViewSet, FeedbackViewSet, InformationViewSet,UsersViewSet, PassajirViewSet, ErrorAppViewSet, CityLangViewSet

router = routers.DefaultRouter()
router.register('api/error', ErrorAppViewSet, 'error')
router.register('api/citylang', CityLangViewSet, 'citylang')
router.register('api/static', StaticViewSet, 'static')
router.register('api/notic', NotificetViewSet, 'notic')
router.register('api/feedback', FeedbackViewSet, 'feedback')
router.register('api/info', InformationViewSet, 'info')
router.register('api/users', UsersViewSet, 'users')
router.register('api/passajir', PassajirViewSet, 'passajir')

urlpatterns = router.urls
