from utils.Utils import Utils
from Cpu import Cpu
from Ram import Ram
from Disks import Disks
from Nics import Nics


class Server:
    def __init__(self, cpu=None, ram=None, nics=None, disks=None):
        self.vendor = self.init_vendor()
        self.model = self.init_model()

        self.serverCpu = cpu if cpu is not None else Cpu()
        self.serverRam = ram if ram is not None else Ram()
        self.serverDisks = disks if disks is not None else Disks()
        self.serverNics = nics if nics is not None else Nics()

    @staticmethod
    def init_vendor():
        # for my laptop, "sudo dmidecode | grep -w 'Manufacturer:' | head -1" returned better results..
        # anyway, I added the sed to cut the key and save only the value
        return Utils.produce_command("sudo dmidecode | grep -w 'Vendor:' | sed 's/^.*: //'")

    @staticmethod
    def init_model():
        return Utils.produce_command(
            "sudo dmidecode -t system | awk -F: '$1~/Product Name/' | sed 's/^.*: //'")
