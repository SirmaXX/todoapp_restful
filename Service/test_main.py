from fastapi.testclient import TestClient 

from .main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "Job"}



def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == True

#KULLANICI BÖLÜMÜNÜN TESTLERİ
def test_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert response.json() == {}

postuser={
  "username": "postuser1",
  "password": "deneme123"
}

def test_post_user():
    response = client.post("/users/add", json=postuser)
    assert response.status_code == 200
    assert response.json() == {}




def test_update_user():
    response = client.put("/users/2", json = {
    "id": 2,
    "username": "postuser123",
    "password": "son123"
  })
    assert response.status_code == 200
    assert response.json() == "string"




def test_delete_users():
    response = client.delete("/users/delete/10")
    assert response.status_code == 200
    assert response.json() =={}

