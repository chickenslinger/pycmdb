class Pycmdb:
    """Class to call cmdb api and return server lists object."""
    base_url = 'http://cmdb.etadirect.com/rest/'

    def __init__(self, instance):
        self.instance = instance

    def is_test(self):
        return 'test' in str(self.instance)

    def is_prod(self):
        return 'app' in str(self.instance)

    def is_instance(self):
        import requests
        company_instance = 'company_instance'
        cp_in = []
        data = requests.get(self.base_url+company_instance).json()
        for key, value in data.items():
            for i in value:
                cp_in.append(i['app_name'])
        return self.instance in cp_in


class Instance(Pycmdb):
    """Class to crate instance obj and return server info"""
    def build_fe_request(self):
        if self.is_test() is True:
            url_request = Pycmdb.base_url + 'test/server_view?search=%s&columns=FE' % self.instance
        elif self.is_prod() is True:
            url_request = Pycmdb.base_url + 'prod/server_view?search=%s&columns=FE' % self.instance
        return url_request

    def fe_server_list(self):
        import requests
        url_request = self.build_fe_request()
        response = requests.get(url_request)
        data = response.json()
        return data

    def build_bem_request(self):
        if self.is_test() is True:
            url_request = Pycmdb.base_url + 'test/server_view?search=%s&columns=BE_Master' % self.instance
        elif self.is_prod() is True:
            url_request = Pycmdb.base_url + 'prod/server_view?search=%s&columns=BE_Master' % self.instance
        return url_request

    def bem_master(self):
        import requests
        url_request = self.build_bem_request()
        response = requests.get(url_request)
        data = response.json()
        return data

    def build_db_request(self):
        if self.is_test() is True:
            url_request = Pycmdb.base_url + 'test/server_view?search=%s&columns=DB' % self.instance
        elif self.is_prod() is True:
            url_request = Pycmdb.base_url + 'prod/server_view?search=%s&columns=DB' % self.instance
        return url_request

    def db_slave(self):
        import requests
        url_request = self.build_db_request()
        response = requests.get(url_request)
        data = response.json()
        return data


class ServerGroups:
    """Creates server group object and returns list of all servers"""
    def __init__(self, url):
        self.url = url

    def server_group_list(self):
        import requests
        data = requests.get(self.url).json()
        sgl = []
        for key, value in data.items():
            for i in value:
                for key_l1, value_l1 in i.items():
                    for value_l2 in value_l1:
                        sgl.append(value_l2)
        return sgl

