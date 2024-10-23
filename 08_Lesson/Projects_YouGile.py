import requests


class Projects_YouGile:

    def __init__(self, url):
        self.url = url

    def list_of_projects(self, api_key=''):
        my_headers = {
            'Content-Type': 'application/json'
        }
        my_headers['Authorization'] = f'Bearer {api_key}'

        resp = requests.get(self.url + '/projects', headers=my_headers)
        return resp.json()

    def get_users(self, api_key=''):
        projects = self.list_of_projects(api_key)
        users = projects["content"][0]["users"]
        return users

    def new_project(self, title, api_key=''):
        my_headers = {
            'Content-Type': 'application/json'
        }
        my_headers['Authorization'] = f'Bearer {api_key}'

        users = self.get_users(api_key)

        project = {
            'title': title,
            'users': users
        }

        resp = requests.post(self.url + '/projects',
                             json=project, headers=my_headers)
        return resp.json()

    def change_project(self, id_project, new_title, api_key='', deleted=True):
        my_headers = {
            'Content-Type': 'application/json'
        }
        my_headers['Authorization'] = f'Bearer {api_key}'

        users = self.get_users(api_key)

        project = {
            'deleted': deleted,
            'title': new_title,
            'users': users
        }

        resp = requests.put(self.url + f'/projects/{id_project}',
                            json=project, headers=my_headers)
        return resp.json()

    def get_project(self, id_project, api_key=''):
        my_headers = {
            'Content-Type': 'application/json'
        }
        my_headers['Authorization'] = f'Bearer {api_key}'

        resp = requests.get(self.url + f'/projects/{id_project}',
                            headers=my_headers)
        return resp.json()
