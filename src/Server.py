from utils.Utils import Utils


class Server:

    def __init__(self, cpu, ram, nic, disk):

        self.utils = Utils()

        self.vendor = self.init_vendor()
        self.model = self.init_model()

        self.serverCpu = cpu
        self.serverRam = ram
        self.serverNic = nic
        self.serverDisk = disk

    def init_vendor(self):
        return self.utils.produce_command("lscpu | grep 'Vendor ID' | awk '{print $3}'")

    def init_model(self):
        return self.utils.produce_command("lscpu | grep 'Model name' | awk '{print $3}'")
