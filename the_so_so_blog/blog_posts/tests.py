import requests
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from the_so_so_blog.blog_posts.models import BlogPost


pytestmark = pytest.mark.django_db(transaction=True)

def test_create_and_retrieve_new_blog(user, api_client):
    data = {
        "title": "test title",
        "content": "test content",
        "category": "PROG"
    }
    url = reverse("blog:create_post")
    response = api_client.post(url, data=data, format="json")
    assert response.status_code == status.HTTP_201_CREATED

    response_data = response.json()
    assert BlogPost.objects.count() == 1
    post = BlogPost.objects.get(pk=response_data["id"])
    assert response_data["title"] == post.title
    assert response_data["content"] == post.content
    assert response_data["category"] == post.category
    assert post.author.id == user.id


def test_update_blog(user, api_client):
    data = {
        "title": "test title",
        "content": "test content",
        "category": "PROG"
    }
    url = reverse("blog:create_post")
    response = api_client.post(url, data=data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    response_data = response.json()
    # update post
    url = reverse("blog:update_post", kwargs={"pk": response_data["id"]})
    data = {
        "title": "updated test title",
        "content": "updated test content",
        "category": "LIFE"
    }
    response = api_client.patch(url, data=data, format="json")
    updated_response_data = response.json()
    assert response.status_code == status.HTTP_200_OK
    post = BlogPost.objects.get(pk=updated_response_data["id"])

    assert BlogPost.objects.count() == 1
    assert updated_response_data["title"] == post.title
    assert updated_response_data["content"] == post.content
    assert updated_response_data["category"] == post.category
    assert post.author.id == user.id


def test_update_blog_with_different_user(user, user2, api_client):
    data = {
        "title": "test title",
        "content": "test content",
        "category": "PROG"
    }
    url = reverse("blog:create_post")
    response = api_client.post(url, data=data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    response_data = response.json()

    updated_data = {
        "title": "updated test title",
        "content": "updated test content",
        "category": "LIFE"
    }
    url = reverse("blog:update_post", kwargs={"pk": response_data["id"]})

    refresh = RefreshToken.for_user(user2)
    api_client.credentials(
        HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}"
    )
    response = api_client.patch(url, data=updated_data, format="json")
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_delete_blog(user, api_client):
    data = {
        "title": "test title",
        "content": "test content",
        "category": "PROG"
    }
    url = reverse("blog:create_post")
    response = api_client.post(url, data=data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    response_data = response.json()

    url = reverse("blog:delete_post", kwargs={"pk": response_data["id"]})
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert BlogPost.objects.count() == 0


def test_delete_blog_with_different_user(user, user2, api_client):
    data = {
        "title": "test title",
        "content": "test content",
        "category": "PROG"
    }
    url = reverse("blog:create_post")
    response = api_client.post(url, data=data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    response_data = response.json()

    url = reverse("blog:delete_post", kwargs={"pk": response_data["id"]})
    refresh = RefreshToken.for_user(user2)
    api_client.credentials(
        HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}"
    )
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert BlogPost.objects.count() == 1


@pytest.mark.parametrize(
    ("category,expected"),
    [
        ("PROG", status.HTTP_201_CREATED), ("LIFE", status.HTTP_201_CREATED),
        ("WRITTEN", status.HTTP_201_CREATED), ("MISC", status.HTTP_201_CREATED),
        ("SPORT", status.HTTP_400_BAD_REQUEST), ("FASHION", status.HTTP_400_BAD_REQUEST),
        ("ProG", status.HTTP_400_BAD_REQUEST), ("Prog", status.HTTP_400_BAD_REQUEST),
        ("life", status.HTTP_400_BAD_REQUEST), ("Life", status.HTTP_400_BAD_REQUEST),
    ]
)
def test_create_blog_categories(category, expected, user, api_client):
    data = {
        "title": "test title",
        "content": "test content",
        "category": category
    }
    url = reverse("blog:create_post")
    response = api_client.post(url, data=data, format="json")
    assert response.status_code == expected
