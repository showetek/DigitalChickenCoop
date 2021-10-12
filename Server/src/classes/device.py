import requests

class device():
    """ Beschreibung """

    def __init__(self, ip, id) -> None:
        self.ip = ip
        self.id = id

    def send_cmd(self,path,data):
        response = requests.post(f"http://{self.ip}:5000{path}", data)
        return response.text
