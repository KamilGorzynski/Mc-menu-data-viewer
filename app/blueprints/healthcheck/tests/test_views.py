

def test_index_route(client):
    response = client.get('/healthcheck/')
    assert response.status_code == 200
