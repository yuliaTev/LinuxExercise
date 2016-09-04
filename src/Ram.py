from utils.Utils import Utils


class Ram:

    def __init__(self):
        self.ramSize = self.init_ram_size()

        self.ramObject = {'Size': self.ramSize}

    def init_ram_size(self):
        return Utils.produce_command("grep MemTotal /proc/meminfo | awk '{print $2}'")
        
    