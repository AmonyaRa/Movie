from rest_framework.routers import DefaultRouter

from applications.movie.views import MovieApiView, RelationApiView, LikeApiView

router = DefaultRouter()
router.register('relation/', RelationApiView)
router.register('like/', LikeApiView)
router.register('', MovieApiView)


urlpatterns = []

urlpatterns += router.urls
