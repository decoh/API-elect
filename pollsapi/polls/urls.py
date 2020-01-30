from django.urls import path, include
from .apiviews import PollList, PollDetail
from .apiviews import ChoiceList, CreateVote, UserCreate, LoginView
from rest_framework.routers import DefaultRouter
from .apiviews import PollViewSet
from rest_framework.authtoken import views
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls
from django.contrib import admin

schema_view = get_swagger_view(title='polls API')


router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')


urlpatterns = [
    path("polls/", PollList.as_view(), name="polls_list"),
    path("polls/<int:pk/", PollDetail.as_view(), name="polls_detail"),
    path("polls/<int:pk>/choices", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
    path("login/", views.obtain_auth_token, name="login"),
    path(r'swagger-docs/', schema_view),
    path(r'docs/', include_docs_urls(title='polls API')),
    path('rest-auth/', include('rest_auth.urls')),
    path('admin/', admin.site.urls),
]


urlpatterns += router.urls
