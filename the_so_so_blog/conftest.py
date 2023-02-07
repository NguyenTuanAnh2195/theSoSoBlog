import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from the_so_so_blog.users.models import User


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user():
    user = User(
        username="test",
        is_active=True,
        is_admin=False,
        email="test@mail.com"
    )
    user.save()
    return user


@pytest.fixture
def user2():
    user = User(
        username="test 2",
        is_active=True,
        is_admin=False,
        email="test_2@mail.com"
    )
    user.save()
    return user


@pytest.fixture
def api_client(user):
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(
        HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}"
    )
    return client
