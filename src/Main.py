from Cpu import Cpu
from Disks import Disks
from Nics import Nics
from Ram import Ram
from Server import Server
from utils.Utils import Utils


class Main:

    server = Server(cpu=Cpu(), ram=Ram(), nics=Nics(), disks=Disks())
    serverObject = {'Vendor' : server.vendor,
                'Model' : server.model,
                'Cpu': server.serverCpu.cpuObject,
                'Ram': server.serverRam.ramObject,
                'NICs' : server.serverNics.nicsObject,
                'Disks' : server.serverDisks.disksObject}

    print(Utils.convert_to_json(serverObject))
