from reapy_boost.errors import DisconnectedClientError, DistError
from reapy_boost.tools import json
from .socket import Socket

from ipaddress import IPv4Address, ip_address

LOCALHOST = "127.0.0.1"


class Client(Socket):

    def __init__(self, port: int, host: IPv4Address = IPv4Address(LOCALHOST)):
        super().__init__()
        self._connect(port, host)
        self.port, self.host = port, host

    def _connect(self, port: int, host: IPv4Address):
        super().connect((str(host), port))
        self.address = self.recv(timeout=None).decode("ascii")

    def _get_result(self):
        s = self.recv(timeout=None).decode()
        return json.loads(s)

    def request(self, function, input=None):
        request = {"function": function, "input": input}
        request = json.dumps(request).encode()
        self.send(request)
        result = self._get_result()
        if result["type"] == "result":
            return result["value"]
        elif result["type"] == "error":
            raise DistError(result["traceback"])
