import pytest


@pytest.mark.api
def test_list_users(reqres_api):
    r = reqres_api.list_users()
#    print(r)
    assert r['data'] != 0

@pytest.mark.api
def test_list_user(reqres_api):
    user_num = 3
    r = reqres_api.list_user(user_num)
#    print(r['data']['id'])
    assert r['data']['id'] == user_num

@pytest.mark.api
def test_no_user(reqres_api):
    user_num = 23
    r = reqres_api.list_user(user_num)
#    print(r)
    assert r == {}

@pytest.mark.api
def test_list_resources(reqres_api):
    r = reqres_api.list_resources()
#    print(r)
    assert r['data'] != 0

@pytest.mark.api
def test_list_resource(reqres_api):
    res_num = 2
    r = reqres_api.list_resource(res_num)
#    print(r)
    assert r['data']['id'] == 2

@pytest.mark.api
def test_no_resource(reqres_api):
    res_num = 23
    r = reqres_api.list_resource(res_num)
#    print(r)
    assert r == {}
