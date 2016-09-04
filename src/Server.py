from utils.Utils import Utils


class Server:
    def __init__(self, cpu, ram, nics, disks):
        self.vendor = self.init_vendor()
        self.model = self.init_model()

        self.serverCpu = cpu
        self.serverRam = ram
        self.serverDisks = disks
        self.serverNics = nics

    @staticmethod
    def init_vendor():
        return Utils.produce_command("sudo dmidecode | grep -w 'Vendor:'")

    @staticmethod
    def init_model():
        return Utils.produce_command("sudo dmidecode -t system | awk -F: '$1~/Product Name/'")
