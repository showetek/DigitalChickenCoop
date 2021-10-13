import requests

class deviceManager():
    def __init__(self) -> None:
        self._device_list = {}

    @property
    def devices(self):
        """List[:class:`device`]: Returns all connected devices."""
        return self._device_list

class device():
    """ Beschreibung """

    def __init__(self, ip, id) -> None:
        self.ip = ip
        self.id = id

    
    def send_cmd(self,path,data):
        response = requests.post(f"http://{self.ip}:5000{path}", data)
        return response.text
