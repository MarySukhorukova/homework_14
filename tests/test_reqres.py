import requests
from pytest_voluptuous import S
from schemas.user import register_user, base_url, login_user, create_user


def test_register_user():

    email = "eve.holt@reqres.in"
    password = "pistol"

    response = requests.post(f"{base_url}api/register",
                             json={
                                 "email": email,
                                 "password": password
                             })

    assert response.status_code == 200
    assert S(register_user) == response.json()
    assert len(response.json()['token']) == 17


def test_login_user():

    email = "eve.holt@reqres.in"
    password = "cityslicka"

    response = requests.post(f"{base_url}api/login",
                             json={
                                 "email": email,
                                 "password": password
                             })

    assert response.status_code == 200
    assert S(login_user) == response.json()
    assert len(response.json()['token']) == 17


def test_create_user():

    name = "harry potter"
    job = "wizard"

    response = requests.post(f"{base_url}api/users",
                             json={
                                 "name": name,
                                 "job": job
                             })

    assert response.status_code == 201
    assert S(create_user) == response.json()
    assert response.json()['name'] == name
    assert response.json()['job'] == job


def test_register_unsuccessful_user():

    email = "eve.holt@reqres.in"

    response = requests.post(f"{base_url}api/register",
                             json={
                                 "email": email
                             })

    assert response.status_code == 400
    assert response.json()['error'] == "Missing password"


def test_update_user():

    name = "harry potter"
    job = "wizard"

    response = requests.put(f"{base_url}api/users/2",
                             json={
                                 "name": name,
                                 "job": job
                             })

    assert response.status_code == 200
    assert response.json()['name'] == name
    assert response.json()['job'] == job


