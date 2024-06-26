import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user("andriicherniavskyi")
    assert r['message'] == 'Not Found'


#import pytest
#from modules.api.clients.gihub import GitHub
#
#
#@pytest.mark.api
#def test_user_exists():
#    api = GitHub()
#    user = api.get_user_defunkt()
#    assert user['login'] == 'defunkt'
#
#@pytest.mark.api
#def test_user_not_exists():
#    api = GitHub()
#    r = api.get_non_exist_user()
#    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
#    print(r['total_count'])
    assert r['total_count'] == 57
    assert 'become-qa-auto' in r['items'][0]['name'] 


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('cherniavskyi_repo_non_exist')
    assert r['total_count'] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('y')
    print(r['total_count'])
    assert r['total_count'] != 0

@pytest.mark.apitemp
def test_list_templates(github_api):
    r = github_api.list_gitignore_templates()
#    print(r)
    assert r != 0

@pytest.mark.apitemp
def test_template(github_api):
    template = 'RhodesRhomobile'
    r = github_api.get_template(template)
#    print(r)
    assert r['name'] == template


