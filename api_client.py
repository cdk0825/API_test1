import requests

class PostAPI:
    def __init__(self, base_url):
        self.base_url = f"{base_url}/posts"
        
    def get_all(self):
        return requests.get(self.base_url)
    
    def create(self, data):
        return requests.post(self.base_url, json=data)
    
    def update(self, post_id, data):
        return requests.put(f"{self.base_url}/{post_id}", json=data)
    
    def delete(self, post_id):
        return requests.delete(f"{self.base_url}/{post_id}")