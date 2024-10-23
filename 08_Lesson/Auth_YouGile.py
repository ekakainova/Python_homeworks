import requests


class Auth_YouGile:

    def __init__(self, url):
        self.url = url

    def get_list_of_companies(self, login = '', password = '', name = ''):
        company = {
            'login': login,
            'password': password,
            'name': name
        }

        resp = requests.post(self.url + '/auth/companies', json=company, headers={'Content-Type': 'application/json'})
        return resp.json()

    def create_key(self, company_id = '', login = '', password = ''):
        company = {
            'login': login,
            'password': password,
            'companyId': company_id
        }

        resp = requests.post(self.url + '/auth/keys', json=company, headers={'Content-Type': 'application/json'})
        return resp.json()

    def authorization(self, login = '', password = '', name = ''):
        company_info = self.get_list_of_companies(login, password, name)
        company_id = company_info["content"][0]["id"]

        get_key = self.create_key(company_id)
        return get_key["key"]
