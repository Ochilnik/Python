import requests


class GitHub:
    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()

        return body


#import requests
#
#class GitHub:
#
#    def get_user_defunkt(self):
#        r = requests.get('https://api.github.com/users/defunkt')
#        body = r.json()
#
#        return body
#
#    def get_non_exist_user(self):
#        r = requests.get('https://api.github.com/users/andriicherniavskyi')
#        body = r.json()
#
#        return body    


    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories",
            params={"q": name}
        )
        body = r.json()

        return body

    def list_gitignore_templates(self):
        r = requests.get(
            'https://api.github.com/gitignore/templates'
        )
        body = r.json()
        return body

    def get_template(self, name):
        r = requests.get(
            f'https://api.github.com/gitignore/templates/{name}'
        )
        body = r.json()
        return body