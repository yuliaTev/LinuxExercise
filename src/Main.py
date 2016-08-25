from Cpu import Cpu
from Disk import Disk
from Nic import Nic
from Ram import Ram
from Server import Server
from utils.Utils import Utils


class Main:

    server = Server(Cpu(), Ram(), Nic(), Disk())
    serverObject = {'Vendor' : server.vendor,
                    'Model' : server.model,
                    'Cpu': server.serverCpu.cpuObject}

    print(Utils().convert_to_json(serverObject))
