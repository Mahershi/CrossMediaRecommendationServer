from rest_framework import routers
from .views import MovieViewSet
from django.urls import path
from .views import CastViewSet, TvViewSet, GameViewSet, BookViewSet, UserViewSet, ObtainAuthTokenViewSet, CreateExistingToken
from .views import MovieRatingViewSet, GenreViewSet, TvGenreViewSet, SearchViewSet
from .views import MovieListView, TvListView
from .views import InaccurateDataView, InaccurateRecomView, BrokenLinkView, MissingTitleView
from .views import MovieMovieViewSet, MovieTvViewSet, TvTvViewSet, MyListView

router = routers.DefaultRouter()
router.register('movies', MovieViewSet, basename='movies')
router.register('tv', TvViewSet, basename='tv')
router.register('games', GameViewSet, basename='games')
router.register('books', BookViewSet, basename='books')

router.register('users', UserViewSet, basename='users')
# router.register('rating/movie', MovieRatingViewSet, basename='movies/rating')
router.register('genres', GenreViewSet, basename='genres')
router.register('genres_tv', TvGenreViewSet, basename='tv_genres')
router.register('search', SearchViewSet, basename='search')
# router.register('my_list/movie', MovieListView, basename='movies_list')
# router.register('my_list/tv', TvListView, basename='tv_list')
router.register('my_list', MyListView, basename='my_list')
router.register('inaccurate_data', InaccurateDataView, basename='inaccurate_data')
router.register('inaccurate_recommendations', InaccurateRecomView, basename='inaccurate_recommendations')
router.register('broken_links', BrokenLinkView, basename='broken_links')
router.register('movie_movie', MovieMovieViewSet, basename='movie_to_movie')
router.register('movie_tv', MovieTvViewSet, basename='movie_to_movie')
router.register('tv_tv', TvTvViewSet, basename='movie_to_movie')
router.register('cast_member', CastViewSet, basename='cast_member')
router.register('missing_title', MissingTitleView, basename='missing_title')


urlpatterns = [
    path('tokens', CreateExistingToken.as_view(), name='gentoken_existing'),
    path('login', ObtainAuthTokenViewSet.as_view(), name='login'),

]

urlpatterns += router.urls