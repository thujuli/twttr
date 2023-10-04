import pytest


@pytest.mark.parametrize("content", ["Hello World", "Flask", "Web framework"])
def test_create_tweet(client, access_token_jhon, content):
    headers = {"Authorization": f"Bearer {access_token_jhon}"}

    # create new tweet
    response = client.post(
        "/api/tweets/",
        headers=headers,
        json={"content": content},
    )

    assert response.status_code == 201


def test_create_tweet_without_token(client):
    response = client.post("/api/tweets/", json={"content": "Hello World"})

    assert response.status_code == 401


def test_create_tweet_without_body(client, access_token_jhon):
    headers = {"Authorization": f"Bearer {access_token_jhon}"}
    response = client.post("/api/tweets/", headers=headers)

    assert response.status_code == 415


def test_create_tweet_without_json_data(client, access_token_jhon):
    headers = {"Authorization": f"Bearer {access_token_jhon}"}
    response = client.post("/api/tweets/", headers=headers, json={})

    assert response.status_code == 400


@pytest.mark.parametrize("content", [None, " "])
def test_create_tweet_with_invalid_json_data(client, access_token_jhon, content):
    headers = {"Authorization": f"Bearer {access_token_jhon}"}
    response = client.post("/api/tweets/", headers=headers, json={"content": content})

    assert response.status_code == 422


def test_get_tweets(client, access_token_jhon, tweets_jhon):
    headers = {"Authorization": f"Bearer {access_token_jhon}"}
    response = client.get("/api/tweets/", headers=headers)

    assert response.status_code == 200


def test_get_tweets_without_headers(client, tweets_jhon):
    response = client.get("/api/tweets/")

    assert response.status_code == 401
