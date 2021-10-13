import requests
from flask import jsonify

class deviceManager():
    """ Beschreibung """
    def __init__(self) -> None:
        self._device_list = []

    @property
    def devices(self):
        """List[:class:`device`]: Returns all connected devices."""
        return self._device_list


    def device_by_ip(self, ip):
        """Obj[:class:`device`]: Returns device objekt by given ip, false otherwise"""
        for d in self._device_list:
            if d.ip == ip:
                return d
        return False

    def is_inside(self, device):
        """:class:`Bool`: Returns True if device is allready connected, flase otherwise"""
        for d in self._device_list:
            if d.ip == device.ip:
                return True
        return False

    def add_device(self, device):
        """:class:`method`: Adds a device to device_list. Returns None"""
        self._device_list.append(device)

class device():
    """ Beschreibung """

    def __init__(self, ip, id) -> None:
        self.ip = ip
        self.id = id

    def to_json(self):
        return jsonify({
            'ip': self.ip,
            'id': self.id
        })
    
    def send_cmd(self,path,data):
        response = requests.post(f"http://{self.ip}:5000{path}", data)
        return response.text
