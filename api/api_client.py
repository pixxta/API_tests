import requests


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_objects(self, ids=None):
        url = self.base_url + '/objects?' + '&'.join(f"id={id_}" for id_ in ids) if ids else self.base_url + '/objects'
        response = requests.get(url)
        return response

    def create_object(self, data):
        response = requests.post(self.base_url + '/objects', json=data)
        return response

    def get_object(self, object_id):
        response = requests.get(self.base_url + f'/objects/{object_id}/')
        return response

    def update_object(self, object_id, data):
        response = requests.put(self.base_url + f'/objects/{object_id}/', json=data)
        return response

    def delete_object(self, object_id):
        response = requests.delete(self.base_url + f'/objects/{object_id}/')
        return response


