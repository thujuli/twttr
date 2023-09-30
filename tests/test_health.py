def test_health_check(client):
    response = client.get("/api/health/")
    json_data = response.json

    assert response.status_code == 200
    assert json_data["status"] == "ok"
